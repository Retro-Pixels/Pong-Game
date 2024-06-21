from Field import PlayingField
from Melody import Melody
from Buzzer import PassiveBuzzer
from Button import Button
from Potentiometer import Potentiometer
import math
import utime as time

class PongGame:
    MODE_INIT = 1
    MODE_TWO_PLAYER = 3
    MODE_ONE_PLAYER = 2 
    MODE_GAME_OVER = 4

    def __init__(self):
        self.RetroPixlsLogo = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHw/n5+DwAAAAAAAAAAAAADuf44fjGAAAAAAAAAAAAAAw2AEGGwwAAAAAAAAAAAAAMdgBBjMMAAAAAAAAAAAAAD4fAQfDDAAAAAAAAB////A6GAEGgwwB////AAAQ///QMZ/hBmOcAT///QAAEAAAEBCAAAAQ8AEAAAAAABAAAAAAAAAAAAABAAABAAAT//+QAAADwAAAAR//+AAAE3d9gAAAA8AAAAEXN/gAABM3fYAAAAAAAAABEzfZAAATs2WAABgAAAAAARs22AAAE/t9gAAAAAAAAAEft9gAABP/fYD8ARn+wH4BHDfYAAAR//+QwyCxgEBgAR//+AAAEAAAAMMg4YBAMAEAAAAAABb89vD+IOGgQAwBp+8vAAAe//74wCGxgEACAW//54AAH///+MAhkYBAAwH///+AAB////jAIxn+fnwB////gAAwAAAIAAAAAAAAAQAAAIAAMAAACAAAAAAAAAEAAACAADAAAAgAAAAAAAABAAAAgAAwAAAIAAAAAAAAAQAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        self.PongGameLogo = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/B4YYfgPgcMM/wAAAAAAAMdxnmYAOAwz/MAAAAAAAAD8YZnmeDHv83z+AAAAAAAAwGGY5jgw7DMMwAAAAAAAAMAeGGH4D+wzDP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAH//////5n//////4AAAAABgAAAAAAYAAAAAAOAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYA/wAAAGAAAA/wBgAAAAAGA//AAABgAAB//AYAAAAABg//8AAAYAAB//8GAAAAAAYP//gAAGDgAf//BgAAAAAGD//wAABj+AH//wYAAAAABg//8AAAY/gB//8GAAAAAAYP//AAAGDgAP//BgAAAAAGAf+AAABgAAAf+AYAAAAABgD/AAAAYAAAH/AGAAAAAAYAMAAAAGAAAAIABgAAAAAGADwAAABgAAADwAYAAAAABgA8AAAAYAAAA8AGAAAAAAYAPAAAAGAAAAPABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAAB//////8Z//////+AAAAAAf//////mf//////gAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAADoAAAAAGAAAAAAwAAAAAAA+AAAAABgAAAAAfAAAAAAAIAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4AMMAAAMAAAMAAMHgAAAAGADDAAADAAADAADBtu488B7t987YB84A985v8bO7ccAbbMMbbAMbAcMbOsHjHzzwG2zDG2wDGwDzDzDBgxgOOBts23tsA3sAO3sw2cePffA+PnHObAHOAfHf+HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

        self.max_score = 10
        self.l_score = 0
        self.r_score = 0
        self.clean_count = 0

        self.paddle_left_old_y = -1
        self.paddle_right_old_y = -1
        self.paddle_width = 3
        self.paddle_height = 12
        self.paddle_x = 128 - self.paddle_width
        self.paddle_y = 30
        self.paddle_left_y = 0
        self.paddle_right_y = 0

        self.ball_speed = 6
        self.ball_width = 3
        self.ball_height = 3
        self.ball_half_height = self.ball_height >> 1
        self.ball_x = 64
        self.ball_y = 32
        self.ball_vx = self.ball_speed
        self.ball_vy = self.ball_speed

        self.max_x = 128
        self.max_y = 64
        self.min_y = 0
        self.min_x = 0

        self.mode = self.MODE_INIT

        self._field = PlayingField()
        self._buzz = PassiveBuzzer(17)
        self._melody = Melody(17)
        self._buttons = [
            Button(22, 'onePlayer', buttonhandler=self),
            Button(21, 'twoPlayer', buttonhandler=self)
        ]
        self._left_player = Potentiometer(26)
        self._right_player = Potentiometer(27)

        # Run the intro once at the start

    def buttonPressed(self, name):
        
        if name == 'onePlayer':
            if self.mode == self.MODE_INIT:
                self._field.clear()
                self.l_score = 0
                self.r_score = 0
                self.clean_count == 0
                self._field.draw_net_scores(self.l_score, self.r_score)
                self._melody.stop()
                self.mode = self.MODE_ONE_PLAYER
            elif self.mode == self.MODE_GAME_OVER:
                self.reset_game()
                self._melody.stop()
                self.titleScreen()
                self.mode = self.MODE_INIT
                
        if name == 'twoPlayer':
            if self.mode == self.MODE_INIT:
                self._field.clear()
                self.l_score = 0
                self.r_score = 0
                self.clean_count == 0
                self._field.draw_net_scores(self.l_score, self.r_score)
                self._melody.stop()
                self.mode = self.MODE_TWO_PLAYER
            elif self.mode == self.MODE_GAME_OVER:
                self.reset_game()
                self._melody.stop()
                self.titleScreen()
                self.mode = self.MODE_INIT

    def reset_game(self):
        self._field.showText("WIN!", 17, 90, 0)
        self._field.showText("WIN!", 17, 30, 0)
        self._field.draw_score(self.l_score, 30, 0)
        self._field.draw_score(self.l_score, 90, 0)
        self._field.clear()
        self.l_score = 0
        self.r_score = 0
        self.paddle_left_old_y = -1
        self.paddle_right_old_y = -1
        self.paddle_left_y = 0
        self.paddle_right_y = 0
        self.ball_x = self.max_x // 2
        self.ball_y = self.max_y // 2
        self.ball_vx = self.ball_speed
        self.ball_vy = self.ball_speed
        self._field.clear()  # Clear the display to remove any old scores or win text
        self._field.draw_net_scores(self.l_score, self.r_score)  # Draw the initial scores

        
    def buttonReleased(self, name):
        pass

    def titleScreen(self):
        self._field.clear()
        RetroPixlsBuffer = self._field.customToBuff(self.RetroPixlsLogo)
        PongGameBuffer = self._field.customToBuff(self.PongGameLogo)
        
        self._field.showShape(RetroPixlsBuffer, 0, 2)
        time.sleep(5)

        self._field.showShape(PongGameBuffer, 0, 2)
        
        self._field.draw_net_scores(0, 0)

    def twoPlayer(self):
        self.paddle_left_y = self._left_player.analog_to_digital()
        self.paddle_right_y = self._right_player.analog_to_digital()
        self.clean_count = (self.clean_count + 1) % 6
        if self.clean_count == 0:
            self._field.addToBuffer()
        if self.paddle_left_old_y != self.paddle_left_y or self.clean_count == 0:
            self._field.draw_paddle(self.paddle_left_old_y, 0, 0)
            self._field.draw_paddle(self.paddle_left_y, 1, 0)
            self.paddle_left_old_y = self.paddle_left_y
        if self.paddle_right_old_y != self.paddle_right_y or self.clean_count == 0:
            self._field.draw_paddle(self.paddle_right_old_y, 0, self.max_x - self.paddle_width)
            self._field.draw_paddle(self.paddle_right_y, 1, self.max_x - self.paddle_width)
            self.paddle_right_old_y = self.paddle_right_y
        self._field.draw_ball(self.ball_x, self.ball_y, 1)
        self._field.show()
        self._field.draw_ball(self.ball_x, self.ball_y, 0)
        self.ball_x += self.ball_vx
        self.ball_y += self.ball_vy
        self.checkCollision()
        
    def onePlayer(self):
        self.paddle_left_y = self._left_player.analog_to_digital()
        
        self.clean_count = (self.clean_count + 1) % 6
        if self.clean_count == 0:
            self._field.addToBuffer()
        if self.paddle_left_old_y != self.paddle_left_y or self.clean_count == 0:
            self._field.draw_paddle(self.paddle_left_old_y, 0, 0)
            self._field.draw_paddle(self.paddle_left_y, 1, 0)
            self.paddle_left_old_y = self.paddle_left_y
        
        self._field.draw_paddle(0, 1, self.max_x - self.paddle_width, self.max_y)
        
        self._field.draw_ball(self.ball_x, self.ball_y, 1)
        self._field.show()
        self._field.draw_ball(self.ball_x, self.ball_y, 0)
        self.ball_x += self.ball_vx
        self.ball_y += self.ball_vy
        self.checkCollisionOne()

    def checkCollisionOne(self):
        if self.ball_y > self.max_y - self.ball_height:
            self._buzz.play(200)
            time.sleep(0.05)
            self._buzz.stop()
            self.ball_vy = -self.ball_vy
            self.ball_y = self.max_y - self.ball_height
        elif self.ball_y < self.min_y:
            self._buzz.play(200)
            time.sleep(0.05)
            self._buzz.stop()
            self.ball_vy = -self.ball_vy
            self.ball_y = self.min_y
        
        # Always reflect off the right wall
        if self.ball_x >= self.max_x - self.ball_width:
            self._buzz.play(200)
            time.sleep(0.05)
            self._buzz.stop()
            self.ball_vx = -self.ball_vx
            self.ball_x = self.max_x - self.ball_width

        elif self.ball_x <= self.min_x + self.paddle_width:
            dy = (self.ball_y + self.ball_height) - self.paddle_left_y
            if dy > 0 and dy < self.paddle_height + self.ball_height:
                self._buzz.play(200)
                time.sleep(0.05)
                self._buzz.stop()
                dy = dy / (self.paddle_height + self.ball_height)
                self.ball_x = self.min_x + self.paddle_width
                angle = math.radians(90 - 60 + dy * 120)
                self.ball_vx = math.sin(angle) * self.ball_speed
                self.ball_vy = -math.cos(angle) * self.ball_speed
            else:
                self.point("right")
                self.ball_x = self.max_x >> 1
                self.ball_y = self.max_y >> 1
                self.ball_vx = -self.ball_vx

        self._field.draw_ball(self.ball_x, self.ball_y, 1)
        self._field.show()
        time.sleep(0.05)


    def checkCollision(self):
        if self.ball_y > self.max_y - self.ball_height:
            self._buzz.play(200)
            time.sleep(0.05)
            self._buzz.stop()
            self.ball_vy = -self.ball_vy
            self.ball_y = self.max_y - self.ball_height
        elif self.ball_y < self.min_y:
            self._buzz.play(200)
            time.sleep(0.05)
            self._buzz.stop()
            self.ball_vy = -self.ball_vy
            self.ball_y = self.min_y
        if self.ball_x >= self.max_x - self.ball_width:  # hit right paddle
            dy = (self.ball_y + self.ball_height) - self.paddle_right_y
            if dy > 0 and dy < self.paddle_height + self.ball_height:
                self._buzz.play(200)
                time.sleep(0.05)
                self._buzz.stop()
                dy = dy / (self.paddle_height + self.ball_height)
                self.ball_x = self.max_x - self.ball_width
                angle = math.radians(90 - 60 + dy * 120)
                self.ball_vx = -math.sin(angle) * self.ball_speed
                self.ball_vy = -math.cos(angle) * self.ball_speed
            else:
                self.point("left")
                self.ball_x = self.max_x >> 1
                self.ball_y = self.max_y >> 1
                self.ball_vx = -self.ball_vx
        elif self.ball_x <= self.min_x + self.paddle_width:
            dy = (self.ball_y + self.ball_height) - self.paddle_left_y
            if dy > 0 and dy < self.paddle_height + self.ball_height:
                self._buzz.play(200)
                time.sleep(0.05)
                self._buzz.stop()
                dy = dy / (self.paddle_height + self.ball_height)
                self.ball_x = self.min_x + self.paddle_width
                angle = math.radians(90 - 60 + dy * 120)
                self.ball_vx = math.sin(angle) * self.ball_speed
                self.ball_vy = -math.cos(angle) * self.ball_speed
            else:
                self.point("right")
                self.ball_x = self.max_x >> 1
                self.ball_y = self.max_y >> 1
                self.ball_vx = -self.ball_vx
        self._field.draw_ball(self.ball_x, self.ball_y, 1)
        self._field.show()
        time.sleep(0.05)

    def point(self, player):
        self._buzz.play(600)
        time.sleep(0.05)
        self._buzz.stop()
        if player == "left":
            self.l_score += 1
            self._field.draw_score(self.l_score, 30)
            if self.l_score == self.max_score:
                self._field.clear()  # Clear the display before showing the win text
                self._field.showText("WIN!", 17, 30, 1)
                time.sleep(0.5)
                self.mode = self.MODE_GAME_OVER
        elif player == "right":
            self.r_score += 1
            self._field.draw_score(self.r_score, 90)
            if self.r_score == self.max_score:
                self._field.clear()  # Clear the display before showing the win text
                self._field.showText("WIN!", 17, 90, 1)
                time.sleep(0.5)
                self.mode = self.MODE_GAME_OVER
    def run(self):
        
        self.titleScreen()
        
        while True:
            if self.mode == self.MODE_TWO_PLAYER:
                self.twoPlayer()
            elif self.mode == self.MODE_ONE_PLAYER:
                self.onePlayer()
            elif self.mode == self.MODE_INIT:
                self._melody.play_melody(39)
            elif self.mode == self.MODE_GAME_OVER:
                self._melody.play_melody(40)


if __name__ == '__main__':
    game = PongGame()
    game.run()
