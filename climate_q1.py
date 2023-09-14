import matplotlib.pyplot as plt
import sqlite3
import os

#initialize empty lists        
years = []
co2 = []
temp = []


#get current directory to avoid bugs
current_dir = os.path.dirname(os.path.abspath(__file__))


#construct full path to the database file
db_file_path = os.path.join(current_dir, "climate.db")


#connect to database
connection = sqlite3.connect(db_file_path)
cursor = connection.cursor()

#execute sql query to fetch data
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")

#fetch all the data rows from the query
data_rows =  cursor.fetchall()

#iterate through
for row in data_rows:
    year, co2_value, temp_value = row
    years.append(year)
    co2.append(co2_value)
    temp.append(temp_value)

#close database connection

connection.close()



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
