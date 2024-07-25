# my_history
## v0.1.0 Basic
### Usage
```bash
$ cnt <string>
```
### example
```bash
$ cnt aws
$ cnt ls
$ cnt cd
```
![image](https://github.com/user-attachments/assets/62a9989c-a0cf-4770-8992-df9711f3def4)

## v0.2.0 Use python argparse

### requirements
```bash
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```

### Usage
```bash
$ my-history -c <cmd>
$ my-history -t <line>
$ my-history -d <date>
```
### example
```bash
$ my-history -c ls
$ my-history -t 10 -d 2024-07-17
```
![image](https://github.com/user-attachments/assets/f3f50f3f-6758-49e9-9a36-7b9a9b40856b)
