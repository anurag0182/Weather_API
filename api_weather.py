import requests

def check_weather(city_name):

    create_key ="Enter an API_key"
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={create_key}&units=metric")

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            print(f"weather in{city}, {country}")
            print(f"temperature:{temp}*C")
            print(f"condition:{weather.capitalize()}")
            print(f"Humidity:{humidity}%\n")
        
        else:
            print("failed to fetch data")

    except requests.exceptions.RequestException as e:
        print("Error in connecting to API: ", e)

city = input("Enter your city")
check_weather(city)