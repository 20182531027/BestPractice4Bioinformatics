# Login A Linux OS and 'decorate' your Home

## Requirement / tools

For windows user, you can use [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) or [MobaXterm](https://mobaxterm .mobatek.net/).

For Mac user, you can use [iTerm2](https://iterm2.com/) or just use the default terminal.

## Login

### Login with SSH

```bash
ssh student@train2025.biochao.cc
```
## Where am I?
![alt text](assets/whereami.png)

## Know the Linux file system

```bash
$ tree -L 1 /
/
├── bin -> usr/bin
├── bin.usr-is-merged
├── boot
├── cdrom
├── CloudrResetPwdAgent
├── dev
├── etc
├── home
├── lib -> usr/lib
├── lib64 -> usr/lib64
├── lib.usr-is-merged
├── lost+found
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin -> usr/sbin
├── sbin.usr-is-merged
├── snap
├── srv
├── sys
├── tmp
├── usr
└── var
```

> 目之所及，皆为文件

![alt text](assets/FileTree.png)

### File types

#### Regular file

普通文件是存储数据或文本的文件，是最常见的文件类型。它们可以包含任何类型的数据，如文本文件、图片、音频文件、视频文件等。

## 'Decorate' your Home 

### Install zsh

```bash
sudo apt-get install zsh
```
#### Directory

目录是一种特殊的文件，用于组织和存储其他文件和目录。目录是文件系统中的树形结构的基础。

#### Link  

链接是一种特殊的文件，用于指向另一个文件或目录。链接分为两种类型：硬链接（Hard Link）和软链接（Symbolic Link 或 Soft Link）。

### Device File  

设备文件用于表示系统中的硬件设备。

### Pipe File / FIFO
管道文件是一种特殊的文件，用于进程间通信。它允许一个进程将数据写入管道，而另一个进程从管道中读取数据。

#### Socket File  

套接字文件用于网络通信或进程间通信。它允许不同进程之间通过网络协议进行通信。

### File permission

![alt text](assets/FilePermission.png)

符号表示法使用字符来表示权限：
- 读权限（r）：用字符 r 表示    (4 or 100)。
- 写权限（w）：用字符 w 表示    (2 or 010)。
- 执行权限（x）：用字符 x 表示  (1 or 001)。
- 无权限（-）：用字符 - 表示。

### Environment Variable

```bash
$ env
SHELL=/bin/bash
HISTSIZE=1000
HISTTIMEFORMAT=%F %T student
PWD=/home/student
LOGNAME=student
XDG_SESSION_TYPE=tty
HOME=/home/student
LANG=en_US.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.crdownload=00;90:*.dpkg-dist=00;90:*.dpkg-new=00;90:*.dpkg-old=00;90:*.dpkg-tmp=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:*.swp=00;90:*.tmp=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:
LC_TERMINAL=iTerm2
SSH_CONNECTION=111.199.109.170 1966 172.31.0.122 22
LESSCLOSE=/usr/bin/lesspipe %s %s
XDG_SESSION_CLASS=user
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=student
LC_TERMINAL_VERSION=3.5.11
SHLVL=1
XDG_SESSION_ID=20
XDG_RUNTIME_DIR=/run/user/1000
SSH_CLIENT=111.199.109.170 1966 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/home/student/bin:/home/student/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
SSH_TTY=/dev/pts/0
_=/usr/bin/env
```

### Install mamba

```bash
bash ../biociao/Miniforge3-Linux-x86_64.sh
```

# Homework

Create your own HOME directory.

Replace `biociao` with your own name.

Create a directory in your name.
```bash
mkdir biociao
```

Enter this directory.
```bash
cd biociao
```

Create a bash profile
```bash
echo "export HOME=/home/student/biociao"  >> .bashrc
```

Source your bash profile. This will change your HOME directory.
```bash
source .bashrc
```

## Install mamba

```bash
bash ../biociao/Miniforge3-Linux-x86_64.sh
```
