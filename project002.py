import json,requests
from web3 import Web3
response = requests.get("https://api.pancakeswap.info/api/v2/pairs")
data = response.json()["data"].values()
results = list()
class smartContracts:
   def __init__(self):
        self.add = list()
   def build(self,name):
        self.add.append(name)
   def build1(self,loc):
        self.add[-1].append(loc)
values = smartContracts()
for i in data:
    values.build([i["base_symbol"]])
    values.build1(i["base_address"])
    values.build1(i["quote_symbol"])
    values.build1(i["quote_address"])
    values.build1(i["pair_address"])
    values.build1(i["liquidity"])
#print(values.add)
j=0
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
while j<len(values.add):   
     abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')
     balance1=web3.eth.contract(address=str(values.add[j][1]), abi=abi).functions.balanceOf(web3.toChecksumAddress(str(values.add[j][4]))).call()
     balance2=web3.eth.contract(address=str(values.add[j][3]), abi=abi).functions.balanceOf(web3.toChecksumAddress(str(values.add[j][4]))).call()
     results.append([values.add[j][0],values.add[j][2],float(web3.fromWei(balance2, "ether"))/float(web3.fromWei(balance1, "ether"))])
     j+=1
print(results)