# Data Version Control

### Data Version Control（数据版本控制）的概念介绍

**数据版本控制（Data Version Control，简称 DVC）** 是一种用于管理数据和模型版本的工具，它借鉴了软件开发中版本控制系统（如 Git）的思想，旨在帮助数据科学家和机器学习工程师更好地管理数据集、模型及其依赖关系。DVC 允许用户跟踪数据和模型的变化，记录实验过程，并确保团队协作的高效性和可重复性。

#### 重要性
1. **可重复性**：DVC 确保数据和模型的每个版本都有明确的记录，使得实验结果可以被准确重现。这对于科学研究和工业应用中的验证和审计至关重要。
2. **协作效率**：通过版本控制，团队成员可以轻松共享数据和模型，避免重复工作，提高协作效率。
3. **数据管理**：DVC 提供了一种结构化的方式来管理大量数据，包括数据的存储、版本跟踪和缓存，从而优化数据的使用和存储。
4. **模型追踪**：DVC 不仅管理数据，还可以跟踪模型的训练过程和参数，帮助用户理解模型的演变和性能变化。
5. **实验管理**：DVC 支持实验的版本控制，允许用户回溯到特定的实验状态，便于调试和优化。

#### 主要原则
1. **版本控制**：DVC 通过创建数据和模型的版本，记录每次更改的详细信息，包括数据的来源、处理过程和模型的训练参数。
2. **依赖管理**：DVC 跟踪数据和模型（或算法、流程、分析过程）之间的依赖关系，确保每次运行的环境和输入数据的一致性。
3. **分布式缓存**：DVC 使用分布式缓存来存储数据和模型的副本，减少重复数据的存储，提高数据传输效率。
4. **与 Git 集成**：DVC 与 Git 无缝集成，将数据和代码的版本控制统一管理，方便团队协作和代码复用。
5. **可扩展性**：DVC 支持多种数据存储和计算环境，包括本地文件系统、云存储和分布式计算平台，适应不同规模的项目需求。

# Practice

## Configure mamba source
Refer to [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn) or other mirrors. This could speed up the downloading process of large packages.  

## Install dvc

```bash
mamba install -c conda-forge dvc dvc-ssh

```

## Configure dvc

```bash
git pull origin train2025

git checkout biociao

dvc remote add -d train2025 ssh://student@train2025.biociao.cc/home/student/DATA/bestPractice_dvc_cache

dvc remote modify train2025 user student
dvc remote modify --local train2025 password <THEPASSWD>
```
> replace '<THEPASSWD>' with the real password.

## Get data from dvc
1. update the repo with `git pull origin train2025`

2. get the data with `dvc pull`
```bash
dvc pull ciao/airway_n8.prof.csv.tar.gz.dvc
```
Successed if you see:
```
A       airway_n8.prof.csv.tar.gz
1 file added
```

## Generate a demo data file by your own
See the example codes in `ciao/GrabData.Rmd`.
Export any data you want to file named like `<Yourname>/airway_n8.prof.csv`.

Add data:
```bash
cd <Yourname>

# Compress the data to reduce the size.
tar czf airway_n4.prof.csv.tar.gz airway_n8.prof.csv

dvc add airway_n4.prof.csv.tar.gz
```
The message should be like:
```
100% Adding...|████████████████████████████████|1/1 [00:00, 15.31file/s]
```

push data to remote cache:
```bash
dvc push airway_n4.prof.csv.tar.gz.dvc
```
The message should be like:
```
A       airway_n4.prof.csv.tar.gz.dvc
1 file added
```

git commit:
```bash
git add airway_n4.prof.csv.tar.gz.dvc ../.dvc/config
git commit -m "Add dvc file airway_n4.prof.csv.tar.gz"
```

## Sync data between local and remote


Grab your data on the server:
After login to the server:
```bash
cd <Yourname>
source .bashrc

mamba install -c conda-forge dvc dvc-ssh

cd Bestpractice4MGWAS
```

由于内网的gitlab站点没法跟跟公网互联，咱们用自己的笔记本做跳板。  
因此现在服务器上初始化一个仓库：
```bash
mkdir -p BestPractices4MGWAS
cd BestPractices4MGWAS
git init
```

然后在本地（自己笔记本上）
```bash
git remote add bgigpd student@train2025.biociao.cc:/home/student/biociao/BestPractices4MGWAS

git push -u bgigpd train2025 fangchao
```

看到类似一下信息说明成功：
```bash

student@124.71.16.51's password:
Enumerating objects: 193, done.
Counting objects: 100% (193/193), done.
Delta compression using up to 8 threads
Compressing objects: 100% (118/118), done.
Writing objects: 100% (193/193), 91.10 KiB | 30.37 MiB/s, done.
Total 193 (delta 56), reused 129 (delta 36), pack-reused 0
remote: Resolving deltas: 100% (56/56), done.
To train2025.biociao.cc:/home/student/biociao/BestPractices4MGWAS
 * [new branch]      train2025 -> train2025
 * [new branch]      fangchao -> fangchao
branch 'train2025' set up to track 'bgigpd/train2025'.
branch 'fangchao' set up to track 'bgigpd/fangchao'.
```

Then back to our server:
```bash
cd /home/student/biociao/BestPractices4MGWAS
git checkout fangchao
```

Configure shared cache:
```bash
dvc cache dir --local /home/student/DATA/bestPractice_dvc_cache
dvc config --local cache.shared group
dvc config --local cache.type symlink
```

将data从cache中拉取出来：
```bash
dvc checkout ciao/airway_n4.prof.csv.tar.gz.dvc
```