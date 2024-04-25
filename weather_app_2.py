#PYTHON PROGRAMMING INTERNSHIP
#PROJECT 4 - BASIC WEATHER APP
#NAME: SEJAL DAROLIYA

#Importing the required modules and files
import requests
import json

# Function: get_data() - extracts the weather details for the required city using weather API
def get_data(api_key, area):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q' : area,
        'units' : 'metric',
        'appid' : api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Unable to fetch weather data.")

#Function : display() - Displays the weather details for the required city
def display(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        conditions = weather_data['weather'][0]['description']
        pressure = weather_data['main']['pressure']
        wind = (weather_data['wind']['speed']) * 3.6
        cloudy = weather_data['clouds']['all']

        print(f"Temperature: {temperature}C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure}hPa")
        print(f"Wind:"  + "{:.2f}".format(wind) + "Km/h")
        print(f"Clouds: {cloudy}%")
        print(f"Weather conditions: {conditions}")
    else:
        print("unable to fetch weather data.")
    print("Thank You!!")

#Runs the program
if __name__ == '__main__':
    api_key = "fc875a13b86b00af11e9f5a8d7156cc2"
    print("Welcome to the weather forecast!!")
    area = input('Enter the city or ZIP code: ')
    print("The weather report is: ")

    weather_data = get_data(api_key, area)
    if weather_data:
        display(weather_data)