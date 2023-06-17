# 引入必要的模块
import csv

# 读取文件的函数
def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

# 处理数据的函数
def process_data(data):
    processed_data = []
    for row in data:
        # 这里只是一个示例，你可以根据实际情况处理数据
        processed_row = [item.upper() for item in row]
        processed_data.append(processed_row)
    return processed_data

# 写入文件的函数
def write_file(data, filename):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

# 主函数
def main():
    data = read_file('input.csv')  # 读取名为'input.csv'的文件
    processed_data = process_data(data)  # 处理数据
    write_file(processed_data, 'output.csv')  # 写入名为'output.csv'的文件

# 调用主函数
if __name__ == "__main__":
    main()
