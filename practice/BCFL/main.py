from web3 import HTTPProvider, Web3
import json
from eth_account import Account
from dotenv import load_dotenv
import os

# Need for .env
load_dotenv()

contract_json_path = "contract_info.json"

# WARNING! Rpc url should be in .env
provider_address = os.environ.get("RPC_URL")
w3 = Web3(HTTPProvider(provider_address))

# WARNING! 지갑 개인 키는 절대 공개된 형태로 깃허브에 올리시면 안됩니다. 해킹 당해요!
user_account = os.environ.get("USER_ACCOUNT")
user_pk = os.environ.get("USER_PK")

with open(contract_json_path,"r") as json_file:
    contract_info = json.load(json_file)
    abi = contract_info['abi']
    contract_address = contract_info['contract_address']

print(abi)
# ABI, contract address is needed for Web3 contract instance
contract = w3.eth.contract(abi=abi, address=contract_address)

def get_tx_param():
    nonce = w3.eth.getTransactionCount(user_account)
    tx_param = {
        "nonce":nonce,
        "gas":300000,
        "gasPrice":w3.toWei('50','gwei'),
        "from":user_account
    }
    return tx_param

def signedHash(tx, privatekey):
    signed_tx = Account.signTransaction(tx, privatekey)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash


def readDiary():
    date = input("Enter Diary's date : YYYYMMDD")
    date = int(date)
    diary = contract.functions.readDiary(date).call(get_tx_param())
    print(diary)

def addDiary():
    date = input("Enter Diary's data : YYYYMMDD")
    date = int(date)
    diary = input("Enter Diary's content")

    tx = contract.functions.addDiary(date,diary).buildTransaction(get_tx_param())
    tx_hash = signedHash(tx,user_pk)
    print(tx_hash)

if __name__ == '__main__':
    while True:
        num = input("press 1 to read diary and 2 to Add diary")
        if num == "1":
            readDiary()
        else :
            addDiary()

