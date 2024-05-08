import sys
import sm3Master


def main():
    # 检查参数数量是否正确
    if len(sys.argv) != 3:
        print("Usage: python main.py <origin_hash> <length>")
        return

    # 获取命令行参数
    origin_hash = sys.argv[1]
    length = int(sys.argv[2])

    # 计算
    append_data = sm3Master.generate_append_data(length)
    new_hash = sm3Master.sm3master(origin_hash, length)
    print("append_data: ", append_data)
    print("new_hash: ", new_hash)


if __name__ == "__main__":
    main()
