# test_weather_location.py
from modules.tools.get_current_weather import CurrentWeather
import requests

def get_my_city():
    try:
        # Usando IP público para estimar a localização
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city")
        return city
    except Exception as e:
        print("Erro ao obter localização:", e)
        return None

if __name__ == "__main__":
    city = get_my_city()
    if city:
        weather = CurrentWeather()
        print(f"Detectei que você está em: {city}")
        print(weather.get_current_weather(city))
    else:
        print("Não foi possível determinar sua localização.")

