from re import A
from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('MP3 Player Python')
root.iconbitmap('img/yh.ico')
root.geometry("500x300")

pygame.mixer.init()

# Fungsi Tambah Lagu


def add_song():
    song = filedialog.askopenfilename(
        initialdir='music/', title="Pilih Lagu", filetypes=(("mp3 Files", "*.mp3"), ))
    print(song)

    song = song.replace(
        # JIKA TIDAK BERFUNGSI/ERROR, SILAHKAN UBAH DESTINASI FOLDERNYA..!!!
        "D:/DATA 1/2. KAMPUS/SEMESTER 6/1312. Multimedia/tugas/multimedia4/music/", "")
    song = song.replace(".mp3", "")

    song_box.insert(END, song)

# Fungsi Tambah Beberapa Lagu


def add_many_songs():
    songs = filedialog.askopenfilenames(
        initialdir='music/', title="Pilih Lagu", filetypes=(("mp3 Files", "*.mp3"), ))

    for song in songs:

        song = song.replace(
            # JIKA TIDAK BERFUNGSI/ERROR, SILAHKAN UBAH DESTINASI FOLDERNYA..!!!
            "D:/DATA 1/2. KAMPUS/SEMESTER 6/1312. Multimedia/tugas/multimedia4/music/", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)

# Fungsi Hapus Lagu


def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

# Fungsi Hapus Semua Lagu


def delete_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()


# Fungsi Mainkan Lagu


def play():
    song = song_box.get(ACTIVE)
    song = f'music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


# Fungsi Pause Lagu

global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:

        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

# Fungsi Stop Lagu


def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

# Fungsi Lagu Berikutnya


def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    song = f'music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

# Fungsi Lagu Sebelumnya


def previous_song():
    next_one = song_box.curselection()
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    song = f'music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


song_box = Listbox(root, bg='black', fg='yellow', width=60,
                   selectbackground="white", selectforeground="black")
song_box.pack(pady=20)

# membuat tombol

back_btn_img = PhotoImage(file='img/back.png')
forward_btn_img = PhotoImage(file='img/forward.png')
play_btn_img = PhotoImage(file='img/play.png')
pause_btn_img = PhotoImage(file='img/pause.png')
stop_btn_img = PhotoImage(file='img/stop.png')

# membuat frame control

controls_frame = Frame(root)
controls_frame.pack()

# membuat tombol kontrol

back_btn = Button(controls_frame, image=back_btn_img,
                  borderwidth=0, command=previous_song)
forward_btn = Button(controls_frame, image=forward_btn_img,
                     borderwidth=0, command=next_song)
play_btn = Button(controls_frame, image=play_btn_img,
                  borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_btn_img,
                   borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(controls_frame, image=stop_btn_img,
                  borderwidth=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)


# membuat menu

my_menu = Menu(root)
root.config(menu=my_menu)

# Link


def link():
    pass


add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Tambah Lagu", menu=add_song_menu)
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Hapus Lagu", menu=remove_song_menu)
remove_song_menu.add_command(
    label="Hapus Lagu Dari Daftar", command=delete_song)
remove_song_menu.add_command(
    label="Hapus Semua Lagu Dari Daftar", command=delete_all_songs)
about_menu = Menu(my_menu)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Visit Here...!!!", command=link)
add_song_menu.add_command(label="Tambah Lagu Ke Playlist", command=add_song)
add_song_menu.add_command(
    label="Tambah Beberapa Lagu Ke Playlist", command=add_many_songs)


root.mainloop()
