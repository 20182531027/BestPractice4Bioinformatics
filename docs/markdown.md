# 数据清洗 + 科研文档规范与可重复性实践

## Content

[认识 Markdown](#什么是Markdown)  
[认识 R-markdown](#Rmarkdown又是什么)  
[了解数据清洗](#利用Rmarkdown开展数据清洗工作)  

## 什么是Markdown  

Markdown 是一种轻量级标记语言，由 John Gruber 于 2004 年创建，旨在以纯文本形式实现内容与格式的优雅结合。它通过简单的符号（如 #、*、-）即可快速定义标题、列表、代码块等元素，兼顾人类可读性与机器可解析性，避免了传统文本处理工具（如 Word）的复杂格式操作。其核心优势在于能将笔记、文档甚至学术论文转化为结构清晰的文本文件，完美兼容版本控制系统（如 Git），让科研协作中的修改追踪和冲突解决变得透明高效。

在生物信息学领域，Markdown 已成为记录实验流程、撰写分析报告的首选工具。它支持直接嵌入代码、数学公式（通过 LaTeX 语法）和图表，结合 Rmarkdown 等扩展工具时，更能动态生成包含统计结果的可视化报告，实现数据分析与文档撰写的无缝衔接。例如，科研人员可在 Markdown 中混合 R/Python 代码块，一键生成包含图表、统计检验结果和结论的 HTML/PDF 文档，极大提升了研究的可重复性。

从日常学习到科研实践，Markdown 的跨平台特性（可用任何文本编辑器编写）和丰富的生态工具（如 Typora、Obsidian、Jupyter Notebook）使其成为知识管理的基石。无论是整理课程笔记、协作撰写论文，还是构建项目文档库，Markdown 都以“内容优先”的设计哲学，帮助研究者专注于核心思想表达，而非格式调整——这正是科研高效协作与知识传承的关键所在。

### 为什么选择Markdown？
- **生信领域的适配性**：
  - 代码/文本/数学公式的完美融合
  - 版本控制友好（diff清晰）
  - 跨平台渲染一致性
- **与传统文档工具对比**：
  - vs Word：纯文本冲突解决/版本追踪优势
  - vs LaTeX：学习曲线与实用性的平衡

### 核心语法元素
```markdown
# 多级标题
**加粗**与*斜体*的科学表述规范  
- 项目符号列表
  - 嵌套列表管理实验步骤

> 文献引用区块的标准格式

`单行代码`与```代码块```的嵌入技巧
![ALT-TEXT](path/to/image.png) 图表标注规范

[超链接](https://example.com) 文献引用方式

表格创建：
| 样本ID | 表达量 | p-value |
|--------|--------|---------|
| A001   | 3.14   | 0.001   |

数学公式（Latex语法）：
$$F(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi i \xi x} \,d\xi$$
```

显示效果如下：

# 多级标题
**加粗**与*斜体*的科学表述规范  
- 项目符号列表
  - 嵌套列表管理实验步骤

> 文献引用区块的标准格式  


`单行代码`与```代码块```的嵌入技巧
![ALT-TEXT](path/to/image.png) 图表标注规范

[超链接](https://example.com) 文献引用方式

表格创建：
| 样本ID | 表达量 | p-value |
|--------|--------|---------|
| A001   | 3.14   | 0.001   |

数学公式（Latex语法）：
$$F(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi i \xi x} \,d\xi$$

显示效果演示结束。

### 应用生态
- **编辑器支持度高**：VSCode/RStudio/Obsidian/Typora
- **学术增强工具**：
  - Zotero联动（MDnotes插件）
  - Draw.io图表整合
  - Mermaid流程图语法

### Rmarkdown又是什么

RMarkdown是可重复性科研的有效工具，基于 Markdown 语法扩展而来，由 RStudio 团队开发。它将数据分析、可视化与学术写作深度融合，允许用户在纯文本文档中直接嵌入 R/Python 等编程语言的动态代码块，并自动将代码执行结果（图表、统计表格、模型参数）实时渲染到最终报告中。这种“代码即文档”的特性，彻底解决了传统研究中数据-分析-结论链条断裂的问题，确保每一次结果更新都能同步反映在文档中，是生信领域实现可重复研究的基石。

作为增强版 Markdown，RMarkdown 支持通过 YAML 元数据自定义输出格式（HTML/PDF/Word/幻灯片），并完美兼容 LaTeX 数学公式与学术引用系统（如 BibTeX）。其参数化报告功能尤为强大：通过定义模板中的变量，可一键生成数百份参数不同的分析报告（如多组学数据的批量处理），大幅提升高通量数据分析效率。例如，在 RNA-seq 分析中，研究者只需维护一个 Rmd 主文件，即可自动生成包含差异表达基因、富集分析和火山图的可交互式 HTML 报告。

与 Git 版本控制的深度整合，更让 RMarkdown 成为团队协作的利器。所有分析步骤和文档修改均以纯文本形式留存历史记录，配合 knitr 引擎的缓存机制，能智能跳过未修改代码的重运行，显著节省计算资源。从实验室笔记本到期刊论文，RMarkdown 以优雅的代码驱动范式，重新定义了科研写作——让数据分析者告别“截图粘贴”的手工时代，真正专注于科学逻辑的构建与传播。

## 利用Rmarkdown开展数据清洗工作  

### 为什么需要元数据清洗？

数据质量是数据分析的基石，未经清洗的元数据可能导致：

- 统计分析的显著偏差（如异常值扭曲均值）
- 机器学习模型性能下降（错误标注误导特征学习）
- 可视化结果失真（类型错误导致绘图失败）
- 研究结论不可靠（输入错误引发连锁错误）


## 数据清洗原则  

- 上策：让代码处理表格
- 中策：批量化处理表格
- 下策：手动处理表格

## 特别注意

- 临床数据要脱敏
- 样本对应关系要再三确认
- 尽可能地交叉验证

## 核心清洗要点及R代码实现

### 1. 异常值检测与处理

**检测方法：**

```r
# 数值型变量快速概览
summary(metadata$measurement)

# 箱线图可视化
boxplot(metadata$measurement, main = "Measurement Distribution")

# 标准差法识别异常
mean_val <- mean(metadata$measurement, na.rm = TRUE)
sd_val <- sd(metadata$measurement, na.rm = TRUE)
outliers <- which(metadata$measurement > mean_val + 3*sd_val | 
                 metadata$measurement < mean_val - 3*sd_val)
```

**处理策略：**

```r
# 替换为NA
metadata$measurement[outliers] <- NA

# 或使用分位数截断
qnt <- quantile(metadata$measurement, probs=c(.25, .75), na.rm = TRUE)
caps <- quantile(metadata$measurement, probs=c(.05, .95), na.rm = TRUE)
metadata$measurement[metadata$measurement < qnt[1]] <- caps[1]
metadata$measurement[metadata$measurement > qnt[2]] <- caps[2]
```

### 2. 错误标注纠正

**检测方法：**

```r
# 正则表达式匹配异常值
library(stringr)
str_subset(metadata$category, "[^A-Za-z]")
```

**处理策略：**

```r
# 统一标签格式
metadata <- metadata %>%
  mutate(category = case_when(
    str_detect(category, "(?i)^control$") ~ "Control",
    str_detect(category, "(?i)^experiment") ~ "Experimental",
    TRUE ~ as.character(category)
  ))
```

### 3. 变量类型修正

**检测方法：**

```r
# 查看数据结构
str(metadata)

# 类型验证
library(purrr)
map_chr(metadata, class)
```

**处理策略：**

```r
# 类型转换
metadata <- metadata %>%
  mutate(
    sample_id = as.character(sample_id),
    collection_date = as.Date(collection_date, format = "%Y-%m-%d"),
    temperature = as.numeric(temperature)
  )
```

### 4. 输入错误修正

**检测方法：**

```r
# 文本型字段模式识别
metadata %>%
  filter(str_detect(patient_id, "[^0-9A-Z]"))

# 日期格式验证
library(lubridate)
sum(is.na(parse_date_time(metadata$timestamp, orders = c("ymd HMS", "dmy HMS"))))
```

**处理策略：**

```r
# 正则表达式清洗
metadata <- metadata %>%
  mutate(
    patient_id = str_replace_all(patient_id, "[^0-9A-Z]", ""),
    timestamp = coalesce(ymd_hms(timestamp), dmy_hms(timestamp))
  )
```

## 高效清洗工具推荐

1. **数据验证神器**：`validate`包创建自定义规则集
2. **自动化清洗**：`dplyr` + `tidyr`组合操作
3. **缺失值处理**：`mice`包多重插补法
4. **流程记录**：RMarkdown实现可复现清洗文档

## 最佳实践建议

- 建立数据质量日志（Data Quality Log）
- 实施版本控制（Git集成）
- 制作自动化检查模板
- 重要修改前创建数据备份副本

通过系统化的数据清洗流程，可使元数据质量显著提升，为后续分析提供可靠保障。

# 作业  

将`/biociao/origin.metadata.xlsx`复制到自己目录，尝试对该表格进行清洗检查，保存最终的高质量表格。

步骤摘要：  

> 1. Website： Update/Sync Fork
> 2. Local-git bash:    git pull
> 3. copy xlsx
> 4. check xlsx
> 5. clean xlsx

## Problem & solving

1. 在自己目录下的`README.md`中记录本节课的学习过程，在此过程中尽可能地运用markdown的各种格式标记语法。

2. 将以下代码重新整理成Rmarkdown的格式，并在Rstudio中执行，并描述、记录结果。