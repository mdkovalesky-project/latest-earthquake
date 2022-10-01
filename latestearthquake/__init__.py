import requests
from bs4 import BeautifulSoup
"""
Method = fungsi
Field / Atrribute = variable
"""

class LatestQuake:
    def __init__(self, url):
        self.description = "to get the live latest earthquake in indonesia from bmkg.go.id"
        self.result = None
        self.url = url

    def ekstraksi_data(self):
        # global magnitude
        try:
            content = requests.get()
        except Exception:
            return None

        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser') # instantiation = instansiasi object pada kelas

            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(',')
            date = result[0]
            time = result[1]

            result = soup.find('div', {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
            result = result.findChildren('li')
            i = 0
            magnitude = None
            depth = None
            ls = None
            bt = None
            central = None
            desc = None

            for res in result:
                if i == 1:
                    magnitude = res.text
                elif i == 2:
                    depth = res.text
                elif i == 3:
                    coordinate = res.text.split(' - ')
                    ls = coordinate[0]
                    bt = coordinate[1]
                elif i == 4:
                    central = res.text
                elif i == 5:
                    desc = res.text
                i = i + 1

            hasil = dict()
            hasil["date"] = date
            hasil["time"] = time
            hasil["magnitude"] = magnitude
            hasil["depth"] = depth
            hasil["coordinate"] = {"ls": ls, "bt": bt}
            hasil["central"] = central
            hasil["desc"] = desc
            self.result = hasil
        else:
            return None


    def show_data(self):
        if self.result is None:
            print("Unable to Find Recent Earthquake Data")
            return

        print('\nGempa Terakhir Berdasarkan BMKG')
        print(f"Date: {self.result['date']}")
        print(f"Time: {self.result['time']}")
        print(f"Magnitude: {self.result['magnitude']}")
        print(f"Depth: {self.result['depth']}")
        print(f"Coordinate Location: LS = {self.result['coordinate']['ls']}, BT = {self.result['coordinate']['bt']}")
        print(f"Location Quake: {self.result['central']}")
        print(f"Description: {self.result['desc']}")
    def run(self):
        self.ekstraksi_data()
        self.show_data()

if __name__ == '__main__':
    quake_in_indonesia = LatestQuake('https://bmkg.go.id')
    print(f'description: {quake_in_indonesia.description}\n')
    print('\n~~~Live Earthquake Application~~~')
    quake_in_indonesia.run()

