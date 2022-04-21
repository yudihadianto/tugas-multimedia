from pygame import mixer
mixer.init()
mixer.music.load('music/my_heart_will_the_end.mp3')
while True:
    x = int(input(''' ### MP3 Player CLI Python ###

    1. Play
    2. Pause
    3. Unpause
    4. Stop
    
    Silahkan Pilih Perintah : '''))

    if x == 1:
        mixer.music.play()
        print('....Music Playing....')
        print('''
              ''')
    elif x == 2:
        mixer.music.pause()
        print('....Music Pause....')
        print('''
             ''')
    elif x == 3:
        mixer.music.unpause()
        print('....Play Musik Again....')
        print('''
             ''')
    elif x == 4:
        mixer.music.stop()
        print('....Music Stop....')
        print('''
             ''')
    else:
        pass
