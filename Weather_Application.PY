import time
from tkinter import*
from tkinter import messagebox
import tkinter as ttk
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests,json
import pytz
from PIL import ImageTk, Image
from plyer import notification
import datetime


w=Tk()
width_window=465 #427
height_window=250
screen_width=w.winfo_screenwidth()
screen_height=w.winfo_screenheight()
x=(screen_width/2)-(width_window/2)

y=(screen_height/2)-(height_window/2)
w.geometry("%dx%d+%d+%d"%(width_window,height_window,x,y))
w.configure(bg="light blue")
w.overrideredirect(1)# to hide title bar
def new_win():
    w.destroy()
    root=Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False, False)

    def signup():
        root.destroy()
        import Signuppage_final
        f = Tk()

    def signin():
        username = user.get()
        Password = password.get()
        a = open('user_name.txt', 'r')
        b = a.readline()
        flag = False
        flag1 = False
        while b:
            line = b.split()
            if username in line:
                flag = True
                b = a.readline().split()
                if Password in b:
                    flag1 = True
            b = a.readline()
        if flag == False:
            messagebox.showerror("ERROR", "Username not found, try logging in instead!")
        elif flag1 == False and flag == True:
            messagebox.showerror("ERROR", "Incorrect Password!")
        elif flag == True and flag1 == True:
            root.destroy()
            root1 = Tk()
            root1.title("Weather App")
            root1.geometry("900x500+200+100")
            x = datetime.datetime.now()
            y = x.hour
            if (y - 18) < 0:
                bg = Image.open("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\trial_bg(900x800).png")
            else:
                bg = Image.open("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\dark.png")

            root1.configure(background=bg)
            root1.resizable(False, False)



            def getWeather():
                try:
                    city=stay.get()
                    city = textfield.get()

                    geolocator = Nominatim(user_agent="geoapiExercises")
                    location = geolocator.geocode(city)
                    obj = TimezoneFinder()
                    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)


                    home = pytz.timezone(result)
                    local_time = datetime.now(home)
                    current_time = local_time.strftime("%I:%M %p")
                    clock.config(text=current_time)
                    name.config(text="CURRENT WEATHER")

                    # weather
                    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=6b3f2bd800a825cb7809e638908db708"

                    json_data = requests.get(api).json()
                    condition = json_data['weather'][0]['main']
                    description = json_data['weather'][0]['description']
                    temp = int(json_data['main']['temp'] - 273.15)
                    pressure = json_data['main']['pressure']
                    humidity = json_data['main']['humidity']
                    wind = json_data['wind']['speed']
                    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6b3f2bd800a825cb7809e638908db708"
                    weather_data=requests.get(api).json()
                    description = weather_data['weather'][0]['description']
                    word='sunny'
                    word1='rain'
                    word2='cold'
                    word3='fog'
                    word4='clear'
                    word5='cloud'
                    if word in description:
                        notification.notify(
                            title='Greetings From Cloud Study',
                            message='It looks like its sunny today. Do not forget to carry your umbrella!',
                            app_icon="sunny.ico",
                            timeout=10,
                            toast=False
                        )
                    if word1 in description:
                        notification.notify(
                            title='Greetings From Cloud Study',
                            message='It looks like it is raining today. Do not forget to wear your raincoat!',
                            app_icon="rain.ico",
                            timeout=10,
                            toast=False
                        )
                    if word2 in description:
                        notification.notify(
                            title='Greetings From Cloud Study',
                            message='It looks like it is cold today. Do not forget to wear your sweater!',
                            app_icon="rain.ico",
                            timeout=10,
                            toast=False
                        )
                    if word3 in description:
                        notification.notify(
                            title='Greetings From Cloud Study',
                            message='It looks like it is cold today. Do not forget to wear your sweater!',
                            app_icon="foggy.ico",
                            timeout=10,
                            toast=False
                        )
                    if word4 in description:
                        notification.notify(
                            title='Greetings From Cloud Study',
                            message='It looks like it is a perfect day. Do not forget to enjoy it!',
                            app_icon="clear.ico",
                            timeout=10,
                            toast=False
                        )
                    if word5 in description:
                        notification.notify(
                            title='Greetings From Cloud Study',
                            message='It looks like it is a cloudy day. Do not forget to enjoy it!',
                            app_icon="cloudy.ico",
                            timeout=10,
                            toast=False
                        )
                    if 'smoke' in description:
                         notification.notify(
                             title='Greetings From Cloud Study',
                             message='It looks like there is a lot of smoke. Do not forget to wear a mask!',
                             app_icon="foggy.ico",
                             timeout=10,
                             toast=False
                         )
                    t.config(text=(temp, "°"))
                    c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

                    w.config(text=wind)
                    h.config(text=humidity)
                    d.config(text=description)
                    p.config(text=pressure)

                except Exception as e:
                    messagebox.showerror("Weather App", "Invalid Entry!")


            # search box
            Search_image = PhotoImage(file="C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\searchbar.png")
            myimage = Label(image=Search_image)
            myimage.place(x=20, y=20)

            textfield = tk.Entry(root1, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
            textfield.place(x=50, y=40)
            textfield.focus()

            Search_icon = PhotoImage(file="C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\searchicon.png")
            myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
            myimage_icon.place(x=400, y=34)

            # logo
            logo_image = PhotoImage(file="C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\pic.png")
            logo = Label(image=logo_image)
            logo.place(x=150, y=100)

            # bottom box
            Frame_image = PhotoImage(file="C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\bluebox.png")
            frame_myimage = Label(image=Frame_image)
            frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

            # time
            name = Label(root1, font=("arial", 15, "bold"))
            name.place(x=30, y=100)
            clock = Label(root1, font=("Helvetica", 20))
            clock.place(x=30, y=130)

            # label
            label1 = Label(root1, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
            label1.place(x=120, y=400)

            label1 = Label(root1, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
            label1.place(x=250, y=400)

            label1 = Label(root1, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
            label1.place(x=430, y=400)

            label1 = Label(root1, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
            label1.place(x=650, y=400)

            t = Label(font=("arial", 70, "bold"), fg="#ee666d")
            t.place(x=400, y=150)
            c = Label(font=("arial", 15, "bold"))
            c.place(x=400, y=250)

            w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
            w.place(x=120, y=430)
            h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
            h.place(x=280, y=430)
            d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
            d.place(x=450, y=430)
            p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
            p.place(x=670, y=430)

            root1.mainloop()

        else:
            pass

    img = PhotoImage(file='C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\\l1.png')
    Label(root, image=img, bg='white').place(x=10, y=10)
    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=500, y=70)
    heading = Label(frame, text='SIGN IN', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ########-------------------------------------------------------------------------------------
    def on_enter(a):
        user.delete(0, 'end')

    def on_leave(a):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    Frame(frame, width=295, height=2, bg='blue').place(x=25, y=107)

    def on_enter(a):
        user.delete(0, 'end')

    def on_leave(a):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='blue', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
    user.place(x=50, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='blue').place(x=25, y=107)

    ########-------------------------------------------------------------------------------------
    def on_enter(a):
        password.delete(0, 'end')

    def on_leave(a):
        name = password.get()
        if name == '':
            user.insert(0, 'Password')

    password = Entry(frame, width=25, fg='blue', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
    password.place(x=50, y=150)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='blue').place(x=25, y=177)
    Button(frame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=signin).place(x=35,
                                                                                                              y=210)
    label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 10))
    label.place(x=55, y=245)
    sign_up = Button(frame, width=6, text="Sign Up", border=0, bg="white", cursor='hand2', fg="#57a1f8", command=signup)
    sign_up.place(x=201, y=247)

    root.mainloop()
Frame(w,width=427,height=250,bg="light blue").place(x=10,y=10)
img=PhotoImage(file='C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\MINIPROJECT\\logo.PNG')
Label(image=img,bg="white").place(x=0,y=0)
label=Label(w,text="Loading...",fg="black")
label.configure(font=("Calibri",18))
label.place(x=190,y=210)
w.after(3000,new_win)

w.mainloop()

