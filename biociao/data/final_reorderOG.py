#!/usr/bin/env python3
import gzip
import csv
import os
import shutil
from collections import defaultdict

# 读取并排序 odb12v1_OGs.tab.gz 文件，同时为每个类别分配一个唯一的ID
sorted_ogs = []
category_id_map = {}
category_counter = 1

with gzip.open('biociao/data/odb12v1_gene_xrefs.tab_fix.gz', 'rt') as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split('\t')
            if len(parts) >= 3:
                og_id, gene_id, name = parts[1], parts[0], parts[2]
                # 为每个唯一的类别分配一个ID
                if name not in category_id_map:
                    category_id_map[name] = f'C{category_counter:04d}'
                    category_counter += 1
                    #print(f'Category: {name}, ID: {category_id_map[name]}, Gene ID: {gene_id}')
                sorted_ogs.append((name, og_id, gene_id))
            # 添加一个进度条显示已处理的category的数量
            if len(sorted_ogs) % 1000 == 0:
                print(f'Processed {len(sorted_ogs)} categories.',end="\r")

print(f'Processed {len(sorted_ogs)} categories.')

# 按类别名称排序
sorted_ogs.sort(key=lambda x: x[0])

# 将排序后的文件写入新的文件中
with gzip.open('odb12v1_OGs_sorted.tab.gz', 'wt') as f:
    for name, og_id, gene_id in sorted_ogs:
        f.write(f'{og_id}\t{gene_id}\t{name}\n')

# 创建基因ID到类别ID的映射
gene_to_category = {}
for name, og_id, gene_id in sorted_ogs:
    category_id = category_id_map[name]
    gene_to_category[gene_id] = category_id

# 清空输出目录
output_dir = 'output'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# 流式处理序列文件
current_id = None
current_sequence = []
with gzip.open('biociao/data/odb12v1_aa_fasta_fix.gz', 'rt') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            # 处理前一个序列
            if current_id and current_id in gene_to_category:
                category_id = gene_to_category[current_id]
                seq_str = ''.join(current_sequence)
                filename = os.path.join('output', f'{category_id}.fa')
                with open(filename, 'a') as out_file:
                    out_file.write(f'>{current_id}\n{seq_str}\n')
            
            # 开始新序列
            current_id = line[1:].split()[0]
            current_sequence = []
        else:
            current_sequence.append(line)
    
    # 处理最后一个序列
    if current_id and current_id in gene_to_category:
        category_id = gene_to_category[current_id]
        seq_str = ''.join(current_sequence)
        filename = os.path.join('output', f'{category_id}.fa')
        with open(filename, 'a') as out_file:
            out_file.write(f'>{current_id}\n{seq_str}\n')

print('Processing completed.')
