import os
import tkinter as tk
import requests
import datetime as dt


#function to get all weather data using API
def get_Weather(app):
    API_KEY = os.environ.get("API_KEY")
    URL = "https://api.openweathermap.org/data/2.5/weather"
    city = city_input.get()
    response = requests.get(f'{URL}?q={city}&appid={API_KEY}')
    # check whether user put wrong name
    if response.status_code != 200:
        final_info = "Wrong city name, please, enter again"
        label.config(text=final_info)
    else:
        weather_data = response.json()
        condition = weather_data["weather"][0]["description"]
        # temperature should to be converted from Kelvin to Celsius
        temperature = int(weather_data["main"]["temp"] - 273.15)
        humidity = weather_data["main"]["humidity"]
        wind = weather_data["wind"]["speed"]

        # display final weather data
        data1 = str(condition).capitalize() + "\n" + "\n" + str(temperature) + "°C"
        data2 = "Humidity: " + str(humidity) + "\n" + "\n" + "Wind: " + str(wind) + " m/s"

        label.config(text=data1 + "\n" + "\n" + data2)



# set app interface
app = tk.Tk()
app.geometry("650x500")
app.title(" Simple Weather App")
# backgroud color
app['bg'] = '#36684b'

# set a frame to input a city name
frm = tk.Frame(app, bg='#9ac6ad', bd=5)
frm.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# search field
label0 = tk.Label(frm, text="Type a city name", font=14)
label0.place(relx=0.4, relheight=1, relwidth=0.7)

#text field to get a city name from the user
city_input = tk.Entry(frm, font=40)
city_input.place(relwidth=0.5, relheight=1)
city_input.focus()
city_input.bind("<Return>", get_Weather)

# set a frame for weather data
data_frame = tk.Frame(app, bg='#9ac6ad', bd=5)
data_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Create an instance of datetime module
date=dt.datetime.now()
# Format the date
d1 = f"{date:%a, %b %d %Y}"
# Display the date in aa label widget
label_time =tk.Label(app, text="Today: " + d1, font=("Nunito", 18))

label_time.pack()


# set label for output data
label = tk.Label(data_frame, font=("bold", 18))
label.place(relwidth=1, relheight=1)

app.mainloop()

