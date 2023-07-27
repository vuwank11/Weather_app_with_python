#Necessary imports
import json
import requests
from geopy.geocoders import Nominatim
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



try:
    #WEATHER APP CREATED BY BHUWAN KHATIWADA
    print("*********WEATHER APP**********")
    city=input("Enter the name of city: ")

    #Initializatiion of Nominatim API
    geolocator=Nominatim(user_agent="Weather_app")

    location=geolocator.geocode(city)

    latitude=location.latitude
    longitude=location.longitude

    print("Address: ",location.address)
    print(f"\nThe coordinates of the entered location are: {latitude},{ longitude}")

    url=f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&current_weather=true'

    response= requests.get(url)
    #print(response.text)

    # response.txt returns a string. Convert it into a dictionary.
    weather_dict=json.loads(response.text)

    #print(type(weather_dict))# of type dict
    #print(weather_dict)

    print("\nCurrent Temperature: ",weather_dict["current_weather"]["temperature"])
    print("Wind Speed: ",weather_dict["current_weather"]["windspeed"])
    print("Wind Direction: ",weather_dict["current_weather"]["winddirection"])
    print("Time: ",weather_dict["current_weather"]["time"])

    enter=input("\nDo yo want to see hourly temperature chart?{y/n): ")

    if(enter=="y"):
        #hourly temprature chart
        hour_df= pd.DataFrame(weather_dict["hourly"])
        hour_tail_df=hour_df.tail(24)


        #visualization

        sns.set_style("whitegrid")
        sns.set_context("paper")

        plt.figure().set_figwidth(10)
        ax=sns.lineplot(data=hour_tail_df, x="time",y="temperature_2m")
        plt.xticks(rotation="vertical")

        plt.xlabel("Time")
        plt.ylabel("Temprature in C")
        plt.title("Hourly Temperature Chart of Last 24 Hours.")

        plt.tight_layout()

        plt.show()

except Exception as e:
    print("Some error occured. Invalid input.\n",e)



