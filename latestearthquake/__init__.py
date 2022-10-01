import requests
from bs4 import BeautifulSoup
"""
Method = fungsi
Field / Atrribute = variable
Constructor =  Method yang dipanggil pertama kali saat object diciptakan. gunakan untuk mendeklarasikan semua 
variable/field pada kelas
"""


class Disaster:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url
    def show_desc(self):
        print(self.description)
    def scraping_data(self):
        print("scraping_data is't implemented")
    def show_data(self):
        print("scraping_data is't implemented")
    def run(self):
        self.scraping_data()
        self.show_data()


class LatestQuake(Disaster):
    def __init__(self, url):

        super(LatestQuake, self).__init__(url, "to get the live latest earthquake in indonesia from https://bmkg.go.id/")
    def scraping_data(self):
        # global magnitude
        try:
            content = requests.get(self.url)
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


class LatestFlooded(Disaster):
    def __init__(self, url):
        super(LatestFlooded, self).__init__(url, "Not Implemented, but should return last flood in Indonesia")

    def show_desc(self):
        print(f"UNDER CONSTRUCTIONS {self.description}")

if __name__ == '__main__':
    quake_in_indonesia = LatestQuake('https://bmkg.go.id')
    # print(f'description: {quake_in_indonesia.description}')
    print('~~~Live Earthquake Application~~~')
    quake_in_indonesia.show_desc()
    quake_in_indonesia.run()

    flood_in_indonesia = LatestFlooded('Not Yet')
    # print(f'\nDeskripsi class oleh banjir terkini: {flood_in_indonesia.description}')
    flood_in_indonesia.show_desc()
    flood_in_indonesia.run()

    list_disaster = [quake_in_indonesia, flood_in_indonesia]
    print("\nSemua Bencana yang Tersedia")
    for disaster in list_disaster:
        disaster.show_desc()



# 'https://bmkg.go.id'