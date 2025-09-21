import pgzero
import pgzrun
import self
import actor
import hub
import random
from pgzero.keyboard import Keyboard
keyboard = Keyboard()
import math


def playing():
    global keyboard
    global self,actor,hub
    if keyboard.K_RIGHT:
        self.power += 2.1
        self.speed += self.power
    #动力控制
    if self.power < 0:
        self.power = 0.5
    if self.power > self.max_power+0.5:
        self.power = self.max_power
    self.power -= 0.1
    if keyboard.K_LEFT:
        self.power -= 0.5
        self.speed -= 100
    #速度控制
    if self.speed >= self.max_speed:
        self.speed = self.max_speed
    if self.power <= 0:
        self.speed -= 2
    if self.speed <= 0:
        self.speed = 0
    #高度控制
    if self.stage == '哇！是白云！':
        actor.road.y = 1500
    if self.height > 20000:
        self.state = 'fail'
        print(1)
    if self.way < 300:
        self.stage = '即将降落'
    if self.height < 300 and self.stage == '即将降落':
        actor.road.y = 620
    if hub.actor_collide(actor.road,actor.self) and self.stage == '即将降落' and self.speed <= 10:
        self.state = 'win'
    self.way -= self.speed/1800
    self.height += (self.speed/100)*(actor.self.angle / 100)
    #角度控制
    if keyboard.K_UP and actor.self.angle < 30 and not self.state == '即将降落':
        actor.self.angle += 1
        actor.road.y += actor.self.angle*(self.speed/100)
    if keyboard.K_DOWN and actor.self.angle > -30 and not hub.actor_collide(actor.self,actor.road) and not self.state == '即将降落':
        actor.self.angle -= 1
    if not hub.actor_collide(actor.self,actor.road) and self.height > 300:
        self.height -= 0.1
    if hub.actor_collide(actor.road,actor.self):
        actor.self.angle = 0
    if actor.self.angle < 15 and actor.self.angle > -15 and self.bu == True:
        self.bu = True
    else:
        self.bu = False