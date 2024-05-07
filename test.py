import os
from gmssl import sm3, func
import sm3Master

length = 64
origin_info = os.urandom(length)
origin_hash = sm3.sm3_hash(func.bytes_to_list(origin_info))

append_data = sm3Master.generate_append_data(length)

new_info = origin_info + bytes.fromhex(append_data)
new_hash = sm3.sm3_hash(func.bytes_to_list(new_info))
print(new_hash)

attack_hash = sm3Master.sm3master(origin_hash, length)
print(attack_hash)

if new_hash == attack_hash:
    print("attack success")