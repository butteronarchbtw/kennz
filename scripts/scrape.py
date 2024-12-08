import requests
from bs4 import BeautifulSoup

url = "https://de.wikipedia.org/wiki/Liste_der_Kfz-Kennzeichen_in_Deutschland"

res = requests.get(url).text
soup = BeautifulSoup(res, "lxml")

lines = []

for table in soup.find_all("table", class_="wikitable")[1:27]:
    for items in table.find_all("tr")[1::]:
        try:
            data = items.find_all(["th", "td"])
            abk = data[0].text.strip()
            if len(abk) > 3 or len(abk) < 1:
                raise Exception("skipping this bs")
            stadt = data[1].text.strip().split("\n")[0]
            lines.append("{},{}".format(abk, stadt))
        except:
            pass

f = open("data.csv", "w")
f.write("\n".join(lines))
f.close()
