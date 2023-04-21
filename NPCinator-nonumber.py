#!/usr/bin/env python

import random
import argparse

parser = argparse.ArgumentParser(description='生成随机组合的词语')
parser.add_argument('--num', type=int, help='生成的行数')
args = parser.parse_args()
num = args.num

if num is None:
    num = 10

# 打开文件并读取内容
with open('adjectives.txt') as adj_file, open('nouns.txt') as noun_file:
    adjectives = adj_file.readlines()
    nouns = noun_file.readlines()

for i in range(num):

    # 随机选择一行字符串
    adj = random.choice(adjectives).strip()
    noun = random.choice(nouns).strip()

    # 拼接字符串并输出结果
    result = adj + ' ' + noun
    print(result)
