# my_history
- parquet 파일의 정보를 cli 기반으로 조회
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

### Dev env setting
```bash
$ git clone <URL>
$ cd <PJT_NAME>
$ pyenv virtualenv 3.11.9 clean 
$ pyenv global clean 
$ rm -rf .venv
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pdm list
$ pytest

# option
$ pdm add -dG test pytest pytest-cov
```

### deploy
```bash
# dev branch
$ pip install git+https://github.com/j25ng/my_history.git@0.2.0/args

# main
$ pip install git+https://github.com/j25ng/my_history.git
```

### ref
```bash
- https://pdm-project.org/en/latest/usage/dependency/#add-development-only-dependencies
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

## v0.2.1 Use tabulate
### Usage
```bash
$ pip install tabulate
$ my-history -t <line> -d <date> -p
```
### example
```bash
$ my-history -t 3 -d 2024-07-17 -p
```
![image](https://github.com/user-attachments/assets/1a176b15-189b-48d1-ba88-0336a8db2e3b)

