#combination

# this code mainly combines the tokened file from the folder to test whether there is an influence of text length on the outcome of the normalizeion
# tend to prevent overfitting

import os

# 指定包含 txt 文件的文件夹路径
folder_path = r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tokens\token_example_product_JP" # 替换为你的文件夹路径
output_file = r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tokens\longer_token_JP\longer_JP.txt"  # 输出的合并文件名

# 创建或打开合并文件
with open(output_file, 'w', encoding='utf-8') as outfile:
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为 txt 文件
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            # 读取每个 txt 文件的内容并写入合并文件
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write('\n')  # 添加换行符以分隔不同文件的内容

print(f'所有 txt 文件已合并到 {output_file}')