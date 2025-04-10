## Data metadata

Data Source: [Carter MQ, et al. Genomic and Phenotypic Characterization of Shiga Toxin-Producing Escherichia albertii Strains Isolated from Wild Birds in a Major Agricultural Region in California. Microorganisms. 2023; 11(11):2803.](https://doi.org/10.3390/microorganisms11112803)


# 认识fastq格式文件

FASTQ文件格式最初由英国的**桑格研究所（Wellcome Trust Sanger Institute）**开发，目的是将FASTA序列与质量数据结合在一起。这种格式最初是为Sanger测序技术设计的，但随着高通量测序技术的发展，FASTQ格式因其简洁性和实用性，逐渐成为高通量测序数据存储的事实标准。它以纯文本形式存储生物序列及其质量分数，既便于读取，也易于解析。

## **FASTQ 文件格式**

- **第一行**：以“@”开头，后面是序列的标识符，可能包含序列的来源、位置等信息。
- **第二行**：是测序得到的核苷酸序列，通常由 A、T、C、G 这四个碱基组成。
- **第三行**：以“+”开头，后面可以是与第一行相同的标识符，也可以是空的，这取决于文件的格式。
- **第四行**：是QUAL质量值，每个碱基都有一个对应的 ASCII 字符表示其质量，ASCII 字符的值减去一个偏移量（通常是 33）就得到了该碱基的质量值，质量值越高，表示该碱基被测序得越准确。

示例：

```
@SRR23879812.87 V300098174L1C001R0010001015 length=50
GTCGTCATGGAAACTGGATGAAAGGCCATCTTTGTTATAAAGTGGCAAAG
+
BD?BD0<FF+BEACE=DDFEFECFCEEFDBEFFACFFFFFFE2FDEEEE=
```

## 熟悉质量值QUAL

QUAL质量值（Quality Score）是用于衡量测序数据中每个碱基的可信度的指标。它通过一个数值来表示碱基被正确测序的概率。质量值越高，表示该碱基的测序准确性越高。

QUAL质量值的计算基于测序错误率（$p_{\text{error}}$），使用以下公式：

_ $$ Q = -10 \log_{10}(p_{\text{error}}) $$ 其中：

- $Q$ 是质量值。
- $p_{\text{error}}$ 是该碱基被测序错误的概率。

例如：

- 如果某个碱基的测序错误率为 0.01（1%），则其质量值 $Q$ 为 20。
- 如果错误率为 0.001（0.1%），则 $Q$ 为 30。

# FASTA 与 FASTQ

FASTA格式仅存储生物序列（如DNA、RNA或蛋白质序列），它以一个大于号（`>`）开头，后跟序列的描述信息，紧接下一行是序列本身。FASTA格式简洁明了，便于存储和交换序列数据，但不包含质量信息。
```
>SRR23879812.87 V300098174L1C001R0010001015 length=50
GTCGTCATGGAAACTGGATGAAAGGCCATCTTTGTTATAAAGTGGCAAAG
```

# gzip压缩文件（.gz后缀）

Gzip（GNU zip）是一种广泛使用的文件压缩格式，最初由Jean-loup Gailly和Mark Adler开发。它基于DEFLATE算法，能够高效地压缩数据，同时保持较高的压缩比。Gzip格式的文件通常以`.gz`作为文件扩展名。

Gzip格式被大多数操作系统和编程语言支持，包括Linux、Windows、macOS等。
许多生物信息学工具（如`fastp`、`bgzip`等）可以直接处理Gzip压缩的文件，无需先解压。

在生物信息学中，Gzip格式常用于压缩FASTQ、FASTA等文件。这些文件通常很大，压缩后可以显著减少存储空间和传输时间。例如一个10GB的FASTQ文件经过Gzip压缩后可能只有2GB左右。

在网络传输中，Gzip格式的文件可以减少传输时间，提高传输效率。许多Web服务器和客户端支持Gzip压缩的HTTP传输。Gzip格式的文件也可以用于数据备份，节省存储空间，同时保持数据的完整性和可读性。

## 操作方法
1. **压缩文件**：
   - 在Linux系统中，可以使用`gzip`命令压缩文件：
     ```bash
     gzip -k input.txt  # 压缩文件，保留原始文件
     gzip input.txt     # 压缩文件，不保留原始文件
     ```
   - 在Windows系统中，可以使用第三方工具（如7-Zip、WinRAR等）来压缩文件为Gzip格式。

2. **解压文件**：
   - 在Linux系统中，可以使用`gunzip`命令解压文件：
     ```bash
     gunzip input.txt.gz  # 解压文件
     gzip -dc input.txt.gz # 作用相同
     ```
   - 在Windows系统中，同样可以使用第三方工具解压Gzip格式的文件。

3. **查看压缩文件内容**：
   - 在Linux系统中，可以使用`zcat`命令查看压缩文件的内容：
     ```bash
     zcat input.txt.gz  # 查看压缩文件内容
     ```
   - 如果需要编辑压缩文件，可以先解压，编辑后再重新压缩。


#### 六、总结
Gzip格式是一种高效、广泛支持的文件压缩格式，特别适用于生物信息学中的大规模数据处理。通过压缩文件，可以显著减少存储空间和传输时间，同时保持数据的完整性和可读性。在生物信息学领域，许多工具（如`fastp`、`bgzip`等）直接支持Gzip格式，使得数据处理更加高效和便捷。

# 质量控制

FASTQ文件的质量控制是生物信息学分析中的关键步骤，目的是去除低质量数据、检测测序偏差、确保数据完整性，从而提高下游分析的准确性和可靠性。质量控制通常包括以下几个方面：
1. **去除低质量reads**：根据质量值（如Phred质量值）过滤掉质量低于一定阈值的reads。
2. **去除接头序列**：识别并去除测序过程中引入的接头序列。
3. **质量剪切**：对reads的两端或中间低质量区域进行剪切。
4. **去除含N碱基过多的reads**：N碱基表示不确定的碱基，过多的N碱基可能影响后续分析。
5. **统计分析**：生成质量报告，包括碱基质量分布、GC含量分布、错误率分布等。

常用的FASTQ文件质量控制工具有`FastQC`、`fastp`、`Trimmomatic`等。其中，`fastp`因其高效性和多功能性而被广泛使用。

其中，`fastp`是一款由陈实富开发的高效质量控制工具，它集成了`FastQC`和`Trimmomatic`的功能，能够快速完成质量评估、过滤低质量序列、去除接头序列等操作。`fastp`支持多线程处理，速度非常快。

1. **安装方法**
   - 使用`wget`下载并赋予可执行权限：
     ```bash
     wget http://opengene.org/fastp/fastp
     chmod a+x ./fastp
     ```
   - 通过`conda`安装：
     ```bash
     conda install -c bioconda fastp
     ```

2. **基本使用**
   - 单端数据处理：
     ```bash
     fastp -i input.fq -o output.fq
     ```
   - 双端数据处理：
     ```bash
     fastp -i input_R1.fq.gz -I input_R2.fq.gz -o output_R1.fq.gz -O output_R2.fq.gz
     ```

3. **高级参数**
   - 设置线程数、质量阈值等：
     ```bash
     fastp --thread 2 --qualified_quality_phred 15 --unqualified_percent_limit 50 --n_base_limit 10 --length_required 50 --detect_adapter_for_pe -i data/SRR22673379_1.fastq.gz -I data/SRR22673379_2.fastq.gz -o  data/SRR22673379_clean_2.fastq.gz -O  data/SRR22673379_clean_1.fastq.gz -h data/SRR22673379_fastp_report.html -j data/SRR22673379_fastp_report.json
     ```
     其中：
     - `--thread`：指定线程数。
     - `--qualified_quality_phred`：设置质量阈值。
     - `--unqualified_percent_limit`：设置低质量碱基的百分比阈值。
     - `--n_base_limit`：设置N碱基的最大数量。
     - `--length_required`：设置过滤后reads的最小长度。
     - `--detect_adapter_for_pe`：自动检测并去除双端测序数据中的接头序列。
     - `-h`：指定HTML报告文件名。
     - `-j`：指定JSON报告文件名。

`fastp`会生成HTML格式的报告，方便检查质量控制结果。

# 作业  

对其他data目录下的fastq数据进行质控，熟悉通过生信工具处理数据的过程。


# FAQ

## 这些数据是如何从NCBI下载并处理的？

利用NCBI的SRA-tools

```
awk -F, 'FNR>1{gsub("\"","");print $1}' \
  data/sra_result.csv > data/SRX_ACC_LIST.txt

prefetch -p --option-file data/SRX_ACC_LIST.txt

for i in `cat data/SraAccList.csv`;do
  fastq-dump --split-files --gzip $i &
done
```

随机抽样：

```
for i in `ls *fastq.gz`;do 
  seed=$(echo $i|cut -c4-11);
  gzip -dc $i | seqkit sample -p 0.01 -s $seed | gzip > data/$i &
done
```

将downsize的数据放入dvc 缓存：

```
dvc add data/*.gz
```