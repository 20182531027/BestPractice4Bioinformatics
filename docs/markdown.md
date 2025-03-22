# 科研文档规范与可重复性实践

## Rapid Introduction

### 什么是Markdown？  

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

数学公式：
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

数学公式：
$$F(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi i \xi x} \,d\xi$$

显示效果演示结束。

### 应用生态
- **编辑器支持度高**：VSCode/RStudio/Obsidian/Typora
- **学术增强工具**：
  - Zotero联动（MDnotes插件）
  - Draw.io图表整合
  - Mermaid流程图语法

### Rmarkdown又是什么？

RMarkdown是可重复性科研的革命性工具（会不会有点夸张），基于 Markdown 语法扩展而来，由 RStudio 团队开发。它将数据分析、可视化与学术写作深度融合，允许用户在纯文本文档中直接嵌入 R/Python 等编程语言的动态代码块，并自动将代码执行结果（图表、统计表格、模型参数）实时渲染到最终报告中。这种“代码即文档”的特性，彻底解决了传统研究中数据-分析-结论链条断裂的问题，确保每一次结果更新都能同步反映在文档中，是生信领域实现可重复研究的基石。

作为增强版 Markdown，RMarkdown 支持通过 YAML 元数据自定义输出格式（HTML/PDF/Word/幻灯片），并完美兼容 LaTeX 数学公式与学术引用系统（如 BibTeX）。其参数化报告功能尤为强大：通过定义模板中的变量，可一键生成数百份参数不同的分析报告（如多组学数据的批量处理），大幅提升高通量数据分析效率。例如，在 RNA-seq 分析中，研究者只需维护一个 Rmd 主文件，即可自动生成包含差异表达基因、富集分析和火山图的可交互式 HTML 报告。

与 Git 版本控制的深度整合，更让 RMarkdown 成为团队协作的利器。所有分析步骤和文档修改均以纯文本形式留存历史记录，配合 knitr 引擎的缓存机制，能智能跳过未修改代码的重运行，显著节省计算资源。从实验室笔记本到期刊论文，RMarkdown 以优雅的代码驱动范式，重新定义了科研写作——让数据分析者告别“截图粘贴”的手工时代，真正专注于科学逻辑的构建与传播。

## Problem & solving

1. 在自己目录下的`README.md`中记录本节课的学习过程，在此过程中尽可能地运用markdown的各种格式标记语法。

2. 将以下代码重新整理成Rmarkdown的格式，并在Rstudio中执行，并描述、记录结果。

需要在Rstudio中新建R markdown文件，然后依次执行（并尝试理解）以下代码：  

2.0 载入需要的包
```markdown
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
if (!require("tidyverse")) install.packages("tidyverse")
if (!require("airway")) BiocManager::install("airway")
library(tidyverse)
library(airway)
library(DT)
```

2.1 获取公共RNA-seq数据
```{r get_data}
data(airway)  # 加载经典RNA-seq数据集
count_matrix <- assay(airway)[, 1:4]  # 提取前4个样本的表达矩阵
metadata <- colData(airway)[1:4, ] %>% 
  as.data.frame() %>%
  select(dex, albut, Run)  # 精简元数据

# 创建交互式数据表
DT::datatable(
  head(count_matrix, 5),
  caption = "RNA-seq原始计数矩阵（前5行）"
)
```

2.2 数据探索与转换
```{r data_processing}
# 标准化处理（CPM转换）
cpm_matrix <- edgeR::cpm(count_matrix) %>% 
  as.data.frame() %>%
  rownames_to_column("GeneID")

# 长格式转换（适合ggplot绘图）
tidy_data <- cpm_matrix %>%
  pivot_longer(
    cols = -GeneID,
    names_to = "Sample",
    values_to = "Expression"
  ) %>%
  left_join(rownames_to_column(metadata, "Sample"), by = "Sample")

# 统计摘要表格
stats_summary <- tidy_data %>%
  group_by(dex) %>%
  summarise(
    Mean = mean(Expression),
    SD = sd(Expression),
    Median = median(Expression)
  )
knitr::kable(stats_summary, caption = "处理组与对照组表达量统计")
```

2.3 数据可视化
```{r visualization}
# 基因表达分布箱线图
ggplot(tidy_data, aes(x = dex, y = log2(Expression + 1)), fill = dex) +
  geom_boxplot(alpha = 0.7, outlier.shape = NA) +
  geom_jitter(width = 0.2, alpha = 0.3, size = 1.5) +
  labs(
    title = "处理组 vs 对照组基因表达分布",
    x = "地塞米松处理",
    y = "log2(CPM + 1)"
  ) +
  theme_minimal(base_size = 14) +
  scale_fill_brewer(palette = "Set2")

# 表达量密度曲线
ggplot(tidy_data, aes(x = log2(Expression + 1), color = dex)) +
  geom_density(linewidth = 1.2) +
  facet_wrap(~albut, ncol = 2) +
  labs(
    title = "不同治疗方案下的表达量分布",
    x = "log2(CPM + 1)",
    color = "处理组"
  ) +
  theme_bw()
```

2.4 进阶分析
```{r advanced}
if (FALSE) {  # 实际运行时移除if条件
  library(DESeq2)
  dds <- DESeqDataSetFromMatrix(
    countData = count_matrix,
    colData = metadata,
    design = ~ dex
  )
  dds <- DESeq(dds)
  res <- results(dds)
}
```

展示Foldchange 与 p值分布：
```{r fold_change_pvalue}
ggplot(res,aes(x=log2FoldChange,y=pvalue)) + 
  geom_point(alpha=.1) +
  geom_density2d()
```

# 交作业
记得将学习的Rmarkdown（.Rmd)文档通过git推送本站点，然后发起MR到教学仓库中。