import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print("People in Space: ", result['number'])
people = result['people']


for p in people:
    print(p["name"],'in', p['craft'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ',lat)
print("Longitude: ", lon)

screen = turtle.Screen()
screen.setup(800, 400)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('https://ibb.co/vmnNxKF')
screen.register_shape('https://ibb.co/fx32Bhj')

iss = turtle.Turtle()
iss.shape('https://ibb.co/fx32Bhj')
iss.setheading(90)

iss.penup()
iss.goto(lon,lat)

# Alter lat & lon of location

# Kuala Lumpur, Malaysia
lat = 3.186528
lon = 101.635028

# London, UK
lat2 = 51.5074
lon2 = 0.1278

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(8)
location.hideturtle()


# Change var lat & lon to change location
url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
over = result['response'][0]['risetime']

date = time.ctime(over)
print('Next overhead of the I.S.S. on', date)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)



