import pgzrun
import random
import time



random_weather = 1
try:
    m = open('money.txt','r')
    l = open('level.txt','r')
    c = open('count.txt','r')
    g = open('good.txt','r')
except FileNotFoundError:
    m = open('money.txt','w').write('0')
    l = open('level.txt','w').write('1')
    c = open('count.txt','w').write('0')
    g = open('good.txt','w').write('100')
import actor
height = 0
speed = 0
power = 0
xin_dict = {'上海至纽约':14000,'上海至莫斯科':7000,'上海至巴黎':9300,'上海至悉尼':8000}
#pla_dict = {'L1':'L1'}
pla_dict = {'l1':'self'}
now_level = open('level.txt','r').read()
max_speed = 700
max_power = 5
jian_cn_dict = {'l1':f'最大速度:{max_speed}km/h\n最大动力:{max_power}','l2':'最大速度:2000km/h\n最大动力:10','自定义':"最大速度:2000km/h\n最大动力：209"}
state = 'start'
stage = '起飞'
way = 1000
now_time = 0
last_time = 0
bu = False
away = 1000
cnt = int(open('count.txt','r').read())
money = int(open('money.txt','r').read())
j_cnt = int(now_level)*5
j_money = int(now_level)*100000
age_score = int(open('good.txt','r').read())