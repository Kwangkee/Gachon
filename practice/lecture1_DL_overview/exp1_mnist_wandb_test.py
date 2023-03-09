import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import numpy as np
import random
from tqdm import tqdm
import wandb
from captum.attr import LayerIntegratedGradients, IntegratedGradients,Occlusion
from captum.attr import visualization as viz
from matplotlib.colors import LinearSegmentedColormap
import math
import matplotlib.pyplot as plt
import torch.nn as nn

#linear model for mnist

# wandb 사용을 위함
wandb.init(project="mnist", entity="daeyeolkim")

# 재현성을 위한 세팅
random_seed = 0
torch.manual_seed(random_seed)
torch.cuda.manual_seed(random_seed)
torch.cuda.manual_seed_all(random_seed)  # if use multi-GPU
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
np.random.seed(random_seed)
random.seed(random_seed)

# 하이퍼 파라미터 세팅
lr = 1e-3
batch_size = 256
num_epoch = 10
# 저장 경로 세팅
ckpt_dir = './checkpoint'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 데이터 로드
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=(0.5,), std=(0.5,))])

train_dataset = datasets.MNIST(download=True, root='./', train=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=batch_size,shuffle=True, num_workers=0)

test_dataset = datasets.MNIST(download=True, root='./', train=False, transform=transform)
test_loader = DataLoader(test_dataset, batch_size=batch_size,shuffle=False, num_workers=0)

train_num_data = len(train_loader.dataset)
train_num_batch = np.ceil(train_num_data / batch_size)

test_num_data = len(test_loader.dataset)
test_num_batch = np.ceil(test_num_data / batch_size)

# 모델 선언
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x):
        x = x.view(-1, 784)
        x = self.linear(x)
        x = nn.Softmax(dim=1)(x)
        return x

# 네트워크 호출 및 optimizer, criterion 선언
model = Model().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=lr)
criterion = torch.nn.CrossEntropyLoss()

fn_acc = lambda pred, label: ((pred.max(dim=1)[1] == label).type(torch.float)).mean()
wandb.watch(model, criterion, log="all", log_freq=10)

for epoch in range(num_epoch):
    with tqdm(train_loader, total=len(train_loader), unit='batch') as tepoch:

        tepoch.set_description("Train" + "%d" % epoch)

        model.train()

        loss_arr = []
        acc_arr = []

        for i, (x, y) in enumerate(tepoch):

            x = x.to(device)
            y = y.to(device)

            optimizer.zero_grad()

            pred = model(x)

            loss = criterion(pred, y)
            acc = fn_acc(pred, y)

            loss.backward()

            optimizer.step()

            loss_arr += [loss.item()]
            acc_arr += [acc.item()]

            tepoch.set_postfix({'': 'TRAIN: EPOCH %04d/%04d | BATCH %04d/%04d | LOSS: %.4f | ACC %.4f' % (epoch, num_epoch, i, train_num_batch, np.mean(loss_arr), np.mean(acc_arr))})
        wandb.log({'loss': np.mean(loss_arr), 'acc': np.mean(acc_arr)})

    with tqdm(test_loader, total=len(test_loader), unit='batch') as tepoch:

        tepoch.set_description("Test" + "%d" % epoch)

        model.eval()
        loss_arr = []
        acc_arr = []

        for i, (x, y) in enumerate(tepoch):

            x = x.to(device)
            y = y.to(device)

            pred = model(x)

            loss = criterion(pred, y)
            acc = fn_acc(pred, y)

            loss_arr += [loss.item()]
            acc_arr += [acc.item()]

            tepoch.set_postfix({'': 'TEST: EPOCH %04d/%04d | BATCH %04d/%04d | LOSS: %.4f | ACC %.4f' % (epoch, num_epoch, i, test_num_batch, np.mean(loss_arr), np.mean(acc_arr))})
        wandb.log({'test_loss': np.mean(loss_arr), 'test_acc': np.mean(acc_arr)})


# 모델 저장
torch.save(model.state_dict(), ckpt_dir + '/model.pth')

