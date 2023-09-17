import board
import sqlite3
import adafruit_bme680
i2c = board.I2C()
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

sensor.seaLevelhPa = 1011.7

print('Temperature: {} degrees C'.format(sensor.temperature))
print('Gas: {} ohms'.format(sensor.gas))
print('Humidity: {}%'.format(sensor.humidity))
print('Pressure: {}hPa'.format(sensor.pressure))

temp = sensor.temperature
gas = sensor.gas
humid = sensor.humidity
press = sensor.pressure

"("

try:
    sqliteConnection = sqlite3.connect('localDatabase.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO BME688
                          (Temperature, Humidity, Gas, Pressure) 
                           VALUES 
                          ({0}, {1}, {2}, {3})""".format(temp, humid, gas, press)

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into BME688 table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into BME688 table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

