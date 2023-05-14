from tkinter import *
from pydub.playback import play
import pydub
from PIL import Image
from PIL import ImageTk
import main

audio = pydub.AudioSegment.silent()
s, f = 0, 0

def CloseApp():
    root.destroy()
    print('На сегодня ты наредактировался, лох')


def LoadAudioFile():
    global audio
    # ВСТАВЬ СЮДА ХУЕТУ, ЧТОБЫ ФАЙЛ ГРУЗИЛО
    route = input_file_entry.get()
    audio = main.open_audio(route)
    print('у тебя файл не грузит, дебила кусок')
    audio_image_panel.place(x=0, y=40)


def VolumeChanged(new_volume):
    global audio
    print('У тебя громкость не меняется, дебила запчасть')
    audio = main.change_volume(audio, new_volume, s, f)


def SpeedChanged(new_speed):
    global audio
    print('У тебя скорость не меняется, ебала')
    audio = main.change_speed(audio, int(new_speed)/100, s, f)


def ReplaceSelectedFragment():
    global s, f
    s = 42
    print('Еблан, у тебя фрагмент не удаляется!!!!ДЕБИЛОЙД')


def OpenReplaceWindow():
    replace_fragment_window = Tk()
    replace_fragment_window.title('Выбор фрагмента')
    replace_fragment_window.geometry('300x200')

    text_lable = Label(replace_fragment_window, text='Выберите фрагмент')
    text_lable.place(x=90, y=15)

    from_entry = Entry(replace_fragment_window, width=10)
    from_entry.place(x=50, y=50)
    from_entry.insert(0, 'От ')

    lable_from = Label(replace_fragment_window, text='->')
    lable_from.place(x=120, y=50)

    to_entry = Entry(replace_fragment_window, width=10)
    to_entry.place(x=150, y=50)
    to_entry.insert(0, 'До ')

    confirm_button = Button(replace_fragment_window, text='Confirm',
                            command=ReplaceSelectedFragment)
    confirm_button.place(x=120, y=100)


def ReturnBackward():
    print('Долбоклюй, у тебя не возвращает изменения')


def ReturnForward():
    print('Совсем ящер? Еще и вперед не возвращает')


root = Tk()  # создаем корневой объект - окно
root.title(
    "Аудиоредактор от Владоса Темщика и Вовки ХаХалка")  # устанавливаем заголовок окна
root.geometry("800x600+200+200")  # устанавливаем размеры окна
root.resizable(False, False)
root.iconbitmap(default='penis.ico')
root.protocol('WM_DELETE_WINDOW', CloseApp)

input_file_entry = Entry(width=50)
input_file_entry.place(x=15, y=15)
input_file_entry.insert(0, 'Введите путь к файлу')

load_input_file_btn = Button(text='Загрузить', command=LoadAudioFile)
load_input_file_btn.place(x=330, y=12)

audio_image = ImageTk.PhotoImage(
    Image.open('dorojka1.png').resize((800, 100), Image.ANTIALIAS))
audio_image_panel = Label(root, image=audio_image)

volume = IntVar(value=50)
volume_label = Label(text='Громкость')
volume_label.place(x=15, y=130)
volume_scale = Scale(orient=VERTICAL, length=200, from_=100.0, to=0.0,
                     variable=volume, command=VolumeChanged)
volume_scale.place(x=15, y=150)

speed = IntVar(value=100)
speed_lable = Label(text='Скорость')
speed_lable.place(x=100, y=130)
speed_scale = Scale(orient=VERTICAL, length=200, from_=200, to=1,
                    variable=speed, command=SpeedChanged)
speed_scale.place(x=100, y=150)

replace_button = Button(text='Вырезать кусок', command=OpenReplaceWindow)
replace_button.place(x=40, y=370)

return_backward_button = Button(text='<=', command=ReturnBackward)
return_backward_button.place(x=500, y=15)

return_forward_button = Button(text='=>', command=ReturnForward)
return_forward_button.place(x=540, y=15)

root.mainloop()
