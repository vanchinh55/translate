#from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from googletrans import Translator
import pyttsx3
import speech_recognition as sr

# Cửa sổ TK
root = Tk()
root.title("Google Translate!")
root.geometry("800x630")
root.iconbitmap("logotranslate.ico")
root.attributes('-topmost', False)

# Background
load = Image.open("vutru3.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

# Voice
chinh = pyttsx3.init()
voice = chinh.getProperty('voices')
# chinh.setProperty('voice', voice[1].id)

name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)
test = StringVar()

box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=20)

box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.pack(pady=50)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
	box.delete(1.0, END) ## Tkinter bắt đầu từ 1.0 chứ ko bắt đầu bằng 0/1
	box1.delete(1.0, END)


cb = StringVar()
# Combobox
combo = ttk.Combobox(root, textvariable=cb)
combo['value'] = ("Language Detection", "Viet Nam", "English", "Korean", "Japanese", "French")
combo.current(0)
combo.place(x=600, y=93)

cb1 = StringVar()
combo = ttk.Combobox(root, textvariable=cb1)
combo['value'] = ("Viet Nam", "English", "Korean", "Japanese", "French")
combo.current(1)
combo.place(x=600, y=360)

# Creat Microphone
def mic_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something")
        audio = r.listen(source)
        try:
            if cb.get() == "Viet Nam":
                a = r.recognize_google(audio, language="vi-VI")
                print(a)
            elif cb.get() == "English":
                a = r.recognize_google(audio, language="en-EN")
                print(a)
            elif cb.get() == "Korean":
                a = r.recognize_google(audio, language="ko-KO")
                print(a)
            elif cb.get() == "Japanese":
                a = r.recognize_google(audio, language="ja-JA")
                print(a)
            elif cb.get() == "French":
                a = r.recognize_google(audio, language="fr-FR")
                print(a)
            box.insert(END, a)
        except sr.UnknownValueError:
            print("could not understand")

# Voice processing
def combo_translate():
    global c
# Tiếng Việt
    if (cb.get() == "Viet Nam" or cb.get() == "Language Detection") and cb1.get() == "English":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="vi")
        b = t.translate(Input, dest="en")
        c = b.text
    elif (cb.get() == "Viet Nam" or cb.get() == "Language Detection") and cb1.get() == "Korean":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="vi")
        b = t.translate(Input, dest="ko")
        c = b.text
    elif (cb.get() == "Viet Nam" or cb.get() == "Language Detection") and cb1.get() == "Japanese":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="vi")
        b = t.translate(Input, dest="ja")
        c = b.text
    elif (cb.get() == "Viet Nam" or cb.get() == "Language Detection") and cb1.get() == "French":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="vi")
        b = t.translate(Input, dest="fr")
        c = b.text
    elif (cb.get() == "Viet Nam" or cb.get() == "Language Detection") and cb1.get() == "Viet Nam":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="vi")
        b = t.translate(Input, dest="vi")
        c = b.text
#Tiếng Anh
    elif cb.get() == "English" and cb1.get() == "Viet Nam":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="en")
        b = t.translate(Input, dest="vi")
        c = b.text
    elif cb.get() == "English" and cb1.get() == "English":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="en")
        b = t.translate(Input, dest="en")
        c = b.text
    elif cb.get() == "English" and cb1.get() == "Korean":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="en")
        b = t.translate(Input, dest="ko")
        c = b.text
    elif cb.get() == "English" and cb1.get() == "Japanese":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="en")
        b = t.translate(Input, dest="ja")
        c = b.text
    elif cb.get() == "English" and cb1.get() == "French":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="en")
        b = t.translate(Input, dest="fr")
        c = b.text
# Tiếng Hàn
    elif cb.get() == "Korean" and cb1.get() == "Viet Nam":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ko")
        b = t.translate(Input, dest="vi")
        c = b.text
    elif cb.get() == "Korean" and cb1.get() == "English":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ko")
        b = t.translate(Input, dest="en")
        c = b.text
    elif cb.get() == "Korean" and cb1.get() == "Korean":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ko")
        b = t.translate(Input, dest="ko")
        c = b.text
    elif cb.get() == "Korean" and cb1.get() == "Japanese":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ko")
        b = t.translate(Input, dest="ja")
        c = b.text
    elif cb.get() == "Korean" and cb1.get() == "French":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ko")
        b = t.translate(Input, dest="fr")
        c = b.text
# Tiếng Nhật
    elif cb.get() == "Japanese" and cb1.get() == "Viet Nam":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ja")
        b = t.translate(Input, dest="vi")
        c = b.text
    elif cb.get() == "Japanese" and cb1.get() == "English":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ja")
        b = t.translate(Input, dest="en")
        c = b.text
    elif cb.get() == "Japanese" and cb1.get() == "Korean":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ja")
        b = t.translate(Input, dest="ko")
        c = b.text
    elif cb.get() == "Japanese" and cb1.get() == "Japanese":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ja")
        b = t.translate(Input, dest="ja")
        c = b.text
    elif cb.get() == "Japanese" and cb1.get() == "French":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="ja")
        b = t.translate(Input, dest="fr")
        c = b.text
# Tiếng Pháp
    elif cb.get() == "French" and cb1.get() == "Viet Nam":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="fr")
        b = t.translate(Input, dest="vi")
        c = b.text
    elif cb.get() == "French" and cb1.get() == "English":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="fr")
        b = t.translate(Input, dest="en")
        c = b.text
    elif cb.get() == "French" and cb1.get() == "Korean":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="fr")
        b = t.translate(Input, dest="ko")
        c = b.text
    elif cb.get() == "French" and cb1.get() == "Japanese":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="fr")
        b = t.translate(Input, dest="ja")
        c = b.text
    elif cb.get() == "French" and cb1.get() == "French":
        Input = box.get(1.0, END)
        print(Input)
        t = Translator()
        a = t.translate(Input, src="fr")
        b = t.translate(Input, dest="fr")
        c = b.text
    print(c)
    box1.insert(END, c)

def speak():
    # Speak tiếng Việt
    if cb1.get() == "Viet Nam":
        id_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_AN"
        chinh.setProperty("voice", id_voice)

    # Speak tiếng Anh
    elif cb1.get() == "English":
        id_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        chinh.setProperty("voice", id_voice)

    # Speak tiếng Hàn
    elif cb1.get() == "Korean":
        id_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0"
        chinh.setProperty("voice", id_voice)

    # Speak tiếng Nhật
    elif cb1.get() == "Japanese":
        id_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0"
        chinh.setProperty("voice", id_voice)

    # Speak tiếng Pháp
    elif cb1.get() == "French":
        id_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
        chinh.setProperty("voice", id_voice)
    chinh.say(c)
    chinh.runAndWait()
c=""

# Messagebox
def quit_root():
    exit_root = messagebox.askyesno(title="Thông báo!", message="Bạn có muốn thoát chương trình không?")
    if exit_root:
        root.quit()

clear_button = Button(button_frame, text="Clear text", font=(("arial"), 10, "bold"), bg="#303030", fg="#7fff00", command=clear)
clear_button.place(x=230, y=310)

img_mic = PhotoImage(file=r'rsz_mic2.png')
photo = img_mic.subsample(3, 3)
mic_button = Button(button_frame, text='Voice', image=img_mic, compound=LEFT, font=(("arial"), 10, "bold"), bg="#C0C0C0", fg="#FFFF00", command=mic_text)
mic_button.place(x=230, y=257)

trans_button = Button(button_frame, text="Translate", font=(("arial"), 10, "bold"), bg="#303030", fg="#7fff00", command=combo_translate)
trans_button.place(x=340, y=310)

img_voice = PhotoImage(file=r'voice2.png')
photo1 = img_voice.subsample(3, 3)
voice_button = Button(button_frame, text="Voice", image=img_voice, compound=LEFT, font=(("arial"), 10, "bold"), bg="#303030", fg="#7fff00", command=speak)
voice_button.place(x=440, y=310)

exit_button = Button(root, text="EXIT", font=(("arial"), 10, "bold"),bg="#ff0000", fg="#ffff00", command=quit_root)
exit_button.place(x=530, y=310)

root.mainloop()