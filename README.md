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
