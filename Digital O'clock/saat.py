# Imports
from tkinter import *
from time import *
from time import sleep,strftime
from PIL import Image, ImageTk
from datetime import datetime
import pytz
#----------------------------------------------------->
# Variables

running = False
elapsed_time = 0
after_id = None 
active_language = "en"
stopwatch_start_button = None
stopwatch_stop_button = None
stop_watch_reset_button = None
increase_hour_button = None
decrease_hour_button = None
increase_minute_button = None
decrease_minute_button = None
increase_second_button = None
decrease_second_button = None
countdown_start_button = None
countdown_stop_button = None
countdown_reset_button = None

#----------------------------------------------------->
# Main Menu
main = Tk()
main.resizable(False, False)
main.title("Dijital Saat")
main.geometry("414x736")

first_page = Image.open(r"C:\Desktop\Digital O'clock")
first_page = first_page.resize((414, 736))  
main_menu_background = ImageTk.PhotoImage(first_page)

arka_plan_label = Label(main, image=main_menu_background)
arka_plan_label.place(relwidth=1, relheight=1)

label_x = 100  
label_y = 100  
label_width = 200
label_height = 50
section = first_page.crop((label_x, label_y, label_x + label_width, label_y + label_height))
section_image = ImageTk.PhotoImage(section)

language_choose = Label(main, text="Choose Your Language", font=("Arial", 14), fg="white", image=section_image, compound="center")
language_choose.place(relx=0.25, rely=0.23)
language_choose.image = section_image

#----------------------------------------------------->
# Dictionary
def change_language(selected_language):
    global language
    if selected_language == "en":
        language = {
        "choosing_language": "Select Language",
        "stopwatch": "Stopwatch",
        "countdown": "Timer",
        "o'clock": "Digital Clock",
        "go_back": "Back",
        "baslat": "Start ▶️",
        "dur": "Stop 🔴",
        "reset": "Reset",
        "saat_arttir": "Hour ↑",
        "saat_eksilt": "Hour ↓",
        "dakika_arttır": "Minute ↑",
        "dakika_azalt": "Minute ↓",
        "saniye_arttir": "Second ↑",
        "saniye_eksillt": "Second ↓",
        "turkey": "Turkey",
        "chicago": "Chicago",
        "new_york": "New York",
        "london": "London"
        }
    elif selected_language == "tr":
        language = {
        "dil_secimi": "Dil Seçimi Yapınız",
        "kronometre": "Kronometre",
        "sayac": "Sayaç",
        "saat": "Dijital Saat",
        "geri_don": "Geri Dön",
        "baslat": "Başlat ▶️",
        "dur": "Dur 🔴",
        "reset": "Sıfırla",                
        "saat_arttir": "Saat ↑",
        "saat_eksilt": "Saat ↓",
        "dakika_arttır": "Dakika ↑",
        "dakika_azalt": "Dakika ↓",
        "saniye_arttir": "Saniye ↑",
        "saniye_eksillt": "Saniye ↓",
        "turkey": "Türkiye",
        "chicago": "Chicago",
        "new_york": "New York",
        "london": "London"
        }

def update_language():
    try:
        increase_hour_button.config(text=language["increase_hour"])
        decrease_hour_button.config(text=language["decrease_hour"])
        increase_minute_button.config(text=language["increase_minute"])
        decrease_minute_button.config(text=language["decrease_minute"])
        increase_second_button.config(text=language["increase_second"])
        decrease_second_button.config(text=language["decrease_second"])
        countdown_start_button.config(text=language["countdown_start"])
        countdown_stop_button.config(text=language["countdown_stop"])
        countdown_reset_button.config(text=language["countdown_reset"])
    except:
        pass

# === Flag Buttons ===
tr_flag = ImageTk.PhotoImage(Image.open((r"C:\Users\Monster\Desktop\saatuygulamaflnfilan\background\turk.png")).resize((40, 25)))
usa_flag = ImageTk.PhotoImage(Image.open((r"C:\Users\Monster\Desktop\saatuygulamaflnfilan\background\usa.png")).resize((40, 25)))

btn_tr = Button(main, image=tr_flag, command=lambda: change_language("tr"))
btn_tr.image = tr_flag
btn_tr.place(relx=0.4, rely=0.32)

btn_en = Button(main, image=usa_flag, command=lambda: change_language("en"))
btn_en.image = usa_flag
btn_en.place(relx=0.5, rely=0.32)

#----------------------------------------------------->

def update_time(timezone, label):
    tz = pytz.timezone(timezone)
    time = datetime.now(tz).strftime("%H:%M:%S")
    label.config(text=f"{time}")
    label.after(1000, update_time, timezone, label)  # Update the clock per second

def time(timezone="Europe/Istanbul"):
    tz = pytz.timezone(timezone)
    ongoing_time = datetime.now(tz).strftime("%H:%M:%S")
    label.config(text=ongoing_time)
    label.after_id = label.after(1000, time, timezone)

#   === Digital O'clock ===
def oclock():   
    # Frame
    oclock_page = Frame(main, bg="white")
    oclock_page.place(relheight=1, relwidth=1)

    # O'clock Page Image
    oclock_image = Image.open(r"C:\Users\Monster\Desktop\saatuygulamaflnfilan\background\oclock_image.jpg")
    oclock_image = oclock_image.resize((414, 736))
    oclock_image_background = ImageTk.PhotoImage(oclock_image)

    # Background Label
    oclock_background_label = Label(oclock_page, image=oclock_image_background)
    oclock_background_label.image = oclock_image_background
    oclock_background_label.place(relwidth=1, relheight=1)

    # Background Label Section
    label_x = 120  
    label_y = 300  
    label_width = 200
    label_height = 50

    section = oclock_image.crop((label_x, label_y, label_x + label_width, label_y + label_height))
    section_image = ImageTk.PhotoImage(section)

    global label
    label = Label(oclock_page, text="", font=("Arial", 40), fg="white", image=section_image, compound="center")
    label.image = section_image
    label.place(relx=0.5, rely=0.5, anchor="center")

    # First Time
    time("Europe/Istanbul")


    def set_timezone(timezone):
        if hasattr(label, "after_id"):
            label.after_cancel(label.after_id)
        time(timezone)

    # City's O'clocks
    turkey_button = Button(oclock_page, text="Türkiye", font=("Helvetica", 10), command=lambda: set_timezone("Europe/Istanbul"))
    turkey_button.place(relx=0.2, rely=0.8)

    chicago_button = Button(oclock_page, text="Chicago", font=("Helvetica", 10), command=lambda: set_timezone("America/Chicago"))
    chicago_button.place(relx=0.4, rely=0.8)

    new_york_button = Button(oclock_page, text="New York", font=("Helvetica", 10), command=lambda: set_timezone("America/New_York"))
    new_york_button.place(relx=0.6, rely=0.8)

    london_button = Button(oclock_page, text="London", font=("Helvetica", 10), command=lambda: set_timezone("Europe/London"))
    london_button.place(relx=0.8, rely=0.8)

    # Go Back Button
    def go_back():
        oclock_page.destroy()

    go_backbutton = Button(oclock_page, text="Go Back", command=go_back)
    go_backbutton.place(relx=0.02, rely=0.01)
#-----------------------------------------------------
#   === Stopwatch Page ===
def stopwatch():
    global running, elapsed_time, after_id

    stopwatch_page = Frame(main, bg="white")
    stopwatch_page.place(relwidth=1, relheight=1)

    stopwatch_image = Image.open(r"C:\Users\Monster\Desktop\saatuygulamaflnfilan\background\stopwatch_image.jpg")
    stopwatch_image = stopwatch_image.resize((414, 736))
    stopwatch_image_background = ImageTk.PhotoImage(stopwatch_image)

    background_label = Label(stopwatch_page, image=stopwatch_image_background)
    background_label.image = stopwatch_image_background
    background_label.place(relwidth=1, relheight=1)

    label_x = 100  
    label_y = 100 
    label_width = 200
    label_height = 50

    section = stopwatch_image.crop((label_x, label_y, label_x + label_width, label_y + label_height))
    section_image = ImageTk.PhotoImage(section)

    global stopwatch_label
    stopwatch_label = Label(stopwatch_page,text="00:00:00",fg="white",image=section_image,compound="center",font=("Arial", 30),borderwidth=0,highlightthickness=0)
    stopwatch_label.image = section_image
    stopwatch_label.pack(pady=50)

    # Stopwatch Start
    def stopwatch_start():
        global running, after_id
        if not running:
            running = True
            stopwatch_update()

    # Stopwatch Stop
    def stopwatch_stop():
        global running, after_id
        running = False
        if after_id:
            stopwatch_page.after_cancel(after_id)
            after_id = None

    # Stopwatch Reset
    def stopwatch_reset():
        global running, elapsed_time, after_id
        stopwatch_stop()
        elapsed_time = 0
        stopwatch_label.config(text="00:00:00")

    # Stopwatch Update
    def stopwatch_update():
        global elapsed_time, running, after_id
        if running:
            elapsed_time += 1  
            hour = elapsed_time // 3600
            minute = (elapsed_time % 3600) // 60
            second = elapsed_time % 60
            stopwatch_label.config(text=f"{hour:02}:{minute:02}:{second:02}")
            after_id = stopwatch_page.after(1000, stopwatch_update)

    # Buttons
    stopwatch_start_button = Button(stopwatch_page, text="Start ▶️", command=stopwatch_start)
    stopwatch_start_button.pack(pady=10)

    stopwatch_stop_button = Button(stopwatch_page, text="Stop 🔴", command=stopwatch_stop)
    stopwatch_stop_button.pack(pady=10)

    stopwatch_reset_button = Button(stopwatch_page, text="Reset 🎬", command=stopwatch_reset)
    stopwatch_reset_button.pack(pady=10)

    # Go Back Button
    def go_back():
        stopwatch_stop()
        stopwatch_page.destroy()

    go_backbutton = Button(stopwatch_page, text="Go Back", command=go_back)
    go_backbutton.place(relx=0.02, rely=0.01)
#----------------------------------------------------->
#   === Timer Function ===
def countdown():
    timer = None
    countdown_page = Frame(main, bg="white")
    countdown_page.place(relheight=1, relwidth=1)

    countdown_image = Image.open(r"C:\Users\Monster\Desktop\saatuygulamaflnfilan\background\countdown_image.jpg")
    countdown_image = countdown_image.resize((414, 736))
    countdown_image_background = ImageTk.PhotoImage(countdown_image)

    background_label = Label(countdown_page, image=countdown_image_background)
    background_label.image = countdown_image_background
    background_label.place(relwidth=1, relheight=1)

    label_x = 100  
    label_y = 100  
    label_width = 200
    label_height = 50

    section = countdown_image.crop((label_x, label_y, label_x + label_width, label_y + label_height))
    section_image = ImageTk.PhotoImage(section)

    hour = 0
    minute = 0
    second = 0

    oclock_text = StringVar()
    oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    countdown_label = Label(countdown_page, textvariable=oclock_text, font=("Arial", 38), bg="white", fg="white")
    countdown_label.place(rely=0.3, relx=0.5, anchor="center")

    countdown_label = Label(countdown_page, textvariable=oclock_text, font=("Arial", 38), image=section_image, compound="center", fg="gray")
    countdown_label.image = section_image  
    countdown_label.place(rely=0.3, relx=0.5, anchor="center")

    # Functions
    def increase_hour():
        nonlocal hour
        hour = (hour + 1) % 24
        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    def decrease_hour():
        nonlocal hour
        hour = (hour - 1) % 24
        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    def increase_minute():
        nonlocal minute
        minute += 1
        if minute >= 60:
            minute = 0
            increase_hour()
        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    def decrease_minute():
        nonlocal minute
        minute -= 1
        if minute < 0:
            minute = 59
            decrease_hour()
        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    def increase_second():
        nonlocal second
        second += 1
        if second >= 60:
            second = 0
            increase_minute()
        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    def decrease_second():
        nonlocal second
        second -= 1
        if second < 0:
            second = 59
            decrease_minute()
        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    def count_down():
        nonlocal hour, minute, second, timer

        if hour == 0 and minute == 0 and second == 0:
            return

        if second == 0:
            second = 59
            if minute == 0:
                minute = 59
                if hour > 0:
                    hour -= 1
            else:
                minute -= 1
        else:
            second -= 1

        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")
        timer = countdown_page.after(1000, count_down)

    def start():
        nonlocal timer
        if timer is None:
            count_down()

    def stop():
        nonlocal timer
        if timer is not None:
            countdown_page.after_cancel(timer)
            timer = None
    
    def reset():
        nonlocal hour, minute, second, timer
        if timer is not None:
            countdown_page.after_cancel(timer)
            timer = None
        hour = 0
        minute = 0
        second = 0
        oclock_text.set(f"{hour:02}:{minute:02}:{second:02}")

    # Buttons
    increase_hour_button = Button(countdown_page, text="Hour ↑", command=increase_hour).place(relx=0.25, rely=0.15)
    decrease_hour_button = Button(countdown_page, text="Hour ↓", command=decrease_hour).place(relx=0.25, rely=0.4)

    increase_minute_button = Button(countdown_page, text="Minute ↑", command=increase_minute).place(relx=0.45, rely=0.15)
    decrease_minute_button = Button(countdown_page, text="Dakika ↓", command=decrease_minute).place(relx=0.45, rely=0.4)

    increase_second_button = Button(countdown_page, text="Second ↑", command=increase_second).place(relx=0.65, rely=0.15)
    decrease_second_button = Button(countdown_page, text="Second ↓", command=decrease_second).place(relx=0.65, rely=0.4)

    countdown_start_button = Button(countdown_page,text="Start ▶️ ",command=start,).place(relx=0.2, rely=0.53)
    countdown_stop_button = Button(countdown_page,text="Stop 🔴",command=stop, ).place(relx=0.41,rely=0.53)
    countdown_reset_button = Button(countdown_page,text="Reset 🎬",command=reset,).place(relx=0.63,rely=0.53)

    def go_back():
        countdown_page.destroy()

    go_back_button = Button(countdown_page, text="Go Back", command=go_back)
    go_back_button.place(relx=0.02, rely=0.01)
#----------------------------------------------------->

#--- Buttons In Main Menu ---
# #Stopwatch Button
stopwatch_button = Button(main, text="Stopwatch", command=stopwatch)
stopwatch_button.place(relx=0.25, rely=0.013)

#Digital O'clock Button
oclock_button = Button(main,text="Digital O'clock", command=oclock)
oclock_button.place(relx=0.6,rely=0.013)

#Countdown Button
timer_button = Button(main,text="Countdown", command=countdown)
timer_button.place(relx=0.42,rely=0.013)
#----------------------------------------------------->



update_language()
mainloop()