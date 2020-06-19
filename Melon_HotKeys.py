#-*-coding:utf-8
from pywinauto.application import Application
import pywinauto
from pynput import keyboard

# 멜론 연결
# 멜론 실행시까지 반복
while True:
    try:
        app = Application().connect(path= r"Melon.exe")
        print('멜론플레이어 감지')
        break
    except pywinauto.application.ProcessNotFoundError:
        print('멜론이  실행되어있지 않음')
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

'''def v_up():
    print('소리 크게')
    app.window(title_re=u".*소리 크게.*", handle=134370).click()

def v_down():
    print('소리 작게')
    app.window(title_re=u".*소리 작게.*", handle=199352).click()'''

def mute():
    han=mwin.handle
    mute=app.window(title_re=u".*Melon", control_id=0,handle=han).소리_작게선택_시_음소거.exists()

    if mute==True:
        print('음소거')
        mwin.소리_작게선택_시_음소거.click()
    else:
        print('음소거 해제')
        mwin.소리_켜기.click()
    

with keyboard.GlobalHotKeys({
        '<alt>+<shift>+w': play,
        '<alt>+<shift>+q': next,
        '<alt>+<shift>+e': preview,
        '<alt>+<shift>+`': mute,
        '<alt>+<shift>+<f1>': exit}) as h:
        
    h.join()
