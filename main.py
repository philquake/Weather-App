from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# The code is creating the main window for the weather app.
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


# The function `getWeather()` takes a city as input, uses geolocation to find the longitude and
# latitude of the city, and then uses a timezone finder to determine the timezone of the city.

def getWeather():
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

t = Label(font=("arial",70,"bold"), fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial",15,"bold"))
c.place(x=400, y=250)

w = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
w.place(x=120,y=430)

w = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
w.place(x=280,y=430)

w = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
w.place(x=450,y=430)

w = Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
w.place(x=670,y=430)


root.mainloop()
