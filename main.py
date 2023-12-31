from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from dotenv import load_dotenv
import os 

# The function `configure()` loads the environment variables from a .env file.
def configure():
    load_dotenv()

# The code is creating the main window for the weather app.
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
# `root.after_idle(configure)` is scheduling the `configure()` function to be called after all pending
# events have been processed by the main event loop. This ensures that the environment variables are
# loaded from the .env file before the rest of the code is executed.
root.after_idle(configure) 


# The function `getWeather()` retrieves weather information for a given city and displays it on a GUI.
def getWeather():
    try:
        city=textfield.get()

        geolocator = Nominatim(user_agent="Weather App")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text = current_time)
        name.config(text = "CURRENT WEATHER")


        #weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&&appid={os.getenv('api_key')}"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        lab_temp.config(text = (temp, "°"))
        lab_con.config(text = (condition, "|", "FEELS", "LIKE", temp, "°" ))

        lab_wind.config(text = wind)
        lab_hum.config(text = humidity)
        lab_desc.config(text = description)
        lab_pres.config(text = pressure)
    
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!")



# The code is creating an image object `Search_image` by loading the image file `search.png`.
Search_image = PhotoImage(file='./img/search.png')  
myimage = Label(image=Search_image)
myimage.place(x=20,y=20)

# The code is creating a text entry field widget using the `Entry` class from the `tkinter` module.
textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

# The code is creating a button widget `myimage_icon` with an image `Search_icon`.
Search_icon = PhotoImage(file="./img/search_icon.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040", command = getWeather)
myimage_icon.place(x=400,y=34)

# The code is creating an image object `Logo_image` by loading the image file `logo.png` from the `img` folder.
#logo
Logo_image = PhotoImage(file="./img/logo.png")
logo = Label(image=Logo_image)
logo.place(x=150,y=100)


# The code is creating an image object `Frame_image` by loading the image file `box.png` from the
#`img` folder. Then, it creates a label widget `frame_myimage` with the image `Frame_image`. Finally,
# it packs the label widget with some padding and places it at the bottom of the main window.
#bottom box
Frame_image = PhotoImage(file="./img/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
lab_wind = Label(root,text="WIND", font=("Helvetica", 15, 'bold'), fg="white",bg="#1ab5ef")
lab_wind.place(x=120,y=400)

lab_hum = Label(root,text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white",bg="#1ab5ef")
lab_hum.place(x=250,y=400)

lab_desc = Label(root,text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white",bg="#1ab5ef")
lab_desc.place(x=430,y=400)

lab_pres = Label(root,text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white",bg="#1ab5ef")
lab_pres.place(x=650,y=400)

lab_temp = Label(font=("arial",70,"bold"), fg="#ee666d")
lab_temp.place(x=400,y=150)
lab_con = Label(font=("arial",15,"bold"))
lab_con.place(x=400, y=250)

lab_wind = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
lab_wind.place(x=120,y=430)

lab_hum = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
lab_hum.place(x=280,y=430)

lab_desc = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
lab_desc.place(x=450,y=430)

lab_pres = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
lab_pres.place(x=670,y=430)


# `root.mainloop()` is a method that starts the main event loop of the tkinter application. It
# continuously listens for events such as button clicks, mouse movements, and keyboard inputs, and
# updates the GUI accordingly. It keeps the application running until the user closes the window or
# exits the program.
root.mainloop()
