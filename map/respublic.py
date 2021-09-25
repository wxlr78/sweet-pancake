import folium
import requests
from bs4 import BeautifulSoup
import pandas as pd

map = folium.Map(location=[56.852593, 53.204843], zoom_start=7)

mark_item = []
count_item = []
coordinates = []

url = "http://wxlr78iv.beget.tech/globaldb.html"

headers = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.content

soup = BeautifulSoup(src, "lxml")

table = soup.find("table")

count = table.find_all(class_="count")
mark = table.find_all(class_="locality")
x = table.find_all(class_="x")
y = table.find_all(class_="y")

for item in mark:
    mark_item.append(item.text)

for item in count:
    count_item.append(int(item.text))

for i in range(len(x)):
    coordinates.append([float(x[i].text), float(y[i].text)])

for i in range(len(coordinates)):
    if count_item[i] <= 25:
        folium.Marker(location=coordinates[i], popup=f"{mark_item[i]}: {count_item[i]}", icon=folium.Icon(color='green')).add_to(map)
    if 25 < count_item[i] <= 50:
        folium.Marker(location=coordinates[i], popup=f"{mark_item[i]}: {count_item[i]}", icon=folium.Icon(color='beige')).add_to(map)
    if 50 < count_item[i] <= 75:
        folium.Marker(location=coordinates[i], popup=f"{mark_item[i]}: {count_item[i]}", icon=folium.Icon(color='orange')).add_to(map)
    if count_item[i] > 75:
        folium.Marker(location=coordinates[i], popup=f"{mark_item[i]}: {count_item[i]}", icon=folium.Icon(color='red')).add_to(map)

map.save("map1.html")
