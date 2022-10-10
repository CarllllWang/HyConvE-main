# -- coding: utf-8 --
# @Time: 2022-10-05 19:36
# @Author: WangCx
# @File: process_2
# @Project: HyConv_64_2

tuples = []

with open("../JF17K-3/valid.txt") as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        if len(line) != 4:
            print(line)
        rel = line[0]
        ents = line[1:]

        tuples.append([rel] + ents)
    f.close()

print(len(tuples))

with open("../JF17K-3/valid.txt", "w") as f:
    for tuple_ in tuples:
        for i in range(len(tuple_)):
            if i != len(tuple_) - 1:
                f.write(tuple_[i] + "\t")
            else:
                f.write(tuple_[i])
        f.write("\n")
    f.close()
