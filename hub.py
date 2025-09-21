import pgzrun
from pgzero.actor import Actor
from pygame import time
import self
#本地版本是3.13，YBC是3.7，可能显示会有一些bug，敬请谅解！！！




a = 0
fps = 0
key_state = False
def on_key_down():
    global key_state
    key_state = True
def on_key_up():
    global key_state
    key_state = False
#def on_mouse_down 会有更多
def return_key():
    global key_state
    return key_state
def update():
    global a
    a+=1
def get_fps():
    global fps,a
    fps = a
    a = 0
    return fps
def move(walk):
    global fps
    return walk*(fps/60)
import pgzrun
def mouse_collide(actor1):
    if actor1.right > mouse.pos[0] and actor1.left < mouse.pos[0] and actor1.bottom > mouse.pos[1] and actor1.top < mouse.pos[1]:
        return True
    else:
        return False
def text_collide(文字上面,文字下面,文字左边,文字右边):
    if mouse.pos[1] > 文字上面 and mouse.pos[1] < 文字下面 and mouse.pos[0] > 文字左边 and mouse.pos[0] < 文字右边 and mouse.left:
        return True
    else:
        return False
def actor_collide(a,b):
    if a.right > b.left and a.left < b.right and a.bottom > b.top and a.top < b.bottom:
        return True
    else:
        return False
class setting:
    fbs = True
    add = True
    afbs = Actor("on",pos=[800,100])
    aadd = Actor("on",pos=[800,200])
    last_click_time = 0
def check_level():
    global self
    if self.age_score <= 0:
        ybc.enterbox('由于你的满意数过于低，我们自动退出~')
        exit()
    if int(self.now_level) <= 5 and self.age_score >= 80:
        if self.cnt >= self.j_cnt and self.money >= self.j_money:
            self.j_cnt *= 2
            self.j_money *= 2
            self.now_level = str(int(self.now_level)+1)
        return "还有"+str(self.j_money-self.money) + "钱和玩" + str(self.j_cnt-self.cnt) + "次游戏可以晋级\n温馨提示：适当玩游戏，不要玩太久哦~"
    else:
        return "已满级"