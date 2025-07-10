import requests
print("\n~~~~~~~~~~ Weather Forcast ~~~~~~~~~~~")
user_choice=int(input("\n1.To Check The Weather.\n2.To Exit.\n"))
while user_choice!=2:
    api_key = 'a1904ec799f0041ff7e7f8f16d5f6d1c'
    user_input= input("Enter a City : ")
# print(user_input)
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("City Not Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        pressure = weather_data.json()['main']['pressure']
        humidity = weather_data.json()['main']['humidity']
        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}°F ")
        print(f"The Pressure in {user_input} is : {pressure}")
        print(f"The Humidity in {user_input} is : {humidity}")
        if weather == 'Haze ':
            print("Have a Good Day :)")
        elif weather == 'Clear':
            print("have a good day:)")
        else:
            print("Stay Safe :(")
    print("\n~~~~~~~~~~ Weather Forcast ~~~~~~~~~~~") 
    user_choice=int(input("\n1.To Check The Weather.\n2.To Exit.\n"))
    


