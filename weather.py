import requests
from tkinter import *



def weather():
	city=city_listbox.get()
	url="https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city)
	res=requests.get(url)
	output=res.json()

	weather_status=output['weather'][0]['description']
	temprature=output['main']['temp']
	humidity=output['main']['humidity']
	wind_speed=output['wind']['speed']

	weather_status_label.configure(text="weather status : "+ weather_status,fg="#fa0505")
	temprature_label.configure(text="temprature : "+ str(temprature))
	humidity_label.configure(text="Humidity : "+ str(humidity))
	wind_speed_label.configure(text="wind speed  : "+ str(wind_speed))
	





project=Tk()
project.title("Weather API Project")
project.geometry("400x350")

city_name_list=["Nairobi","Kisumu","Mombasa","Voi","Taita","Malindi","Lamu","Kericho","Eldoret","Siaya","Kiambu","Busia"]

city_listbox=StringVar(project)
city_listbox.set("select the city")
option=OptionMenu(project,city_listbox,*city_name_list)
option.grid(row=2,column=2,padx=150,pady=10)

button=Button(project,text="Display Weather",width=15,fg="#060f75",bg="green",command=weather)
button.grid(row=5,column=2,padx=150)


weather_status_label=Label(project,font=("times",10,"bold"),fg="#949431",bg="#03183b")
weather_status_label.grid(row=10,column=2)

temprature_label=Label(project,font=("times",10,"bold"),fg="#319494",bg="#03183b")
temprature_label.grid(row=12,column=2)

humidity_label=Label(project,font=("times",10,"bold"),fg="#ab878d",bg="#03183b")
humidity_label.grid(row=14,column=2)

wind_speed_label=Label(project,font=("times",10,"bold"),fg="#0bbda8",bg="#03183b")
wind_speed_label.grid(row=16,column=2)

project.mainloop()
