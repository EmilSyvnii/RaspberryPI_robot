from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/lab_temp")
def lab_temp():
	import sys
	import Adafruit_DHT
	CO = 0.8
	smk = 0.0
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 21)
	if humidity is not None and temperature is not None:
		return render_template("lab_temp.html",temp=temperature,hum=humidity, CO=CO, smk=smk)
	else:
		return render_template("no_sensor.html")

@app.route("/lab_env_db")
def lab_env_db():
	import sqlite3
	conn=sqlite3.connect('/var/www/lab_app/lab_app.db')
	curs=conn.cursor()
	curs.execute("SELECT * FROM temperatures")
	temperatures = curs.fetchall()
	curs.execute("SELECT * FROM humidities")
	humidities = curs.fetchall()
	curs.execute("SELECT * FROM smoke")
        smoke = curs.fetchall()
	curs.execute("SELECT * FROM co_level")
        co_level = curs.fetchall()

	conn.close()
	return render_template("lab_env_db.html",temp=temperatures,hum=humidities, smoke=smoke, co_level=co_level)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
