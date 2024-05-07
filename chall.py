# hash_append的脚本
import os
from gmssl import sm3, func

with open('flag') as f:
    flag = f.read()


MySecretInfo = os.urandom(64)
HashValue = sm3.sm3_hash(func.bytes_to_list(MySecretInfo))
print('MySecretInfo Hash:', HashValue)

AppendData = bytes.fromhex(input('Input AppendData: '))
assert len(AppendData) == 64
NewSecretInfo = MySecretInfo + AppendData
# 原来的明文跟附加数据相加后的sm3

GeneratedHash = input('Input NewSecretInfo Hash: ')
NewHashValue = sm3.sm3_hash(func.bytes_to_list(NewSecretInfo))
print(NewHashValue)

if GeneratedHash == NewHashValue:
    print(flag)
else:
    print('Nope')