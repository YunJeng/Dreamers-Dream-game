__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup, tools
from .. import constants as c
from . import powerups
from .. import game_sound
#from .. components import info
import subprocess

class Mario(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['main']
        self.music_dict = setup.CHUCK_SFX  # 保留以便用於其他非背景音樂用

        self.setup_timers()
        self.setup_state_booleans()
        self.setup_forces()
        self.setup_counters()
        self.load_images_from_sheet()
        #self.sound = game_sound.Sound()

        self.state = c.WALK
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        self.key_timer = 0


    def setup_timers(self):
        """Sets up timers for animations"""
        self.walking_timer = 0
        self.death_timer = 0
        self.transition_timer = 0
        self.flag_pole_timer = 0
        self.invincible_animation_timer = 0
        self.invincible_start_timer = 0
        self.fire_transition_timer = 0
        self.last_fireball_time = 0
        self.hurt_invisible_timer = 0
        self.hurt_invisible_timer2 = 0
        


    def setup_state_booleans(self):
        """Sets up booleans that affect Mario's behavior"""
        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.in_transition_state = False
        self.in_castle = False
        self.crouching = False
        self.hurt_invincible = False
        self.invincible = False
        #self.big = False
        self.fire = False
        self.allow_fireball = True
        self.losing_invincibility = False
        self.just_become_big = False
        self.getcrown = False

    def setup_forces(self):
        """Sets up forces that affect Mario's velocity"""
        self.x_vel = 0
        self.y_vel = 0
        #self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        #self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY


    def setup_counters(self):
        """These keep track of various total for important values"""
        self.frame_index = 0
        self.invincible_index = 0
        self.fire_transition_index = 0
        self.fireball_count = 0
        self.flag_pole_right = 0


    def load_images_from_sheet(self):
        """Extracts Mario images from his sprite sheet and assigns
        them to appropriate lists"""
        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.right_small_green_frames = []
        self.left_small_green_frames = []
        self.right_small_red_frames = []
        self.left_small_red_frames = []
        self.right_small_black_frames = []
        self.left_small_black_frames = []

        self.right_big_normal_frames = []
        self.left_big_normal_frames = []
        self.right_big_green_frames = []
        self.left_big_green_frames = []
        self.right_big_red_frames = []
        self.left_big_red_frames = []
        self.right_big_black_frames = []
        self.left_big_black_frames = []

        self.right_fire_frames = []
        self.left_fire_frames = []
        
        #=== Images for normal small mario ===#

        self.right_small_normal_frames.append(
            self.get_image(13, 0, 200, 256))  # 站著時的效果 [0]  #walk2(8)
        self.right_small_normal_frames.append(
            self.get_image(13,  0, 200, 256))  # Right walking 1 [1] #walk1(1)
        self.right_small_normal_frames.append(
            self.get_image(715,	289, 200, 256))  # Right walking 2 [2] #walk2(8)
        self.right_small_normal_frames.append(
            self.get_image(13,  0, 200, 256))  # Right walking 3 [3] #walk1(1)
        self.right_small_normal_frames.append(
            self.get_image(468, 0, 220, 256))  # Right jump 1 [4] #jump1(3)
        self.right_small_normal_frames.append(
            self.get_image(234, 0, 220, 256))  # Right jump 2 [5] #jump2(2) # Right skid [5]
        self.right_small_normal_frames.append(
            self.get_image(702, 0, 220, 256))  # Death frame [6] #death(4)
        self.right_small_normal_frames.append(
            self.get_image(0, 0, 220, 256))  # Transition small to big [7] #這個要刪掉
        self.right_small_normal_frames.append(
            self.get_image(0, 0, 220, 256))  # Transition big to small [8] #這個要刪掉
        self.right_small_normal_frames.append(
            self.get_image(0, 0, 220, 256))  # Frame 1 of flag pole Slide [9] #這個要刪掉
        self.right_small_normal_frames.append(
            self.get_image(0, 0, 220, 256))  # Frame 2 of flag pole slide [10] #這個要刪掉'''

        #==dontneed==#Images for small green mario (for invincible animation)#

        self.right_small_green_frames.append(
            self.get_image(0, 0, 220, 256))  # 站著時的效果 [0]  #walk2(8)
        self.right_small_green_frames.append(
            self.get_image(0,  0, 220, 256))  # Right walking 1 [1] #walk1(1)
        self.right_small_green_frames.append(
            self.get_image(702,	289, 220, 256))  # Right walking 2 [2] #walk2(8)
        self.right_small_green_frames.append(
            self.get_image(0,  0, 220, 256))  # Right walking 3 [3] #walk1(1)
        self.right_small_green_frames.append(
            self.get_image(468, 0, 220, 256))  # Right jump 1 [4] #jump1(3)
        self.right_small_green_frames.append(
            self.get_image(234, 0, 220, 256))  # Right jump 2 [5] #jump2(2) # Right skid [5]

        #==dontneed==#Images for red mario (for invincible animation)#

        self.right_small_red_frames.append(
            self.get_image(0, 0, 220, 256))  # 站著時的效果 [0]  #walk2(8)
        self.right_small_red_frames.append(
            self.get_image(0,  0, 220, 256))  # Right walking 1 [1] #walk1(1)
        self.right_small_red_frames.append(
            self.get_image(702,	289, 220, 256))  # Right walking 2 [2] #walk2(8)
        self.right_small_red_frames.append(
            self.get_image(0,  0, 220, 256))  # Right walking 3 [3] #walk1(1)
        self.right_small_red_frames.append(
            self.get_image(468, 0, 220, 256))  # Right jump 1 [4] #jump1(3)
        self.right_small_red_frames.append(
            self.get_image(234, 0, 220, 256))  # Right jump 2 [5] #jump2(2) # Right skid [5]

        #==dontneed==#Images for black mario (for invincible animation)#

        self.right_small_black_frames.append(
            self.get_image(0, 0, 220, 256))  # 站著時的效果 [0]  #walk2(8)
        self.right_small_black_frames.append(
            self.get_image(0,  0, 220, 256))  # Right walking 1 [1] #walk1(1)
        self.right_small_black_frames.append(
            self.get_image(702,	289, 220, 256))  # Right walking 2 [2] #walk2(8)
        self.right_small_black_frames.append(
            self.get_image(0,  0, 220, 256))  # Right walking 3 [3] #walk1(1)
        self.right_small_black_frames.append(
            self.get_image(468, 0, 220, 256))  # Right jump 1 [4] #jump1(3)
        self.right_small_black_frames.append(
            self.get_image(234, 0, 220, 256))  # Right jump 2 [5] #jump2(2) # Right skid [5]

        #Images for normal big Mario

        self.right_big_normal_frames.append(
            self.get_image(0, 578, 220, 256, scale_multiplier=1.2))  # Right 站著時的效果 [0] #walk2(9)
        self.right_big_normal_frames.append(
            self.get_image(234, 578, 220, 256, scale_multiplier=1.2))  # Right walking 1 [1] #walk1(10)
        self.right_big_normal_frames.append(
            self.get_image(0, 578, 220, 256, scale_multiplier=1.2))  # Right walking 2 [2] #walk2(9)
        self.right_big_normal_frames.append(
            self.get_image(234, 578, 220, 256, scale_multiplier=1.2))  # Right walking 3 [3] #walk1(10)
        self.right_big_normal_frames.append(
            self.get_image(702, 578, 220, 256, scale_multiplier=1.2))  # Right jump [4] #jump1(12)
        self.right_big_normal_frames.append(
            self.get_image(468, 578, 220, 256, scale_multiplier=1.2))  # Right skid [5] #jump2(11)
        self.right_big_normal_frames.append(
            self.get_image(234, 289, 220, 256, scale_multiplier=1.2))  # Right throwing [6] #att(6)
        self.right_big_normal_frames.append(
            self.get_image(0, 289, 220, 256, scale_multiplier=1.2))  # Right crouching [7] #death(5)


        #==dontneed==#Images for green big Mario#

        self.right_big_green_frames.append(
            self.get_image(0, 578, 220, 256))  # Right 站著時的效果 [0] #walk2(9)
        self.right_big_green_frames.append(
            self.get_image(234, 578, 220, 256))  # Right walking 1 [1] #walk1(10)
        self.right_big_green_frames.append(
            self.get_image(0, 578, 220, 256))  # Right walking 2 [2] #walk2(9)
        self.right_big_green_frames.append(
            self.get_image(234, 578, 220, 256))  # Right walking 3 [3] #walk1(10)
        self.right_big_green_frames.append(
            self.get_image(702, 578, 220, 256))  # Right jump [4] #jump1(12)
        self.right_big_green_frames.append(
            self.get_image(468, 578, 220, 256))  # Right skid [5] #jump2(11)
        self.right_big_green_frames.append(
            self.get_image(234, 289, 220, 256))  # Right throwing [6] #att(6)
        self.right_big_green_frames.append(
            self.get_image(0, 289, 220, 256))  # Right crouching [7] #death(5)

        #==dontneed==#Images for red big Mario#

        self.right_big_red_frames.append(
            self.get_image(0, 578, 220, 256))  # Right 站著時的效果 [0] #walk2(9)
        self.right_big_red_frames.append(
            self.get_image(234, 578, 220, 256))  # Right walking 1 [1] #walk1(10)
        self.right_big_red_frames.append(
            self.get_image(0, 578, 220, 256))  # Right walking 2 [2] #walk2(9)
        self.right_big_red_frames.append(
            self.get_image(234, 578, 220, 256))  # Right walking 3 [3] #walk1(10)
        self.right_big_red_frames.append(
            self.get_image(702, 578, 220, 256))  # Right jump [4] #jump1(12)
        self.right_big_red_frames.append(
            self.get_image(468, 578, 220, 256))  # Right skid [5] #jump2(11)
        self.right_big_red_frames.append(
            self.get_image(234, 289, 220, 256))  # Right throwing [6] #att(6)
        self.right_big_red_frames.append(
            self.get_image(0, 289, 220, 256))  # Right crouching [7] #death(5)

        #==dontneed==#Images for black big Mario#

        self.right_big_black_frames.append(
            self.get_image(0, 578, 220, 256))  # Right 站著時的效果 [0] #walk2(9)
        self.right_big_black_frames.append(
            self.get_image(234, 578, 220, 256))  # Right walking 1 [1] #walk1(10)
        self.right_big_black_frames.append(
            self.get_image(0, 578, 220, 256))  # Right walking 2 [2] #walk2(9)
        self.right_big_black_frames.append(
            self.get_image(234, 578, 220, 256))  # Right walking 3 [3] #walk1(10)
        self.right_big_black_frames.append(
            self.get_image(702, 578, 220, 256))  # Right jump [4] #jump1(12)
        self.right_big_black_frames.append(
            self.get_image(468, 578, 220, 256))  # Right skid [5] #jump2(11)
        self.right_big_black_frames.append(
            self.get_image(234, 289, 220, 256))  # Right throwing [6] #att(6)
        self.right_big_black_frames.append(
            self.get_image(0, 289, 220, 256))  # Right crouching [7] #death(5)

        #==dontneed==#Images for Fire Mario ===#

        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right standing [0] #角色在(x, y)=(3, 1)（從左上角開始數）
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right walking 1 [1] #角色在(x, y)=(4, 1)
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right walking 2 [2]
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right walking 3 [3]
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right jump 1 [4] #角色在(x, y)=(3, 2)
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right jump 2 [5] #角色在(x, y)=(4, 2)
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right throwing [6] #角色在(x, y)=(3, 3)
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Right crouching [7] #先用死亡的圖
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Place holder [8]
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Frame 1 of flag pole slide [9] #這個要刪掉
        self.right_fire_frames.append(
            self.get_image(0, 0, 220, 256))  # Frame 2 of flag pole slide [10] #這個要刪掉


        #The left image frames are numbered the same as the right
        #frames but are simply reversed.

        for frame in self.right_small_normal_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_normal_frames.append(new_image)

        for frame in self.right_small_green_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_green_frames.append(new_image)

        for frame in self.right_small_red_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_red_frames.append(new_image)

        for frame in self.right_small_black_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_black_frames.append(new_image)

        for frame in self.right_big_normal_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_normal_frames.append(new_image)

        for frame in self.right_big_green_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_green_frames.append(new_image)

        for frame in self.right_big_red_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_red_frames.append(new_image)

        for frame in self.right_big_black_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_black_frames.append(new_image)

        for frame in self.right_fire_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_fire_frames.append(new_image)


        self.normal_small_frames = [self.right_small_normal_frames,
                              self.left_small_normal_frames]

        self.green_small_frames = [self.right_small_green_frames,
                             self.left_small_green_frames]

        self.red_small_frames = [self.right_small_red_frames,
                           self.left_small_red_frames]

        self.black_small_frames = [self.right_small_black_frames,
                             self.left_small_black_frames]

        self.invincible_small_frames_list = [self.normal_small_frames,
                                          self.green_small_frames,
                                          self.red_small_frames,
                                          self.black_small_frames]

        self.normal_big_frames = [self.right_big_normal_frames,
                                  self.left_big_normal_frames]

        self.green_big_frames = [self.right_big_green_frames,
                                 self.left_big_green_frames]

        self.red_big_frames = [self.right_big_red_frames,
                               self.left_big_red_frames]

        self.black_big_frames = [self.right_big_black_frames,
                                 self.left_big_black_frames]

        self.fire_frames = [self.right_fire_frames,
                            self.left_fire_frames]

        self.invincible_big_frames_list = [self.normal_big_frames,
                                           self.green_big_frames,
                                           self.red_big_frames,
                                           self.black_big_frames]

        self.all_images = [self.right_big_normal_frames,
                           self.right_big_black_frames,
                           self.right_big_red_frames,
                           self.right_big_green_frames,
                           self.right_small_normal_frames,
                           self.right_small_green_frames,
                           self.right_small_red_frames,
                           self.right_small_black_frames,
                           self.left_big_normal_frames,
                           self.left_big_black_frames,
                           self.left_big_red_frames,
                           self.left_big_green_frames,
                           self.left_small_normal_frames,
                           self.left_small_red_frames,
                           self.left_small_green_frames,
                           self.left_small_black_frames]


        self.right_frames = self.normal_small_frames[0]
        self.left_frames = self.normal_small_frames[1]


    def get_image(self, x, y, width, height, scale_multiplier=1):
        """Extracts image from sprite sheet and scales it"""
        image = pg.Surface([width, height], pg.SRCALPHA)
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        final_scale = c.SIZE_MULTIPLIER * scale_multiplier
        image = pg.transform.scale(image,
                                (int(width * final_scale),
                                    int(height * final_scale)))
        return image



    def update(self, keys, game_info, fire_group):
        """Updates Mario's states and animations once per frame"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state(keys, fire_group)
        self.check_for_special_state()
        self.animation()


    def handle_state(self, keys, fire_group):
        """Determines Mario's behavior based on his state"""
        if self.state == c.STAND:
            self.standing(keys, fire_group)
        elif self.state == c.WALK:
            self.walking(keys, fire_group)
        elif self.state == c.JUMP:
            self.jumping(keys, fire_group)
        elif self.state == c.FALL:
            self.falling(keys, fire_group)
        elif self.state == c.DEATH_JUMP:
            self.jumping_to_death()
        elif self.state == c.SMALL_TO_BIG:
            self.changing_to_big()
        elif self.state == c.BIG_TO_FIRE:
            self.changing_to_fire()
        elif self.state == c.BIG_TO_SMALL:
            self.changing_to_small()
        
        elif self.state == c.BOTTOM_OF_POLE:
            self.sitting_at_bottom_of_pole()
        elif self.state == c.WALKING_TO_CASTLE:
            self.walking_to_castle()
        elif self.state == c.END_OF_LEVEL_FALL:
            self.falling_at_end_of_level()
        '''elif self.state == c.FLAGPOLE:
                    self.flag_pole_sliding()'''

    def standing(self, keys, fire_group):
        """This function is called if Mario is standing still"""
        self.check_to_allow_jump(keys)
        self.check_to_allow_fireball(keys)
        
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0

        if keys[tools.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)

        if keys[tools.keybinding['down']]:
            self.crouching = True

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.get_out_of_crouch()
            self.state = c.WALK
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.get_out_of_crouch()
            self.state = c.WALK
        elif keys[tools.keybinding['jump']]:
            if self.allow_jump:
                #setup.SFX['small_jump'].play()
                subprocess.Popen(['chuck', self.music_dict['small_jump']])  # ChucK 播放
                self.state = c.JUMP
                self.y_vel = c.JUMP_VEL
        else:
            self.state = c.STAND

        if not keys[tools.keybinding['down']]:
            self.get_out_of_crouch()


    def get_out_of_crouch(self):
        """Get out of crouch"""
        bottom = self.rect.bottom
        left = self.rect.x
        if self.facing_right:
            self.image = self.right_frames[0]
        else:
            self.image = self.left_frames[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left
        self.crouching = False


    def check_to_allow_jump(self, keys):
        """Check to allow Mario to jump"""
        if not keys[tools.keybinding['jump']]:
            self.allow_jump = True


    def check_to_allow_fireball(self, keys):
        """Check to allow the shooting of a fireball"""
        if not keys[tools.keybinding['action']]:
            self.allow_fireball = True


    def shoot_fireball(self, powerup_group):
        """Shoots fireball, allowing no more than two to exist at once"""
        setup.SFX['fireball'].play()
        self.fireball_count = self.count_number_of_fireballs(powerup_group)

        if (self.current_time - self.last_fireball_time) > 200:
            if self.fireball_count < 2:
                self.allow_fireball = False
                powerup_group.add(
                    powerups.FireBall(self.rect.right, self.rect.y, self.facing_right))
                self.last_fireball_time = self.current_time

                self.frame_index = 6
                if self.facing_right:
                    self.image = self.right_frames[self.frame_index]
                else:
                    self.image = self.left_frames[self.frame_index]


    def count_number_of_fireballs(self, powerup_group):
        """Count number of fireballs that exist in the level"""
        fireball_list = []

        for powerup in powerup_group:
            if powerup.name == c.FIREBALL:
                fireball_list.append(powerup)

        return len(fireball_list)


    def walking(self, keys, fire_group):
        """This function is called when Mario is in a walking state
        It changes the frame, checks for holding down the run button,
        checks for a jump, then adjusts the state if necessary"""
        self.image = self.right_frames[self.frame_index] if self.facing_right else self.left_frames[self.frame_index]
        self.check_to_allow_jump(keys)
        self.check_to_allow_fireball(keys)

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = self.current_time
        else:
            if (self.current_time - self.walking_timer >
                    self.calculate_animation_speed()):
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1

                self.walking_timer = self.current_time

        if keys[tools.keybinding['action']]:
            #self.max_x_vel = c.MAX_RUN_SPEED
            #self.x_accel = c.RUN_ACCEL
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)

        if keys[tools.keybinding['jump']]:
            if self.allow_jump:
                #setup.SFX['small_jump'].play()
                subprocess.Popen(['chuck', self.music_dict['small_jump']])   # ChucK 播放

                self.state = c.JUMP
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.JUMP_VEL - .5
                else:
                    self.y_vel = c.JUMP_VEL

        if keys[tools.keybinding['left']]:
            self.get_out_of_crouch()
            self.facing_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                #self.x_accel = c.SMALL_TURNAROUND
            else:
                #self.x_accel = c.WALK_ACCEL
                self.x_vel = -c.FIXED_SPEED

        elif keys[tools.keybinding['right']]:
            self.get_out_of_crouch()
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
                #self.x_accel = c.SMALL_TURNAROUND
            else:
                #self.x_accel = c.WALK_ACCEL
                self.x_vel = c.FIXED_SPEED
        else:
            self.x_vel = 0
            self.state = c.STAND
        



    def calculate_animation_speed(self):
        """Used to make walking animation speed be in relation to
        Mario's x-vel"""
        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed


    def jumping(self, keys, fire_group):
        """Called when Mario is in a JUMP state."""
        self.allow_jump = False
        self.frame_index = 4
        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity
        self.check_to_allow_fireball(keys)

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.x_vel = -c.FIXED_SPEED

        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.x_vel = c.FIXED_SPEED
        else:
            self.x_vel = 0
            self.state = c.STAND

        if not keys[tools.keybinding['jump']]:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[tools.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)


    def falling(self, keys, fire_group):
        """Called when Mario is in a FALL state"""
        self.check_to_allow_fireball(keys)
        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.x_vel = -c.FIXED_SPEED

        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.x_vel = c.FIXED_SPEED
        else:
            self.x_vel = 0
            self.state = c.STAND

        if keys[tools.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)


    def jumping_to_death(self): #死亡過程
        """Called when Mario is in a DEATH_JUMP state"""
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 500:
            self.rect.y += self.y_vel
            self.y_vel += self.gravity


    def start_death_jump(self, game_info): #死亡動畫起始
        """Used to put Mario in a DEATH_JUMP state"""
        self.dead = True
        game_info[c.MARIO_DEAD] = True
        self.y_vel = -11
        self.gravity = .5
        self.frame_index = 6
        self.image = self.right_frames[self.frame_index]
        self.state = c.DEATH_JUMP
        self.in_transition_state = True

    def changing_to_big(self):
        """Changes Mario's image attribute based on time while
        transitioning to big"""
        self.in_transition_state = True

        if self.facing_right:
            frames = [self.right_small_normal_frames[3],
                      self.right_big_normal_frames[3]]
            print("轉換用的大圖:", frames[1])
        else:
            frames = [self.left_small_normal_frames[3],
                      self.left_big_normal_frames[3]]
            
        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif (self.current_time - self.transition_timer) < 265:
            self.image = frames[1]
        elif (self.current_time - self.transition_timer) < 330:
            self.image = frames[0]
        elif (self.current_time - self.transition_timer) < 395:
            self.image = frames[1]
        elif (self.current_time - self.transition_timer) < 460:
            self.image = frames[0]
        elif (self.current_time - self.transition_timer) < 525:
            self.image = frames[1]
        elif (self.current_time - self.transition_timer) < 590:
            self.image = frames[0]
        elif (self.current_time - self.transition_timer) < 655:
            self.image = frames[1]
        elif (self.current_time - self.transition_timer) < 720:
            self.image = frames[0]
        elif (self.current_time - self.transition_timer) < 785:
            self.image = frames[1]
        elif (self.current_time - self.transition_timer) < 850:
            self.image = frames[0]
        elif (self.current_time - self.transition_timer) < 915:
            self.image = frames[1]
            #print("become big")
            self.in_transition_state = False
        
            self.transition_timer = 0
            self.become_big()
            self.state = c.WALK
            

    def timer_between_these_two_times(self,start_time, end_time):
        """Checks if the timer is at the right time for the action. Reduces
        the ugly code."""
        if (self.current_time - self.transition_timer) >= start_time\
            and (self.current_time - self.transition_timer) < end_time:
            return True


    def set_mario_to_middle_image(self):
        """During a change from small to big, sets mario's image to the
        transition/middle size"""
        if self.facing_right:
            self.image = self.normal_small_frames[0][7]
        else:
            self.image = self.normal_small_frames[1][7]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx


    def set_mario_to_small_image(self):
        """During a change from small to big, sets mario's image to small"""
        if self.facing_right:
            self.image = self.normal_small_frames[0][0]
        else:
            self.image = self.normal_small_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx


    def set_mario_to_big_image(self):
        """During a change from small to big, sets mario's image to big"""
        if self.facing_right:
            self.image = self.normal_big_frames[0][0]
        else:
            self.image = self.normal_big_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx
        

    def become_big(self):
        self.getcrown = True
        self.right_frames = self.right_big_normal_frames
        self.left_frames = self.left_big_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        print("切換成大馬力歐圖片:", self.right_frames[0])  # 新增這一行
        self.rect = image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left
        self.just_become_big = True
        self.frame_index = 0
        self.image = self.right_frames[0] if self.facing_right else self.left_frames[0]
        print("變身後圖片是：", self.image)


    def changing_to_fire(self):
        """Called when Mario is in a BIG_TO_FIRE state (i.e. when
        he obtains a fire flower"""
        self.in_transition_state = True

        if self.facing_right:
            frames = [self.right_fire_frames[3],
                      self.right_big_green_frames[3],
                      self.right_big_red_frames[3],
                      self.right_big_black_frames[3]]
        else:
            frames = [self.left_fire_frames[3],
                      self.left_big_green_frames[3],
                      self.left_big_red_frames[3],
                      self.left_big_black_frames[3]]

        if self.fire_transition_timer == 0:
            self.fire_transition_timer = self.current_time
        elif (self.current_time - self.fire_transition_timer) > 65 and (self.current_time - self.fire_transition_timer) < 130:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 195:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 260:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 325:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 390:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 455:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 520:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 585:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 650:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 715:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 780:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 845:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 910:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 975:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 1040:
            self.image = frames[2]
            self.fire = True
            self.in_transition_state = False
            self.state = c.WALK
            self.transition_timer = 0


    def changing_to_small(self):
        """Mario's state and animation when he shrinks from big to small
        after colliding with an enemy"""
        self.in_transition_state = True
        self.hurt_invincible = True
        self.state = c.BIG_TO_SMALL #這個狀態是從有皇冠到沒有皇冠

        if self.facing_right:
            frames = [self.right_big_normal_frames[4],
                      self.right_big_normal_frames[5],
                      self.right_small_normal_frames[5]
                      ]
        else:
            frames = [self.left_big_normal_frames[4],
                      self.left_big_normal_frames[5],
                      self.left_small_normal_frames[5]
                     ]

        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif (self.current_time - self.transition_timer) < 265:
            self.image = frames[0]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 330:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 395:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 460:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 525:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 590:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 655:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 720:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 785:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 850:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 915:
            self.image = frames[2]
            self.adjust_rect()
            self.in_transition_state = False
            self.state = c.WALK
            #self.big = False
            self.getcrown=False
            self.transition_timer = 0
            self.hurt_invisible_timer = 0
            self.become_small()


    def adjust_rect(self):
        """Makes sure new Rect has the same bottom and left
        location as previous Rect"""
        x = self.rect.x
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom


    def become_small(self):
        #self.big = False
        self.getcrown=False
        self.right_frames = self.right_small_normal_frames
        self.left_frames = self.left_small_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect()
        self.image = image  # 確保最後 image 被指定
        self.rect.bottom = bottom
        self.rect.x = left


    """def flag_pole_sliding(self):
        State where Mario is sliding down the flag pole
        self.state = c.FLAGPOLE
        self.in_transition_state = True
        self.x_vel = 0
        self.y_vel = 0

        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
        elif self.rect.bottom < 493:
            '''if (self.current_time - self.flag_pole_timer) < 65:
                self.image = self.right_frames[0]
            elif (self.current_time - self.flag_pole_timer) < 130:
                self.image = self.right_frames[0]
            elif (self.current_time - self.flag_pole_timer) >= 130:
                self.flag_pole_timer = self.current_time'''

            self.rect.right = self.flag_pole_right
            self.y_vel = 5
            self.rect.y += self.y_vel

            if self.rect.bottom >= 488:
                self.flag_pole_timer = self.current_time

        elif self.rect.bottom >= 493:
            pass
            #self.image = self.right_frames[0]"""


    def sitting_at_bottom_of_pole(self):
        """State when mario is at the bottom of the flag pole"""
        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
            #self.image = self.left_frames[0]
        elif (self.current_time - self.flag_pole_timer) < 210:
            self.image = self.left_frames[0]
        else:
            self.in_transition_state = False
            if self.rect.bottom < 485:
                self.state = c.END_OF_LEVEL_FALL
            else:
                self.state = c.WALKING_TO_CASTLE


    def set_state_to_bottom_of_pole(self):
        """Sets Mario to the BOTTOM_OF_POLE state"""
        #self.image = self.left_frames[9]
        right = self.rect.right
        self.rect.bottom = 493
        self.rect.x = right
        if self.getcrown:
            self.rect.x -= 10
        self.flag_pole_timer = 0
        self.state = c.BOTTOM_OF_POLE


    def walking_to_castle(self):
        """State when Mario walks to the castle to end the level"""
        #self.max_x_vel = 5
        #self.x_accel = c.WALK_ACCEL
        self.x_vel = c.FIXED_SPEED

        if (self.walking_timer == 0 or (self.current_time - self.walking_timer) > 200):
            self.walking_timer = self.current_time

        elif (self.current_time - self.walking_timer) > self.calculate_animation_speed():
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
            self.walking_timer = self.current_time


    def falling_at_end_of_level(self, *args):
        """State when Mario is falling from the flag pole base"""
        self.y_vel += c.GRAVITY



    def check_for_special_state(self):
        """Determines if Mario is invincible, Fire Mario or recently hurt"""
        self.check_if_invincible()
        self.check_if_fire()
        self.check_if_hurt_invincible()
        self.check_if_crouching()


    def check_if_invincible(self):
        if self.invincible:
            if ((self.current_time - self.invincible_start_timer) < 10000):
                self.losing_invincibility = False
                self.change_frame_list(30)
            elif ((self.current_time - self.invincible_start_timer) < 12000):
                self.losing_invincibility = True
                self.change_frame_list(100)
            else:
                self.losing_invincibility = False
                self.invincible = False
        else:
            if self.getcrown:
                self.right_frames = self.right_big_normal_frames
                self.left_frames = self.left_big_normal_frames
            else:
                self.right_frames = self.right_small_normal_frames
                self.left_frames = self.left_small_normal_frames

    def change_frame_list(self, frame_switch_speed):
        if (self.current_time - self.invincible_animation_timer) > frame_switch_speed:
            if self.invincible_index < (len(self.invincible_small_frames_list) - 1):
                self.invincible_index += 1
            else:
                self.invincible_index = 0

            if self.getcrown:
                frames = self.invincible_big_frames_list[self.invincible_index]
            else:
                frames = self.invincible_small_frames_list[self.invincible_index]

            self.right_frames = frames[0]
            self.left_frames = frames[1]

            self.invincible_animation_timer = self.current_time

    def check_if_fire(self):
        if self.fire:
            self.right_frames = self.fire_frames[0]
            self.left_frames = self.fire_frames[1]

    def check_if_hurt_invincible(self):
        """Check if Mario is still temporarily invincible after getting hurt"""
        if self.hurt_invincible and self.state != c.BIG_TO_SMALL:
            if self.hurt_invisible_timer2 == 0:
                self.hurt_invisible_timer2 = self.current_time
            elif (self.current_time - self.hurt_invisible_timer2) < 2000:
                self.hurt_invincible_check()
            else:
                self.hurt_invincible = False
                self.hurt_invisible_timer = 0
                self.hurt_invisible_timer2 = 0
                for frames in self.all_images:
                    for image in frames:
                        image.set_alpha(255)
    
    def hurt_invincible_check(self):
        """Makes Mario invincible on a fixed interval"""
        if self.hurt_invisible_timer == 0:
            self.hurt_invisible_timer = self.current_time
        elif (self.current_time - self.hurt_invisible_timer) < 35:
            self.image.set_alpha(0)
        elif (self.current_time - self.hurt_invisible_timer) < 70:
            self.image.set_alpha(255)
            self.hurt_invisible_timer = self.current_time

    def check_if_crouching(self):
        """Checks if mario is crouching"""
        if self.crouching and self.getcrown:
            bottom = self.rect.bottom
            left = self.rect.x
            if self.facing_right:
                self.image = self.right_frames[7]
            else:
                self.image = self.left_frames[7]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.x = left

    def animation(self):
        """Adjusts Mario's image for animation"""
        if self.just_become_big:
            print("跳過動畫，保留變大圖片")
            self.just_become_big = False
            return  # ← 要在這裡就結束 animation，避免其他判斷干擾

        # ⬇ 這些 state 判斷應該在後面執行
        if self.state == c.DEATH_JUMP \
            or self.state == c.SMALL_TO_BIG \
            or self.state == c.BIG_TO_FIRE \
            or self.state == c.BIG_TO_SMALL \
            or self.state == c.FLAGPOLE \
            or self.state == c.BOTTOM_OF_POLE \
            or self.crouching:
            return  # 也用 return，避免執行到下方 image 設定

        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
