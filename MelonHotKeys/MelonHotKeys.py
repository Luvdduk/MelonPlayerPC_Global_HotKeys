# -*- coding: utf-8 -*-

from pywinauto.application import Application
from pywinauto.application import ProcessNotFoundError
from pynput import keyboard
from configparser import ConfigParser
# from PyQt5 import QtCore, QtGui, QtWidgets


#config 파일 생성 및 확인
try:
    config = ConfigParser()
    config.read('config.ini')
    print(config['HotKeys']['play-pause'])
    print("파일 확인")
except KeyError:
    config['HotKeys'] = {
    'play-pause': '<alt>+<shift>+w',
    'next':  '<alt>+<shift>+e',
    'preview': '<alt>+<shift>+q',
    'mute': '<alt>+<shift>+`',
    'overlay_toggle':'<alt>+<shift>+<f1>'
    }
    with open('./config.ini', 'w') as f:
        config.write(f)
    print("config파일 생성")

# 설정값 불러오기
def load_config():
    # GlobalHotKey 호출을 위한 전역변수
    global play_config, next_config, preview_config, mute_config, overlay_config
    play_config=config['HotKeys']['play-pause']
    next_config=config['HotKeys']['next']
    preview_config=config['HotKeys']['preview']
    mute_config=config['HotKeys']['mute']
    overlay_config=config['HotKeys']['overlay_toggle']

load_config()

# 멜론 연결
# 멜론 실행시까지 반복
while True:
    try:
        app = Application().connect(path= r"Melon.exe")
        print('멜론플레이어 감지')
        break
    except ProcessNotFoundError:
        print('멜론이 실행되어있지 않음')
        continue
mwin = app.window(title_re=u".*Melon", control_id=0)


def play():
    han=mwin.handle
    playing=app.window(title_re=u".*Melon", control_id=0,handle=han).재생.exists()

    if playing==True:
        print("재생")
        mwin.재생.click()
    else:
        print("일시정지")
        mwin.일시정지.click()


def next():
    print('다음곡')
    mwin.다음_곡.click()

def preview():
    print('이전곡')
    mwin.이전_곡.click()

def exit():
    quit()

# def v_up():
#     print('소리 크게')
#     app.window(title_re=u".*소리 크게.*", handle=134370).click()

# def v_down():
#     print('소리 작게')
#     app.window(title_re=u".*소리 작게.*", handle=199352).click()

def mute():
    han=mwin.handle
    mutev=app.window(title_re=u".*Melon", control_id=0,handle=han).소리_작게선택_시_음소거.exists()

    if mutev==True:
        print('음소거')
        mwin.소리_작게선택_시_음소거.click()
    else:
        print('음소거 해제')
        mwin.소리_켜기.click()



with keyboard.GlobalHotKeys({
    play_config: play,
    next_config: next,
    preview_config: preview,
    mute_config: mute,
    overlay_config: exit}) as h:
    
    h.join()