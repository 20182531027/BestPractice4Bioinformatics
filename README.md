# BestPractice4Bioinformatics
Learn bioinformatics from 'ZERO' background

# 课程设置

0. 了解版本控制
1. 感受生物信息学分析的过程
2. 认识数据（表格）
3. 认识数据（大数据）
4. 如何使用工具
5. 设计实验方案与分析流程

# 课程文档与作业

CH.0: [Experience your first git operation!](#guideline)  
CH.1: [Markdown everything!](./docs/markdown.md)  
CH.2: [(Very) basic statistics](./docs/basicStatistics.md)  
CH.3: [Login to a Linux OS](./docs/LinuxHome.md)  
CH.4: [Data version control](./docs/dvc.md)  
CH.5: [Quality control for sequence data](./biociao/checkSeqData.md)  
CH.6: [Squence Alignment/Mapping and data manipulation](./docs/mapping.md)  

BOX.01: [AI powered IDE](./docs/IDE.md)
BOX.02: [Knowledge Management](./docs/Knowledge_Management.md)

# 准备工作（即作业Ex.0）
使用 `github.com`平台，参与`BestPractice4Bioinformatics`培训项目并完成首次提交。


## Guideline

### STEP 1. Fork the [`BGIGPD/BestPractice4Bioinformatics`](https://github.com/BGIGPD/BestPractice4Bioinformatics) project

由于新加入的同学并非都是该项目成员，所以需要先讲仓库复制到自己的账户下，然后才能方便地进行后续操作。  
在项目右上角选择"Fork", 

![Fork button](<assets/forkButton.png>)  

然后选择自己的账户（或新建group），

![Create your own group](<assets/CreateNewFork.png>)

点击`CreateFork`,完成Fork操作。

![Forking](<assets/Forking.png>)

等待完成。

Fork完成后，页面将会跳转到你自己的仓库页面。我们对该仓库拥有完全的读写权限。

### STEP 2. Clone the <yourname>/BestPractice4Bioinformatics project
> <yourname> 是你自己账户名称。
> 切记头尾的尖括号`<>`也要去掉。

接下来需要在自己电脑上操作。对于于Windows用户，请安装[git bash]()。

![clone](<assets/cloneButton.png>)


在本地计算机上打开终端（如git bash），输入以下命令(记得使用刚才复制的地址，替换 git clone 后面的部分)  
> :warning: 要将`<yourname>`连同前后尖括号一起改为你自己的用户名
```bash
cd ~ # ‘～’ 表示当前用户的家目录，也可以选择其他你想要放置仓库的目录
git clone git@github.com:biociao/BestPractice4Bioinformatics.git
cd BestPractice4Bioinformatics
git checkout train2025
git checkout -b YourName # Create a new branch of your name from train2025
```

如果是第一次使用git，需要告诉git系统你的信息
```bash
# For the first time using git, you may need configure your author information.
git config --add user.name YourName # Init add your name 
git config --add user.email Your email # Init add your email 
```

### STEP 2. Init your task
```
mkdir YourName
cd YourName
vi README.md
```
Open `README.md`. 

Add a h1-title of "About this project". Write something about your work then save it.

### STEP 3. Recording Changes to the Repository

```
git status
git add README.md
git status
git commit -m 'My work begin' README.md
```
### STEP 4. Sync with your remote branch 
```
git push origin YourName
```
### STEP FINAL. Merge your work to the course branch

在网页上找到发起合并请求的按钮  
选择branch从当前改动的分支（YourName）合并到教学仓库的`train2025`分支。  
发起请求后即可等待老师审核。

Complete...
======================================
Good job! Cheers! :champagne\_glass: 

Or not...
======================================
Ask Deepseek or check following FAQ :)


# FAQ
### Q: 终端是什么？我该怎么操作？  
A: 跟着视频操作【[Extra01-认识终端-哔哩哔哩](https://b23.tv/38AhlTG)】 

### Q: 我在操作git的过程中总是遇到各种各样的问题。  
A：跟着视频操作【[Extra02-git实操-哔哩哔哩](https://b23.tv/Nqi6l8W)】

### Q：怎么Fork？  
A：跟着视频操作【[Extra03-Fork-哔哩哔哩](https://b23.tv/2A788xG)】

### Q：我已经clone了教学仓库，在发现`git push`权限问题后该怎么办？  
A：可以不用重复clone，直接替换origin地址即可。步骤如下：  
1 Fork教学仓库。  
2 获取Frok后的仓库clone地址。  
3 按如下命令变更origin地址：  
```bash
git remote set-url origin https://github.com/<YourName>/BestPractice4Bioinformatics.git
```
4 确认新地址是否修改成功
```bash
git remote show origin
```
5 推送代码
```bash
git push origin YourName
```

### Q: Occasionally unable to access github.com  

The cause is complex and involves a mix of various factors. To avoid this issue, I provided multiple distributed repository access points. When encountering difficulties in accessing github.com smoothly, you may consider using the following [gitee.com](https://gitee.com/bgigpd/BestPractice4Bioinformatics) mirror repository (no login is required if you only need to pull the latest code).  

```bash
git remote add gitee https://gitee.com/bgigpd/BestPractice4Bioinformatics.git
git pull gitee train2025
```

### Q: conda/mamba install failed

The reasons are mainly due to OOM(out-of-memory) or network unaccessiable.  

#### Solution 1  
Try use anaconda mirror like [tuna](https://mirrors.tuna.tsinghua.edu.cn) or [NJU](https://mirror.nju.edu.cn).

#### Solution 2  
Tyr not use vscode and `mamba install` in the same time, as vscode requires a lot of memory.

#### Solution 3  
Skip this step and directly use my profile. By `source` following configuration you will be using my installed mamba and obtained the tools we need during this course.

```bash
source /home/student/biociao/init_mamba.rc
```
