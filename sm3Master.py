from gmssl import sm3


# sm3任意长度拓展攻击脚本(大概，如果没写错的话，当然是不可能超过2^512bit的)

# 把十六进制字符串拆分成8个为一个单位的字符串，用于把旧的hash拆分为新的IV
def split_hex_string(hex_string):
    hex_list = [int(hex_string[i:i + 8], 16) for i in range(0, len(hex_string), 8)]
    return hex_list


def generate_append_data(length):
    if length % 64 < 56:
        left_length = 2 * (64 - length % 64) - 10
        append_data = "80" + left_length * "0" + hex(length * 8)[2:].zfill(8)
    else:
        left_length = 64 - length % 64 - 1
        append_data = '80' + left_length * '0' + 120 * '0' + hex(length * 8)[2:].zfill(8)
    return append_data


# length是字符串的长度，64个Byte
def sm3master(origin_hash, length):
    # 把旧的hash拆分为新的IV
    new_IV = split_hex_string(origin_hash)
    result = ""
    # 根据length的长度生成append_data，其实就是补全操作
    append_data = generate_append_data(length)
    # 长度是算的bit，要乘8；length是字符串，乘8，append_data是hex，乘4
    final_length = length * 8 + len(append_data) * 4
    # 根据新的msg(info+append_data)生成的new_B
    new_B = '80' + 118 * '0' + hex(final_length)[2:].zfill(8)
    new_B = bytes.fromhex(new_B)
    new_B = [i for i in bytes(new_B)]
    y = sm3.sm3_cf(new_IV, new_B)
    for i in y:
        result = '%s%08x' % (result, i)
    return result
