import pgzrun
import pgzero
import actor
import self
import random
import hub
from pgzero.keyboard import Keyboard
keyboard = Keyboard()


def playing():
    actor.road.x -= self.speed/10
    if actor.road.right <= 960:
        actor.road.left = 0
    if self.height >= 1000 and self.height <= 3000:
        actor.cloudy.draw()
        self.stage = '哇！是白云！'
    actor.cloudy.x -= self.speed/10
    if actor.cloudy.x < 0:
        actor.cloudy.x = 960
        actor.cloudy.y = random.randint(200,400)
    if self.height < 80 and (self.away - self.way) > 100:
        actor.sea.draw()
        actor.sea.y = 620
    if hub.actor_collide(actor.sea,actor.self) and not self.state == '即将降落':
        self.state = 'fail'
    if hub.actor_collide(actor.self,actor.road) and actor.self.image == 'self2':
        actor.self.image = 'self'
    elif not hub.actor_collide(actor.self,actor.road) and actor.self.image == 'self':
        actor.self.image = 'self2'
    if self.random_weather >= 1 and self.random_weather <= 4:
        actor.wind.draw()
        actor.bg.image = 'rain'
        if not hub.actor_collide(actor.self,actor.road): actor.self.angle -= random.randint(-2,2)
    elif self.random_weather == 5:
        actor.bg.image = 'rain'
        if not hub.actor_collide(actor.self,actor.road):
            self.height -= random.randint(1,3)
            self.speed -= random.randint(3,5)
    else:
        actor.bg.image = 'bg'
    if actor.self.angle > 50:
        actor.self.angle = 50
    if actor.self.angle < -50:
        actor.self.angle = -50