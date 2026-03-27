from pandas import DataFrame

data = []

with open("weather_data.csv") as file:
    reader = file.readlines()
    print(reader)


import csv                                      #Old school method of getting tabular data

with open("weather_data.csv") as file:
    temperatures = []
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


import pandas                                   #Commonly used library when using data processing

data = pandas.read_csv("weather_data.csv")
print(type(data))                               #Gets data type. Pandas uses SERIES (columns/rows of data) or DATA FRAMES (cells)
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(type(data_dict))
print(data_dict)

temp_list = data["temp"].tolist()
print(temp_list)

average_temp = sum(temp_list) / len(temp_list)
print(f"Average temp is {average_temp}")

print(f"The average temp is {data["temp"].mean()}")
print(f"The highest temp is {data["temp"].max()}")


"""Get data from COLUMN"""
print(data["condition"])                            #These 2 lines of code are the same
print(data.condition)                               #The data series are CASE SENSITIVE


"""Get data from ROW"""
print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])        #Find row with highest temp. data["temp"].max() is a conditional

monday = data[data.day == "Monday"]
print(monday.condition)

print(f"{(monday.temp * 9/5) + 32} Fahrenheit")


"""Create a dataframe"""
dataframe_dict = {
    "students": ["Amy", "James", "David"],
    "scores": [70, 80, 90],
}

dataframe_data = DataFrame(dataframe_dict)
dataframe_data.to_csv("student_data.csv")



