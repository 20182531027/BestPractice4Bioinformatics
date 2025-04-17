
# 序列比对

在生信领域主要有以下几类比对工具：

### 基于种子哈希和贪婪算法的比对工具

- **BLAT** ：适用于较短的序列比对，速度快，但对长序列比对效果不佳，且对序列质量要求较高，对低质量序列比对不准确。
- **MAQ** ：专门用于高通量测序数据的比对和 SNP 检测，准确性和速度都较好，但对内存要求较高，且不支持长序列比对。
- **SHRiMP** ：基于位模式匹配和 Smith-Waterman 算法，能有效处理长序列和低质量序列的比对，但速度较慢。

### 基于 Burrows-Wheeler Transform 算法的比对工具

- **BWA** ：比对速度快，准确率高，资源占用低，对短序列和长序列的比对效果都很好，是目前常用的基因组比对工具之一，但对长序列和低质量序列的处理能力相对较弱。
- **Bowtie** ：速度快，内存占用低，适用于大规模数据的快速比对，但对长序列和低质量序列的处理能力有限，且不支持 SNP 检测。
- **SOAP** ：比对准确率高，资源占用低，适用于全基因组比对和 SNP 检测，但对长序列和低质量序列的处理能力有限，且速度较慢。

### 基于其他算法或技术的比对工具

- **HISAT2** ：专为 RNA-Seq 数据设计，基于 Ferragina-Manzini 索引和 GraphFM 索引，能快速准确地比对 RNA-Seq 数据，尤其在处理可变剪接方面表现出色，速度较快，准确率高。
- **STAR** ：也是为 RNA-Seq 数据设计，采用两步比对策略，先构建基因组索引，再进行比对，能高效处理大量数据，准确率高，速度较快，还支持可变剪接和融合基因的检测。
- **Kallisto** ：基于 k-mer 的轻量化比对工具，无需构建基因组索引，比对速度快，资源占用低，适用于大规模数据的快速分析，但准确率相对较低。
- **Salmon** ：同样基于 k-mer，采用准映射方法，在保证速度的同时，也能提供较高的准确率，并且可以自动判断测序类型。
- **Kraken** ：基于 k-mer 匹配算法，通过与数据库中的序列进行比对，快速识别样本中的不同物种，分类精准，速度快，内存占用低，适用于宏基因组研究，但结果解释复杂，效果依赖于参考数据库。


## 原理理解  

以BWA为例，Burrows-Wheeler Transform（BWT）算法是一种用于数据压缩和比对的算法，它通过重新排列字符串来提高数据的可压缩性。其核心思想是通过对原始字符串进行特定的旋转和排序操作，将相似的字符聚集在一起，从而增加数据的冗余度，使得后续的压缩算法能够更有效地进行压缩。

其过程简单描述如下：  

假设原始序列为：`GATAGAG`

### 1. 添加终止符

为了标记序列的结束，我们通常在序列的末尾添加一个特殊的终止符，比如 `$`。这样处理后的序列为：`GATAGAG$`

### 2. 生成所有循环旋转

将序列进行所有可能的循环旋转，得到以下旋转列表：

| 旋转索引 | 旋转后的序列 |
| -------- | ------------ |
| 0        | GATAGAG$     |
| 1        | ATAGAG$G     |
| 2        | TAGAG$GA     |
| 3        | AGAG$GAT     |
| 4        | GAG$GATA     |
| 5        | AG$GATAG     |
| 6        | G$GATAGA     |
| 7        | $GATAGAG     |

### 3. 按字典序排序

将所有旋转后的序列按字典序进行排序。DNA 序列的字典序通常按照以下顺序排列：`$ < A < C < G < T`。

排序后的旋转列表如下：

| 排序索引 | 旋转后的序列 |
| -------- | ------------ |
| 0        | $GATAGAG     |
| 1        | AG$GATAG     |
| 2        | AGAG$GAT     |
| 3        | ATAGAG$G     |
| 4        | G$GATAGA     |
| 5        | GATAGAG$     |
| 6        | GAG$GATA     |
| 7        | TAGAG$GA     |

### 4. 提取最后一列

从排序后的列表中提取每个字符串的最后一列字符，得到一个新的字符串，这就是 BWT 转换后的结果。

提取后的最后一列字符：`G$GAGATG`。  可以看到`GA`与`GA`靠得更近了，这对于多数数据压缩算法来说都能获得较高得压缩率。  

在 BWT 转换的基础上，BWA 还会构建 FM-Index。FM-Index 是一种基于 BWT 的索引结构，它记录了每个字符在 BWT 变换后字符串中的出现次数和位置信息。如此一来，可以通过统计每个字符在参考序列中出现的次数和起始位置，快速确定查询序列中某个字符或子字符串在参考序列中的可能位置范围。这避免了在整个参考序列中逐个位置进行比对，从而大大缩小了搜索范围。提升了比对得速度和效率。

在比对过程中，BWA 使用种子（seed）来快速定位可能的匹配区域。种子长度通常是一个较短的子字符串（例如，28bp 到 32bp），用于在参考基因组中进行初步匹配。BWA 会根据种子长度在索引中查找匹配位置，然后在这些位置附近进行更详细的比对。


# Practice: build a BWA index

To install bwa:
```bash
mamba install -c bioconda bwa
```

### index the selected references:
```bash
cat Refs/ncbi_dataset/data/*/GCF*.fna > Refs/merged_genome.fa
bwa index Refs/merged_genome.fa
```

以下后缀组成的文件共同构成了 BWA 的索引，使得在进行序列比对时能够快速、高效地定位读段在参考基因组中的位置。每个文件都有其特定的功能和用途，它们相互配合，确保 BWA 能够高效地处理大规模的测序数据。

| 后缀   | 含义             | 用途                 |
| ------ | ---------------- | -------------------- |
| `.amb` | 重复序列信息     | 处理模糊匹配         |
| `.ann` | BWT 辅助信息     | 快速定位字符位置     |
| `.bwt` | BWT 转换后的序列 | 快速定位潜在匹配位置 |
| `.pac` | 压缩后的原始序列 | 快速检索序列内容     |
| `.sa`  | 后缀数组         | 精确定位子字符串     |

> 实际上并不需要特别了解这些文件的作用。除非你想开发或优化新的比对算法。

### Do alignment:
```bash
mkdir -p bwa_result
# single end reads
bwa mem Refs/merged_genome.fa data/SRR17173180_1.fastq.gz > bwa_result/SRR17173180_1.bwa.sam

# paired end reads
bwa mem Refs/merged_genome.fa data/SRR22673346_{1,2}.fastq.gz > bwa_result/SRR2267334.bwa.sam
```

### read alignment `sam` file:
```bash
less bwa_result/SRR2267334.bwa.sam
```

SAM（Sequence Alignment/Map）格式文件是一种用于存储序列比对结果的标准文本文件格式。它详细记录了每个读段（read）在参考基因组中的比对位置、比对质量以及其他相关信息。以下是 SAM 文件格式的详细解释：

### SAM 文件结构

SAM 文件由两部分组成：头部信息和比对结果数据行。

### 1. 头部信息

头部信息以 `@` 符号开头，包含对比对结果的元数据描述。常见的头部行包括：

- **`@HD`** ：描述 SAM 文件的版本和排序顺序。
  - **`VN`** ：SAM 文件的版本号。
  - **`SO`** ：排序顺序，如 `unsorted`、`coordinate`（按坐标排序）等。
- **`@SQ`** ：描述参考序列（contig）的信息。
  - **`SN`** ：参考序列的名称。
  - **`LN`** ：参考序列的长度。
- **`@RG`** ：描述测序文库（read group）的信息。
  - **`ID`** ：文库的唯一标识符。
  - **`SM`** ：样本名称。
  - **`PL`** ：测序平台（如 ILLUMINA、PACBIO 等）。
  - **`LB`** ：文库名称。
  - **`PU`** ：测序单元（platform unit）。
  - **`CN`** ：测序中心名称。
- **`@PG`** ：描述比对过程中使用的程序信息。
  - **`ID`** ：程序的唯一标识符。
  - **`PN`** ：程序名称。
  - **`VN`** ：程序版本号。
  - **`CL`** ：调用程序的命令行。
- **`@CO`** ：注释信息，用于添加自定义的注释或说明。

### 2. 比对结果数据行

每行代表一个读段的比对结果，包含多个字段，字段之间用制表符（TAB）分隔。以下是各字段的详细说明：

| 字段索引 | 字段名 | 含义                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| 1        | QNAME  | 读段的唯一标识符（通常是读段的名称或 ID）。                  |
| 2        | FLAG   | 比对标志，一个无符号整数，用于表示比对的各种属性（如是否为第一端、是否未比对等）。 |
| 3        | RNAME  | 读段比对到的参考序列名称（如染色体名称）。如果未比对，则为 `*`。 |
| 4        | POS    | 读段在参考序列中的起始位置（1-based 坐标）。如果未比对，则为 `0`。 |
| 5        | MAPQ   | 比对质量分数，表示该读段比对到当前位置的置信度。范围通常是 0 到 60。 |
| 6        | CIGAR  | CIGAR 字符串，描述读段与参考序列的比对情况（如匹配、插入、删除等）。 |
| 7        | RNEXT  | 下一条读段比对到的参考序列名称。如果未知或未比对，则为 `*`。 |
| 8        | PNEXT  | 下一条读段在参考序列中的起始位置。如果未知或未比对，则为 `0`。 |
| 9        | TLEN   | 模板长度，表示两条配对读段之间的距离（如果适用）。           |
| 10       | SEQ    | 读段的序列本身。如果未比对，则为 `*`。                       |
| 11       | QUAL   | 读段的碱基质量分数，通常使用 FASTQ 格式的质量编码。如果未比对，则为 `*`。 |
| 12+      | TAGS   | 可选字段，包含额外的比对信息（如 NM 标签表示比对中的错配数量）。 |

### FLAG 字段详解

FLAG 字段是一个位掩码（bitwise flag），用于表示比对的各种属性。常见的标志位包括：

| 位（bit）掩码 | 十进制数值 | 含义                                                |
| ------ | --------- | --------------------------------------------------- |
| 0x1    | 0 or    1 | 该读段是配对读段的一部分。                          |
| 0x2    | 0 or    2 | 配对读段已适当比对（properly paired）。             |
| 0x4    | 0 or    4 | 该读段未比对。                                      |
| 0x8    | 0 or    8 | 配对读段的另一条未比对。                            |
| 0x10   | 0 or   16 | 该读段的序列是反向互补的（reverse complemented）。  |
| 0x20   | 0 or   32 | 配对读段的另一条是反向互补的。                      |
| 0x40   | 0 or   64 | 该读段是第一端（first segment in the pair）。       |
| 0x80   | 0 or  128 | 该读段是第二端（second segment in the pair）。      |
| 0x100  | 0 or  256 | 该读段不是主比对结果（not primary alignment）。     |
| 0x200  | 0 or  512 | 该读段是重复比对结果（duplicate）。                 |
| 0x400  | 0 or 1024 | 该读段属于补充比对结果（supplementary alignment）。 |

Check this page to play FLAG: [https://broadinstitute.github.io/picard/explain-flags.html](https://broadinstitute.github.io/picard/explain-flags.html)

### CIGAR 字符串详解

CIGAR（Concise Idiosyncratic Gapped Alignment Report）字符串描述了读段与参考序列的比对情况。每个 CIGAR 字符串由一个或多个操作组成，每个操作包含一个数字和一个字符。常见的操作包括：

| 操作字符 | 含义                                                         |
| -------- | ------------------------------------------------------------ |
| M        | 匹配（Match, 可以是序列匹配或错配）。                               |
| I        | 插入（Insert, 相对于参考序列）。                                     |
| D        | 删除（Delete, 相对于参考序列）。                                     |
| N        | 区域跳过（N-bases, 通常用于基因组中的间隔区域）。                     |
| S        | 软剪切（soft clipping），表示序列的该部分未比对到参考序列，但包含在读段中。 |
| H        | 硬剪切（hard clipping），表示序列的该部分未比对到参考序列，且不包含在读段中。 |
| P        | 填充（padding），用于表示比对中的间隙。                      |
| =        | 序列匹配。                                                   |
| X        | 序列错配。                                                   |

以下是一个 SAM 文件的示例：

```
@HD	VN:1.6	SO:coordinate
@SQ	SN:chr1	LN:248956422
@RG	ID:sample1	SM:sample1	PL:ILLUMINA	LB:lib1	CN:seq_center
@PG	ID:bwa	PN:bwa	VN:0.7.18	CL:bwa mem -t 4 ref.fa reads.fq
SRR123456.1	99	chr1	100	60	100M	=	200	100	AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT	*	NM:i:2	MD:Z:100	AS:i:98	XS:i:95
SRR123456.2	147	chr1	200	60	90M10S	=	100	-100	TGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC	*	NM:i:1	MD:Z:90	AS:i:90	XS:i:88
```

解释：

- **头部信息** ：
  - `@HD` 行表示 SAM 文件的版本为 1.6，并且比对结果按坐标排序。
  - `@SQ` 行描述了参考序列 `chr1` 的长度为 248,956,422。
  - `@RG` 行提供了测序文库的信息，包括文库 ID、样本名称、测序平台等。
  - `@PG` 行记录了比对程序的信息，如程序名称、版本和命令行参数。
- **比对结果数据行** ：
  - 第一条数据行表示读段 `SRR123456.1` 比对到 `chr1` 的位置 100，比对质量为 60，CIGAR 字符串为 `100M`（表示 100 个碱基完全匹配），并且该读段是配对读段的第一端（FLAG 为 99）。
  - 第二条数据行表示读段 `SRR123456.2` 比对到 `chr1` 的位置 200，比对质量为 60，CIGAR 字符串为 `90M10S`（表示 90 个碱基匹配，10 个碱基被软剪切），并且该读段是配对读段的第二端（FLAG 为 147）。


### Stat

aligned reads
```bash
grep -v '^@' bwa_result/SRR2267334.bwa.sam | awk '{arr[$3]++} END {for (ref in arr) {print ref, arr[ref]}}'
```

total alignments:
```bash
grep -v '^@' bwa_result/SRR2267334.bwa.sam | cut -f1 | uniq | wc -l
```

total sequences:
```
zcat data/SRR22673346_{1,2}.fastq.gz|wc -l
```

calculate alignment rate:
```bash
perl -e '$a=520/(4160/4/2);print $a'
```



# FAQ: How to prepare reference databse

Shigella flexneri 2a str. 301: [GCF_000006925.2](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000006925.2/)  

Shigella flexneri 2a: [GCF_002950215.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_002950215.1/)  

Shigella flexneri: [GCF_022354705.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_022354705.1/)

Escherichia coli str. K-12 substr. MG1655: [GCF_000005845.2](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/)  

Escherichia albertii: [GCF_028622335.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_028622335.1/)



```bash
datasets download genome accession GCF_000006925.2 GCF_002950215.1 GCF_022354705.1 GCF_000005845.2 GCF_028622335.1 \
  --include gff3,rna,cds,protein,genome,seq-report --dehydrated
unzip ncbi_dataset.zip
datasets rehydrate --directory .
```