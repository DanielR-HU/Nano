import requests

countryCode = "NL"
city = input("Voer stad in: ")


locationKey = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/{countryCode}/search?apikey=NCkXL1pFDKcj3MAl2wpiif2jcI6yowRH&q={city}")
locationKey = locationKey.json()[0]["Key"]
response = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{locationKey}?apikey=NCkXL1pFDKcj3MAl2wpiif2jcI6yowRH&language=nl-nl&details=true&metric=true')
data = response.json()

voorspelling = data["DailyForecasts"][0]
temperatuur = voorspelling["Temperature"]
minTemp = temperatuur["Minimum"]["Value"]
maxTemp = temperatuur["Maximum"]["Value"]
GevoelsTemp = voorspelling["RealFeelTemperature"]["Maximum"]["Value"]
weer = voorspelling["Day"]["IconPhrase"]
#nieuw
luchtKwaliteit = voorspelling["AirAndPollen"][0]["Category"]
onweerKans = voorspelling["Day"]["ThunderstormProbability"]
regenKans = voorspelling["Day"]["RainProbability"]
sneeuwKans = voorspelling["Day"]["SnowProbability"]
ijsKans = voorspelling["Day"]["IceProbability"]
wind = voorspelling["Day"]["Wind"]["Speed"]["Value"]
windRichting = voorspelling["Day"]["Wind"]["Direction"]["Localized"]
wolkenCover = voorspelling["Day"]["CloudCover"]
wolkSoort = voorspelling["Day"]["LongPhrase"]
source = voorspelling["Sources"]

print("Temperatuur:")
print(f"De minimale temperatuur is vandaag {minTemp} graden")
print(f"De maximale temperatuur is vandaag {maxTemp} graden")
print(f"De temperatuur voelt vandaag aan als {GevoelsTemp} graden")
print("\n\nWeer:")
print(f"het weer is vandaag {weer}")
print(f"De luchtkwaliteit is vandaag {luchtKwaliteit}")
print(f"De kans op onweer is vandaag {onweerKans}%")
print(f"De kans op regen is vandaag {regenKans}%")
print(f"De kans op sneeuw is vandaag {sneeuwKans}%")
print(f"De kans op ijs is vandaag {ijsKans}%")
print(f"De windsnelheid is vandaag {wind} km/h")
print(f"De windrichting is vandaag {windRichting}")
print(f"De bewolking is vandaag {wolkenCover}%")
print(f"De soort bewolking is vandaag {wolkSoort}")
print(f"\nBron: {source}")