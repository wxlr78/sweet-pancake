import folium
import requests
from bs4 import BeautifulSoup
import pandas as pd

map = folium.Map(location=[56.854560, 53.206894], zoom_start=11)

mark_item = []
coordinates = []
male_list = []
female_list = []

url = "http://wxlr78iv.beget.tech/sexdb.html"

headers = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.content

soup = BeautifulSoup(src, "lxml")

table = soup.find("table")

mark = table.find_all(class_="locality")
x = table.find_all(class_="x")
y = table.find_all(class_="y")
male = table.find_all(class_="male")
female = table.find_all(class_="female")

for item in mark:
    mark_item.append(item.text)

for i in range(len(x)):
    coordinates.append([float(x[i].text), float(y[i].text)])

for item in male:
    male_list.append(int(item.text))

for item in female:
    female_list.append(int(item.text))

for i in range(len(coordinates)):
    if male_list[i] > female_list[i]:
        folium.Marker(location=coordinates[i], popup=f"{mark_item[i]}, мужчин:{male_list[i]}, женщин:{female_list[i]}", icon=folium.Icon(color='blue')).add_to(map)
    else:
        folium.Marker(location=coordinates[i], popup=f"{mark_item[i]}, мужчин:{male_list[i]}, женщин:{female_list[i]}", icon=folium.Icon(color='purple')).add_to(map)


map.save("map2.html")
