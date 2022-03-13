from tkinter import *
import requests
import time
from datetime import datetime
# CONFIG

root = Tk()
root["bg"] = "#1a1a1a"  
root.title("Weather")
root.geometry("500x700")
root.resizable(width=False,height=False)
root.wm_attributes("-alpha",1.0)

# DATA INPUT
def search_click():
    city = input_city.get()
    key = 'e5c66ebe5f53b281dbbf1c6dee0e4bd2'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'appid':key,'q':city, 'units':'metric'}
    result= requests.get(url,params=params)
    weather = result.json()
    json_data = requests.get(url,params=params).json()

    info_weather['text'] = int(json_data['main']['temp'])
    info_weather2['text'] = json_data['main']['pressure']
    info_weather3['text'] = json_data['main']['humidity']
    info_weather4['text'] = json_data['wind']['speed']
    info_weather5['text'] = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']+10800))
    info_weather6['text'] = datetime.fromtimestamp((json_data['sys']['sunset'])) 
    info_weather7['text'] = json_data['weather'][0]['description']
    info_weather8['text'] = json_data['visibility']


    print(weather)


search = Button(root,text="Узнать погоду", bg="#323232", command=search_click) 
search.pack()
search.place(relx= 0.67, rely= 0.05, relheight=0.07, relwidth=0.3)

input_city = Entry(root,bg = "#323232") 
input_city.pack()
input_city.place(relx=0.05,rely=0.05, relheight=0.07, relwidth=0.65)

# DATA OUTPUT
info = Frame(root,bg="#323232") 
info.pack()
info.place(relx=0.05,rely=0.15,relheight=0.82,relwidth=0.92)

info_weather = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10)) 
info_weather.pack()
info_weather.place(relx=0.02,rely=0.014,relwidth=0.5,relheight=0.05)

info_weather2 = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10)) 
info_weather2.pack()
info_weather2.place(relx=0.02,rely=0.074,relwidth=0.5,relheight=0.05)

info_weather3 = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10)) 
info_weather3.pack()
info_weather3.place(relx=0.02,rely=0.134,relwidth=0.5,relheight=0.05)

info_weather4 = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10)) 
info_weather4.pack()
info_weather4.place(relx=0.02,rely=0.194,relwidth=0.5,relheight=0.05)

info_weather5 = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10)) 
info_weather5.pack()
info_weather5.place(relx=0.02,rely=0.254,relwidth=0.5,relheight=0.05)

info_weather6 = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10))
info_weather6.pack()
info_weather6.place(relx=0.02,rely=0.314,relwidth=0.5,relheight=0.05)

info_weather7 = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10)) 
info_weather7.pack()
info_weather7.place(relx=0.02,rely=0.374,relwidth=0.5,relheight=0.05)

info_weather8 = Label(info,text ="--:--" ,bg='#555555',font =("Arial", 10)) 
info_weather8.pack()
info_weather8.place(relx=0.02,rely=0.434,relwidth=0.5,relheight=0.05)


# DATA VIEW

view_weather = Label(info,text ="temperature" ,bg='#555555',font =("Arial", 10)) 
view_weather.pack()
view_weather.place(relx=0.48,rely=0.014,relwidth=0.5,relheight=0.05)

view_weather2 = Label(info,text ="pressure" ,bg='#555555',font =("Arial", 10)) 
view_weather2.pack()
view_weather2.place(relx=0.48,rely=0.074,relwidth=0.5,relheight=0.05)

view_weather3 = Label(info,text ="humidity (%)" ,bg='#555555',font =("Arial", 10)) 
view_weather3.pack()
view_weather3.place(relx=0.48,rely=0.134,relwidth=0.5,relheight=0.05)

view_weather4 = Label(info,text ="wind speed (M/S)" ,bg='#555555',font =("Arial", 10)) 
view_weather4.pack()
view_weather4.place(relx=0.48,rely=0.194,relwidth=0.5,relheight=0.05)

view_weather5 = Label(info,text ="sunrise time" ,bg='#555555',font =("Arial", 10)) 
view_weather5.pack()
view_weather5.place(relx=0.48,rely=0.254,relwidth=0.5,relheight=0.05)

view_weather6 = Label(info,text ="sunset time (PM)" ,bg='#555555',font =("Arial", 10)) 
view_weather6.pack()
view_weather6.place(relx=0.48,rely=0.314,relwidth=0.5,relheight=0.05)

view_weather7 = Label(info,text ="clouds info" ,bg='#555555',font =("Arial", 10)) 
view_weather7.pack()
view_weather7.place(relx=0.48,rely=0.374,relwidth=0.5,relheight=0.05)

view_weather8 = Label(info,text ="visibility (M)" ,bg='#555555',font =("Arial", 10)) 
view_weather8.pack()
view_weather8.place(relx=0.48,rely=0.434,relwidth=0.5,relheight=0.05)

root.mainloop()
