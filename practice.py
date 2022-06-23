import datetime
today = datetime.datetime(2022, 6, 3)
nextday = today + datetime.timedelta(days=1)
print(str(nextday).split()[0].split("-"))