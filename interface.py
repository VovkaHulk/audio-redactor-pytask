from tkinter import *

import pydub
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

import main


def stop():
    pass


def get_segment_start():
    return int(fragment_to_edit_from.get()) * 1000


def get_segment_end():
    c = fragment_to_edit_to.get()
    if c == '10^00':
        return len(audio)
    else:
        return min(int(c) * 1000, int(audio.duration_seconds * 1000))


def CloseApp():
    root.destroy()
    print('На сегодня ты наредактировался, лох')


audio = pydub.AudioSegment.silent()
history_for = []
history_back = []
root = Tk()  # создаем корневой объект - окно
root.title(
    "Аудиоредактор от Владоса Темщика и Вовки ХаХалка")  # устанавливаем заголовок окна
root.geometry("800x600+200+200")  # устанавливаем размеры окна
root.resizable(False, False)
root.iconbitmap(default='penis.ico')
root.protocol('WM_DELETE_WINDOW', CloseApp)

input_file_entry = Entry(width=50)
input_file_entry.place(x=15, y=15)
input_file_entry.insert(0, 'Путь к файлу')


def LoadAudioFile():
    global audio
    # ВСТАВЬ СЮДА ХУЕТУ, ЧТОБЫ ФАЙЛ ГРУЗИЛО
    filepath = filedialog.askopenfilename()
    if filepath != "":
        text = filepath
        input_file_entry.delete("0", END)
        input_file_entry.insert("0", text)
        audio = main.open_audio(filepath)
    audio_image_panel.place(x=0, y=40)


def VolumeChanged(new_volume):
    global audio
    audio = main.change_volume(audio, new_volume, get_segment_start(),
                               get_segment_end())


def SpeedChanged(new_speed):
    global audio
    audio = main.change_volume(audio, new_speed, get_segment_start(),
                               get_segment_end())


def ReplaceSelectedFragment():
    global audio, history_for
    history_back.append(audio)
    history_for = []
    audio = audio[:get_segment_start()] + audio[get_segment_end():]


def ReturnBackward():
    global audio
    history_for.append(audio)
    if len(history_back):
        audio = history_back.pop()


def ReturnForward():
    global audio
    history_back.append(audio)
    if len(history_for):
        audio = history_for.pop()


def FadeInFragment():
    global audio, history_for
    history_back.append(audio)
    history_for = []
    audio = audio[:get_segment_start()] + \
            audio[get_segment_start():get_segment_end()] \
                .fade_in(int(float(fade_in_out_value.get()) * 1000)) + \
            audio[get_segment_end():]


def FadeOutFragment():
    global audio, history_for
    history_back.append(audio)
    history_for = []
    audio = audio[:get_segment_start()] + \
            audio[get_segment_start():get_segment_end()] \
                .fade_in(int(float(fade_in_out_value.get()) * 1000)) + \
            audio[get_segment_end():]


def play():
    main.play(audio)


def ExportFile():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = input_file_entry.get()
        audio.export(filepath, format='mp3')


def make_changes():
    global history_for
    history_back.append(audio)
    history_for = []
    SpeedChanged(float(speed_entry.get()))
    VolumeChanged(float(volume_entry.get()))


load_input_file_btn = Button(text='Загрузить', command=LoadAudioFile)
load_input_file_btn.place(x=330, y=12)

export_file_button = Button(text='Экспортировать', command=ExportFile)
export_file_button.place(x=695, y=12)

audio_image = ImageTk.PhotoImage(
    Image.open('dorojka1.png').resize((800, 100), Image.BILINEAR))
audio_image_panel = Label(root, image=audio_image)

volume = StringVar(value="0")
volume_label = Label(text='Изменить громкость')
volume_label.place(x=15, y=130)
volume_entry = Entry(width=10, textvariable=volume)
volume_entry.place(x=15, y=150)

speed = StringVar(value='1.0')
speed_lable = Label(text='Скорость')
speed_lable.place(x=100, y=130)
speed_entry = Entry(width=10, textvariable=speed)
speed_entry.place(x=100, y=150)

podtv_button = Button(text='Применить', command=make_changes)
podtv_button.place(x=40, y=180)

replace_button = Button(text='Вырезать кусок', command=ReplaceSelectedFragment)
replace_button.place(x=640, y=40)

return_backward_button = Button(text='<=', command=ReturnBackward)
return_backward_button.place(x=420, y=12)

return_forward_button = Button(text='=>', command=ReturnForward)
return_forward_button.place(x=460, y=12)

fragment_to_edit_lable = Label(text="Фрагмент:")
fragment_to_edit_lable.place(x=500, y=15)

fragment_to_edit_from = StringVar(value='0')
fragment_to_edit_from_entry = Entry(width=7,
                                    textvariable=fragment_to_edit_from)
fragment_to_edit_from_entry.place(x=565, y=15)

fragment_to_edit_to_lable = Label(text="-->")
fragment_to_edit_to_lable.place(x=610, y=15)

fragment_to_edit_to = StringVar(value='10^00')
fragment_to_edit_to_entry = Entry(width=7, textvariable=fragment_to_edit_to)
fragment_to_edit_to_entry.place(x=640, y=15)

fade_in_button = Button(text='fade in', command=FadeInFragment)
fade_in_button.place(x=200, y=145)

fade_out_button = Button(text='fade out', command=FadeOutFragment)
fade_out_button.place(x=250, y=145)

fade_in_out_value = IntVar(value='1.0')
fade_in_out_entry = Entry(width=10, textvariable=fade_in_out_value)
fade_in_out_entry.place(x=225, y=180)

play_button_image = PhotoImage(file='pngwing.com(3).png')
play_button = Button(root, image=play_button_image, command=play)
play_button.place(x=320, y=150)

stop_button_image = PhotoImage(file='channels4_profile.png')
stop_button = Button(root, image=stop_button_image, command=stop)
stop_button.place(x=360, y=150)

root.mainloop()

root.mainloop()
