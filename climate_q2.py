import matplotlib.pyplot as plt
import pandas as pd
import os

#get current directory to avoid bugs
current_dir = os.path.dirname(os.path.abspath(__file__))

#construct full path to the file
csv_file_path = os.path.join(current_dir, "climate.csv")

#load data from the CSV file into a dataframe
df = pd.read_csv(csv_file_path)

#extract data to columns
years = df['Year']
co2 = df['CO2']
temp = df['Temperature']

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
plt.savefig("co2_temp_2.png") 

