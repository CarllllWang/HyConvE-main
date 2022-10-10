# -- coding: utf-8 --
# @Time: 2022-03-27 19:35
# @Author: WangCx
# @File: tmp
# @Project: HypergraphNN


file = ["train.txt", "test.txt", "valid.txt"]

ent2id = {}
rel2id = {}
i = 0
j = 0
for filename in file:
    with open("../JF17K-3/{}".format(filename)) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split("\t")
            ents = line[1:]
            rel = line[0]
            if rel not in rel2id:
                rel2id[rel] = j
                j += 1
            for ent in ents:
                if ent not in ent2id:
                    ent2id[ent] = i
                    i+=1

print(len(ent2id))
print(len(rel2id))
print(rel2id)

with open("../JF17K-3/entities.dict", "w") as f:
    for ent, idx in ent2id.items():
        f.write(str(idx) + "\t" + ent)
        f.write("\n")
    f.close()

with open("../JF17K-3/relations.dict", "w") as f:
    for rel, idx in rel2id.items():
        f.write(str(idx) + "\t" + rel)
        f.write("\n")
    f.close()