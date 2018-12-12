# -*- coding:utf-8 -*-
import os
print('       ******  MySQL Demo  ******     ')
print('                         ——open source')
print()
print('>>正在安装依赖库，请稍后......')
print()
os.system('python -m pip install --upgrade pip ')
file = open('requirements.txt')
models = file.read().split()
for model in models:
    os.system('pip install {}'.format(model))
file.close()
print()
input('>>安装完毕，按任意键启动。')
os.system('start MysqlDemo.py')
exit()
