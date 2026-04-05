__author__ = 'justinarmstrong'

import pygame as pg
from . import setup
from . import constants as c
import subprocess

class Sound(object):
    """Handles all sound for the game using ChucK for background music and sound effects"""
    def __init__(self, overhead_info):
        self.sfx_dict = setup.SFX  # 音效字典，保留以便pygame音效播放用（可選）
        self.music_dict = setup.MUSIC  # 背景音樂檔案字典(ChucK腳本路徑)
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info

        self.music_process = None  # 背景音樂ChucK進程
        self.current_theme = None  # 正在播放的背景音樂
        self.state = None  # 狀態
        self.last_zone = None  # 區域標記

        self.sfx_processes = []  # 播放中的音效ChucK進程列表

        pg.mixer.init()
        self.set_music_mixer()

    def set_music_mixer(self):
        if self.overhead_info.state == c.LEVEL:
            self.state = c.NORMAL
        elif self.overhead_info.state == c.WIN:
            self.play_music(self.music_dict['win'])
            self.state = c.WIN
        elif self.overhead_info.state == c.GAME_OVER:
            self.play_music(self.music_dict['game_over'])
            self.state = c.GAME_OVER
        elif self.overhead_info.state == c.MAIN_MENU:
            self.play_music(self.music_dict['main_menu'])
            self.state = c.MAIN_MENU

    def play_music(self, chuck_file):
        """播放背景音樂，只播一首，若已播相同檔案則不重播"""
        if self.current_theme == chuck_file and self.music_process \
            and self.music_process.poll() is None:
            return
        self.stop_music()
        self.music_process = subprocess.Popen(['chuck', chuck_file])
        self.current_theme = chuck_file
        print(f"[Music] Start playing: {chuck_file}")

    def stop_music(self):
        """停止背景音樂"""
        if self.music_process:
            self.music_process.terminate()
            self.music_process.wait()
            self.music_process = None
            self.current_theme = None
            print("[Music] Stopped")

    def play_sound_effect(self, chuck_file):
        """播放音效，非背景音樂，可多個同時播放，播完自動結束"""
        p = subprocess.Popen(['chuck', chuck_file])
        self.sfx_processes.append(p)
        print(f"[SFX] Played: {chuck_file}")
        self.sfx_processes = [proc for proc in self.sfx_processes if proc.poll() is None]
    
    def play_sound_effect2(self, chuck_file): #jump
        """播放音效，非背景音樂，可多個同時播放，播完自動結束"""
        p = subprocess.Popen(['chuck', chuck_file])
        self.sfx_processes.append(p)
        print(f"[SFX] Played: {chuck_file}")
        # 清理結束的音效進程
        self.sfx_processes = [proc for proc in self.sfx_processes if proc.poll() is None]

    def play_music_by_position(self, x):
        if x < 2200:
            zone = 'spring'
        elif x < 5000:
            zone = 'summer'
        elif x < 6704:
            zone = 'autumn'
        else:
            zone = 'winter'
        if zone != self.last_zone:
            if zone in self.music_dict:
                self.play_music(self.music_dict[zone])
                self.last_zone = zone

    def update(self, game_info, mario):
        self.game_info = game_info
        self.mario = mario

        # 背景音樂邏輯
        if self.state == c.NORMAL:
            self.play_music_by_position(self.mario.rect.x)
        self.handle_state()

        # 清理音效已結束進程，避免殭屍進程
        self.sfx_processes = [proc for proc in self.sfx_processes if proc.poll() is None]

    def handle_state(self):
        if self.state == c.NORMAL:
            if self.mario.dead:
                self.stop_music()
                self.play_music(self.music_dict['death'])
                self.state = c.MARIO_DEAD
            elif self.mario.invincible and not self.mario.losing_invincibility:
                self.play_sound_effect(self.sfx_dict['invincible'])
                self.state = c.MARIO_INVINCIBLE
            elif self.mario.state == c.FLAGPOLE:
                self.play_sound_effect(self.sfx_dict['flagpole'])
                self.state = c.FLAGPOLE
            elif self.overhead_info.time == 100:
                #self.play_sound_effect(self.sfx_dict['out_of_time'])
                self.state = c.TIME_WARNING

        elif self.state == c.FLAGPOLE:
            if self.mario.state == c.WALKING_TO_CASTLE:
                self.play_sound_effect(self.sfx_dict['stage_clear'])
                self.state = c.STAGE_CLEAR

        elif self.state == c.STAGE_CLEAR:
            if self.mario.in_castle:
                self.play_sound_effect(self.sfx_dict['count_down'])
                self.state = c.FAST_COUNT_DOWN

        elif self.state == c.FAST_COUNT_DOWN:
            if self.overhead_info.time == 0:
                # 這裡pygame音效就直接停止，若你改用ChucK，請自行準備chuck停止邏輯
                self.sfx_dict['count_down'].stop()
                self.state = c.WORLD_CLEAR

        elif self.state == c.TIME_WARNING:
            if self.mario.dead:
                self.stop_music()
                self.play_music(self.music_dict['death'])
                self.state = c.MARIO_DEAD

        elif self.state == c.MARIO_INVINCIBLE:
            if (self.mario.current_time - self.mario.invincible_start_timer) > 11000:
                self.state = c.NORMAL
                self.current_theme = None
            elif self.mario.dead:
                self.stop_music()
                self.play_music(self.music_dict['death'])
                self.state = c.MARIO_DEAD

        elif self.state in [c.WORLD_CLEAR, c.MARIO_DEAD, c.GAME_OVER]:
            pass
