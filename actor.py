import pgzero
import pgzrun
from pgzero.actor import Actor
import self as plane



road = Actor('road')
road.x = 1000
road.y = 620
bg = Actor('bg',pos=[480,360])
start = Actor('start')
start.x = 260
start.y = 460
logo = Actor('self')
logo2 = Actor('road')
cloudy = Actor('c')
shili = Actor('l1')
plane_list = [Actor('l1')]
shili.x = 200
shili.y = 200
cloudy.y = 200
admin = Actor('admin')
xuan_list = [Actor('上海至纽约.png',pos=[200,200]),Actor('上海至巴黎.png',pos=[200,600]),Actor('上海至悉尼.png',pos=[600,600]),Actor('上海至莫斯科.png',pos=(600,200))]
admin.x = 750
admin.y = 350
logo2.x = 1000
logo2.y = 620
sets = Actor('setting',pos=[900,50])
wind = Actor('winds',pos=[800,500])
logo.x = 500
logo.y = 600
sea = Actor('sea')
sea.x = 480
sea.y = 1500
self = Actor('self')
self.x=500
self.y = 500
Actor_list = [bg,logo2,start]
running_list = [bg,road,self]
#setting_list = []
def paint_start():
    global Actor_list
    for _ in Actor_list:
        _.draw()
def paint_running():
    global running_list
    for _ in running_list:
        _.draw()
#def paint_setting():
