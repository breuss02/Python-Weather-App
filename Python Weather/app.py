import requests
import os
import pyfiglet

api_key = 'YOUR_API_KEY_HERE'

weather = ""
temp = 0
pressure = 0
humidity = 0
high = 0
low = 0
user_input_city = ""

def menu_func():
    print("-------------------------------------------------------")
    print("**MENU**")
    print("-------------------------------------------------------")
    print()
    print("1: Request Data For New City")
    print("-------------------------------------------------------")
    print()
    print("2: Display Current City's Pressure")
    print("-------------------------------------------------------")
    print()
    print("3: Display Current City's Humidity")
    print("-------------------------------------------------------")
    print()
    print("4: Display Current City's High and Low Temps")
    print("-------------------------------------------------------")
    print()
    print("5: Exit")
    print("-------------------------------------------------------")
    print()
    
    choice = input("Enter Action Number: ")
    converted_choice = int(choice)
   
    os.system('cls')
    
    if converted_choice == 1:
        os.system('cls')
        city_func()
        menu_func()
    elif converted_choice == 2:
        os.system('cls')
        pressure_func(user_input_city, pressure)
        input("Press any key to continue")
        os.system('cls')
        menu_func()
    elif converted_choice == 3:
        os.system('cls')
        humidity_func(user_input_city, humidity)
        input("Press any key to continue")
        os.system('cls')
        menu_func()
    elif converted_choice == 4:
        os.system('cls')
        extrema_func(user_input_city, high, low)
        input("Press any key to continue")
        os.system('cls')
        menu_func()
    elif converted_choice == 5:
       quit()
    elif converted_choice > 5:
        os.system('cls')
        print("**Please Enter A Valid Choice**")
        menu_func()

def city_func():
    global weather, temp, pressure, humidity, high, low, user_input_city

    weather = ""
    temp = 0
    pressure = 0
    humidity = 0
    high = 0
    low = 0
    user_input_city = ""
    
    print("-------------------------------------------------------")

    user_input_city = input("Enter Desired City: ")
    ascii_banner_city = pyfiglet.figlet_format(user_input_city, font = "starwars")
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input_city}&units=imperial&APPID={api_key}")

    print(f"API Status Code: {weather_data.status_code}")
    print("-------------------------------------------------------")
    print()

    if weather_data.json()['cod'] == '404':
        print("City Not Found")
        print("-------------------------------------------------------")
        print()
    else:
        weather = weather_data.json()['weather'][0]['main']
        
        temp = round(weather_data.json()['main']['temp'])
        temp_string = str(temp)
        ascii_banner_temp = pyfiglet.figlet_format(temp_string + "°F", font = "starwars")
        
        pressure = weather_data.json()['main']['pressure']
        humidity = weather_data.json()['main']['humidity']

        high = round(weather_data.json()['main']['temp_max'])
        low = round(weather_data.json()['main']['temp_min'])

    print("-------------------------------------------------------")
    print(f"The weather in {user_input_city} is currently: {weather}")
    print("-------------------------------------------------------")
    print()
    print(f"The current temperature in {user_input_city} is: {temp} degrees °F")
    print(ascii_banner_city)
    print(ascii_banner_temp)
    print("-------------------------------------------------------")
    print()

def pressure_func(user_input_city, pressure):
    print("-------------------------------------------------------")
    print(f"The Pressure in {user_input_city} is currently: {pressure}")
    print("-------------------------------------------------------")
    
    pressure_string = str(pressure) + "hPa"
    ascii_banner_pressure = pyfiglet.figlet_format(pressure_string, font = "starwars")
    
    print(ascii_banner_pressure)
    print("-------------------------------------------------------")
    print()

def humidity_func(user_input_city, humidity):
    print("-------------------------------------------------------")
    print(f"The humidity in {user_input_city} is currently: {humidity}")
    print("-------------------------------------------------------")
   
    humidity_string = str(humidity) + "%"
    ascii_banner_humidity = pyfiglet.figlet_format(humidity_string, font = "starwars")
    
    print(ascii_banner_humidity)
    print("-------------------------------------------------------")
    print()

def extrema_func(user_input_city, high, low):
    print("-------------------------------------------------------")
    print(f"The high temp in {user_input_city} is projected to be: {high}")
    print("-------------------------------------------------------")
    print()
    print(f"The low temp in {user_input_city} is projected to be: {low}")
    print("-------------------------------------------------------")
    print()
    
    high_string = str(high)
    low_string = str(low)
    ascii_banner_highlow = pyfiglet.figlet_format("HIGH LOW", font = "starwars")
    ascii_banner_highlowtemp = pyfiglet.figlet_format(high_string+ "F                       " + low_string + "F")
    
    print(ascii_banner_highlow)
    print(ascii_banner_highlowtemp)
    print("-------------------------------------------------------")
    print()

city_func()
menu_func()

