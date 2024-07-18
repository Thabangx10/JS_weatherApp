from flask import Flask
import requests
import jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Connection Configuration
mydb = mysql.connector.connect(
    host="bw59sqe4chjztk4k1mri-mysql.services.clever-cloud.com",
    user="uemwk5cbfvpokdi0",
    password="qAiIhXVCUKdob2tTzO9F",
    database="bw59sqe4chjztk4k1mri"
)

# Endpoint to save weather data
@app.route('/save_weather_data', methods=['POST'])
def save_weather_data():
    data = requests.json
    city = data['city']
    temperature = data['temperature']
    humidity = data['humidity']
    weather_conditions = data['weather_conditions']

    cursor = mydb.cursor()
    sql = "INSERT INTO weather (city, temperature, humidity, weather_conditions) VALUES (%s, %s, %s, %s)"
    val = (city, temperature, humidity, weather_conditions)
    cursor.execute(sql, val)
    mydb.commit()

    return jsonify({'status': 'success', 'message': 'Data saved successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
