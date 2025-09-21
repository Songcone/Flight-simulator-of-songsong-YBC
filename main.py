import pgzero
import pgzrun
import math


try:
    m = open('money.txt','r')
    l = open('level.txt','r')
    c = open('count.txt','r')
    g = open('good.txt','r')
    m.close()
    l.close()
    c.close()
    g.close()
except:
    m = open('money.txt','w')
    l = open('level.txt','w')
    c = open('count.txt','w')
    g = open('good.txt','w')
    m.write('0')
    l.write('1')
    c.write('0')
    g.write('100')
    m.close()
    l.close()
    c.close()
    g.close()
def save():
    m = open('money.txt','w')
    l = open('level.txt','w')
    c = open('count.txt','w')
    g = open('good.txt','w')
    m.write(str(self.money))
    l.write(self.now_level)
    c.write(str(self.cnt))
    g.write(str(self.age_score))
    m.close()
    l.close()
    c.close()
    g.close()
if True:
    import actor
    import self
    import logic
    import center
    import hub 
    from pgzero.actor import Actor
    from pygame import time
    import time
    import random
    mouse_down = False
    TITLE = '航班模拟器'
    WIDTH = 960
    HEIGHT = 720
    sounds.bgm.play(-1)
    m = Actor('angle')
    def output():
        if self.random_weather > 4:
            screen.draw.text('速度:'+str(self.speed)+'km\h',center = [750,150],fontsize = 30,fontname = 'simsum.ttf',color = "#2FFF00DB")
            screen.draw.text('动力:'+str(round(self.power,0)),center = [750,85],fontsize = 30,fontname = 'simsum.ttf',color = "#81FAE0CF")
            screen.draw.text('角度:'+str(actor.self.angle),center = [750,120],fontsize = 30,fontname = 'simsum.ttf',color = "#C9FC69BA")
            screen.draw.text('高度:'+str(round(self.height,0))+'m',center = [750,50],fontsize = 30,fontname = 'simsum.ttf',color = "#DBFA5FDF")
            screen.draw.text('→',center = [920,120],fontsize = 50,fontname = 'simsum.ttf',color = 'white',angle = actor.self.angle)
        else:
            screen.draw.text('速度:'+str(self.speed)+'km\h',center = [750,150],fontsize = 30,fontname = 'simsum.ttf',color = "#FF8800")
            screen.draw.text('动力:'+str(round(self.power,0)),center = [750,85],fontsize = 30,fontname = 'simsum.ttf',color = "#FA8801")
            screen.draw.text('角度:'+str(actor.self.angle),center = [750,120],fontsize = 30,fontname = 'simsum.ttf',color = "#FF8800")
            screen.draw.text('高度:'+str(round(self.height,0))+'m',center = [750,50],fontsize = 30,fontname = 'simsum.ttf',color = "#FA8800")
            screen.draw.text('→',center = [920,120],fontsize = 50,fontname = 'simsum.ttf',color = 'red',angle = actor.self.angle)
            screen.draw.text('警告！警告！遇到恶劣天气，请谨慎驾驶！',center = [480,80],fontsize = 30,fontname = 'simsum.ttf',color = "#F2FA07FF")
    def update():
        hub.a+=1
        if self.state == 'start':
            actor.paint_start()
            actor.shili.draw()
            actor.admin.draw()
            screen.draw.text(self.jian_cn_dict['l'+self.now_level],center = [200,300],fontsize = 30,fontname = 'microsoft.ttf',color = 'yellow')
            screen.draw.text('航班模拟器',center = [750,150],fontsize = 70,fontname = 'simsum.ttf',color = 'red')
            screen.draw.text('您启动游戏时的飞机型号:',center = [200,100],fontsize = 30,fontname = 'chinese.ttf',color = 'green')
            screen.draw.text('Flight simulator',center = [750,230],fontsize = 40,fontname = 'english.ttf',color = 'yellow')
            actor.sets.draw()
            screen.draw.text('@松松原创作品',center = [750,400],fontsize = 20,fontname = 'simsum.ttf',color = 'black')
            if hub.actor_collide(actor.start,m) and mouse_down or keyboard.space:
                self.height = 0
                self.speed = 0
                self.power = 0
                self.stage = '开始'
                actor.sea.y = 1500
                self.state = 'xuanze'
            if hub.actor_collide(actor.sets,m) and mouse_down:
                self.state = 'settings'
            if hub.actor_collide(actor.admin,m) and mouse_down:
                self.state = 'plane'
        if self.state == 'xuanze':
                actor.bg.draw()
                screen.draw.text('请选择您的航班',center = [480,100],fontname = 'microsoft.ttf',fontsize = 30,color = "#49FFE1")
                for i in actor.xuan_list:
                    i.draw()
                if hub.actor_collide(actor.xuan_list[0],m) and mouse_down:
                    self.away = 14000
                    self.way = 14000
                    self.state = 'running'
                if hub.actor_collide(actor.xuan_list[1],m) and mouse_down:
                    self.away = 9000
                    self.way = 9000
                    self.state = 'running'
                if hub.actor_collide(actor.xuan_list[2],m) and mouse_down:
                    self.away = 8000
                    self.way = 8000
                    self.state = 'running'
                if hub.actor_collide(actor.xuan_list[3],m) and mouse_down:
                    self.away = 7000
                    self.way = 7000
                    self.state = 'running'
                ret = Actor('return',pos=[50,50])
                ret.draw()
                if hub.actor_collide(ret,m) and mouse_down:
                    self.state = 'start'
        if self.state == 'settings':
            actor.bg.draw()
            actor.bg.draw()
            hub.setting.aadd.draw()
            hub.setting.afbs.draw()
            screen.draw.text('帧率开关:',center = [200,100],fontname = 'chinese',fontsize = 30,color = 'green')
            screen.draw.text('显示数据:',center = [200,200],fontname = 'chinese',fontsize = 30,color = 'green')
            screen.draw.text('游戏通用设置',center = [480,50],fontsize = 50,fontname = 'simsum.ttf',color = "#000000")
            screen.draw.text('您的游戏数据',center = [480,300],fontsize = 50,fontname = 'simsum.ttf',color = "#000000")
            screen.draw.text('金币money:'+str(self.money),center = [300,400],fontsize = 50,fontname = 'simsum.ttf',color = "#E2A31B")
            screen.draw.text('等级:LeveL '+self.now_level,center = [750,400],fontsize = 50,fontname = 'simsum.ttf',color = "#7B1BE2")
            screen.draw.text('满意度:'+str(self.age_score),center = [300,550],fontsize = 50,fontname = 'simsum.ttf',color = "#6BE21B")
            screen.draw.text('次数:'+str(self.cnt),center = [750,550],fontsize = 50,fontname = 'simsum.ttf',color = "#E2391B")
            screen.draw.text(hub.check_level(),center = [480,680],fontsize = 30,fontname = 'chinese.ttf',color = "#FFFFFF")
            ret = Actor('return',pos=[50,50])
            ret.draw()
            if hub.actor_collide(ret,m) and mouse_down:
                self.state = 'start'
        if self.state == 'plane':
            actor.road.y = 1000
            actor.bg.draw()
            a = Actor('l1',pos=[500,300])
            a.draw()
            screen.draw.text('预览',center = [480,200],fontsize = 30, fontname = 'microsoft.ttf',color = 'pink')
            for i in range(len(actor.plane_list)):
                actor.plane_list[i].draw()
                actor.plane_list[i].y = 500
                actor.plane_list[i].x = 480-(i-1)*100
            screen.draw.text('您已获得此飞机',center = [500,600],fontsize = 30, fontname = 'simsum.ttf',color = 'white')
            screen.draw.text('飞机列表：',center = [500,380],fontsize = 30, fontname = 'chinese.ttf',color = 'white')
            ret = Actor('return',pos=[50,50])
            ret.draw()
            if hub.actor_collide(ret,m) and mouse_down:
                self.state = 'start'
        if self.state == 'running':
            if int(self.now_level) <= 5:
                self.max_power *= int(self.now_level)
                self.max_speed *= int(self.now_level)
            actor.paint_running()
            if hub.setting.add:
                output()
            screen.draw.text('达成成就:'+self.stage,center=[420,30],color = 'white',fontname = 'simsum.ttf',fontsize = 30)
            screen.draw.text('距离终点还有:'+str(round(self.way,1))+'km/h',center=[420,120],fontname = 'simsum.ttf',color = 'white')
            logic.playing()
            center.playing()
        if self.state == 'win':
            screen.fill('yellow')
            screen.draw.text('游戏结束，你是一名合格的飞行员！\n您的钱已经到账在设置上\n按上键回到桌面',center=[500,360],fontname = 'simsum.ttf',fontsize = 50,color = 'red')
            self.way = self.away
            if keyboard.up:
                self.cnt+=1
                if self.age_score <= 95:
                    self.age_score += 5
                elif self.age_score > 95:
                    self.age_score = 100
                self.money += self.away
                self.state = 'start'
        if self.state == 'fail':
            screen.fill('grey')
            screen.draw.text('ao，输了，再试一次可能更好！\n原因：可能是您太晚起飞，或者飞得太高\n按上键回到首页',center=[500,360],fontname = 'simsum.ttf',fontsize = 50,color = 'red')
            if keyboard.up:
                self.age_score -= random.randint(10,50)
                self.state = 'start'
        if hub.setting.fbs:
            screen.draw.text('FPS:'+str(hub.fps),center = [900,700],fontname = 'simsum.ttf',color = 'green')
        m.draw()
        screen.draw.text('审核，你说我的作品会吓到别人\n如果我没猜错的话肯定是暴风雨彩蛋的问题\n那为什么地球上的暴风雨也会吓到人呢？\n那你为什么不去把地球下架呢',center = [800,700],color = '#FF8800',fontname = 'simsum.ttf',fontsize = 10)
    def on_mouse_move(pos):
        m.x = pos[0]
        m.y = pos[1]
    def on_mouse_down(pos):
        global mouse_down
        mouse_down = True
        t = time.time()
        if self.state == 'settings' and t - hub.setting.last_click_time > 0.2:
            if hub.setting.afbs.collidepoint(pos):
                hub.setting.fbs = not hub.setting.fbs
                hub.setting.afbs.image = 'on' if hub.setting.fbs else 'off'
                hub.setting.last_click_time = t  
            elif hub.setting.aadd.collidepoint(pos):
                hub.setting.add = not hub.setting.add
                hub.setting.aadd.image = 'on' if hub.setting.add else 'off'
                hub.setting.last_click_time = t
        print(self.random_weather)
    def on_mouse_up():
        global mouse_down
        mouse_down = False
    def randweather():
        self.random_weather = random.randint(1,15-int(self.now_level))
    clock.schedule_interval(update,1/1000)
    clock.schedule_interval(hub.get_fps,1.0)
    clock.schedule_interval(save,20.0)
    clock.schedule_interval(randweather,15)
    pgzrun.go()