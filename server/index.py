from flask import Flask, request, jsonify
from weather import get_daily_city_weather, get_hourly_city_weather
import json


index = Flask(__name__)#references this file

@index.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
        index.run(debug=True)

#returns 3 days of temperature, day0, day1, day2
#example: {'day0': {'date': '2024-05-15', 'high': 61, 'low': 58, 'current': 60}, 'day1': {'date': '2024-05-16', 'high': 60, 'low': 57, 'current': 58}, 'day2': {'date': '2024-05-17', 'high': 71, 'low': 54, 'current': 62}}
@index.route('/getDailyWeatherByCity', methods=['GET'])
async def get_daily_weather_by_city():
    try:
        city_name = request.args.get('name')
        response_data = await get_daily_city_weather(city_name)
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@index.route('/getHourlyWeatherByCity', methods=['GET'])
async def get_hourly_weather_by_city():
    try:
        city_name = request.args.get('name')
        response_data = await get_hourly_city_weather(city_name)
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400



##Example route