## GPU 이용할 계획이 있다면 드라이버 및 쿠다 설치
- https://www.nvidia.co.kr/Download/index.aspx <- conda
- https://developer.nvidia.com/cuda-11-7-0-download-archive <- cuda
- https://developer.nvidia.com/rdp/cudnn-archive <-cudnn

## Conda 설치
- https://www.anaconda.com/products/individual
- Sh 파일로 받았다면, $./Anaconda3-2021.11-Linux-x86_64.sh

## Conda 환경 구축
```
conda create -n pytorch python=3.9
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install captum –c pyotorch
pip install wandb
```

## Pycharm install
"https://www.jetbrains.com/ko-kr/pycharm/download/
•학교 계정이 있고, 연구실 서버를 외부에서 이용할 계획이 있다면 Professional 버전 추천
•https://cosmosproject.tistory.com/480 
<- interpreter 설정 / professional 버전이라면 ssh 외부 interpreter 설정가능

## Tqdm install
•conda install -c conda-forge tqdm

## Numpy install
Pip install numpy

## Matplotlib install
Pip install matplotlib

```
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
```
