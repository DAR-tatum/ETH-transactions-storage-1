from web3 import Web3

try:
    web3 = Web3(Web3.HTTPProvider("http://52.20.37.157:8545"))
    #web3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8546"))
    #web3 = Web3(Web3.IPCProvider("/home/geth/.ethereum/geth.ipc"))
    print(web3.eth.block_number)
except Exception as e:
  print(f"An error occurred: {e}")
