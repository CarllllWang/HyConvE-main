# -- coding: utf-8 --
# @Time: 2022-10-05 22:04
# @Author: WangCx
# @File: process
# @Project: HyConv_64_2



with open("./train.txt") as f:
    for line in f.readlines():
        line = line.strip().split("\t")
        rel = line[0]
        ents = line[1:]

