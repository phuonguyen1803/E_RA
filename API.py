import requests
import pandas as pd
from datetime import datetime, timedelta

# Hàm lấy dữ liệu dự báo theo giờ từ API One Call
def fetch_hourly_forecast(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        hourly_data = []
        for item in data['list']:
            weather_info = {
                "Date": item['dt_txt'].split(" ")[0],
                "Time": item['dt_txt'].split(" ")[1],
                "Temperature (°C)": item['main']['temp'],
                "Humidity (%)": item['main']['humidity'],
                "Wind Speed (m/s)": item['wind']['speed'],
                "Pressure (hPa)": item['main']['pressure']
            }
            hourly_data.append(weather_info)
        return hourly_data
    else:
        print(f"Error: {response.status_code}")
        return None

# Hàm lưu dữ liệu vào file CSV
def save_to_csv(data, filename="hourly_weather_data.csv"):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Dữ liệu đã được lưu vào {filename}.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Thông tin API và tọa độ thành phố cần lấy dữ liệu
API_KEY = "70776dedcb452d7cfebda26b6b167e53"  # Thay bằng API key của bạn
CITY_NAME = "Ho Chi Minh"
LAT = 10.7769  # Vĩ độ của TP Hồ Chí Minh
LON = 106.7009  # Kinh độ của TP Hồ Chí Minh

# Lấy dữ liệu và lưu vào file CSV
weather_forecast = fetch_hourly_forecast(LAT, LON, API_KEY)
if weather_forecast:
    save_to_csv(weather_forecast)
