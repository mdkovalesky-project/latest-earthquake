# Lates Earthquake in Indonesia
This package will get the live latest earthquake from BMKG | Meteorological, Climatological, and Geophysical Agency

## HOW IT WORK?
This package will scrape from [BMKG](https://bmkg.go.id) to get live latest quake happend in indonesia

## HOW TO USE?
```
import latestearthquake

if __name__ == '__main__':
    print('~~~Live Earthquake Application~~~')
    result = latestearthquake.ekstraksi_data()
    latestearthquake.show_data(result)
```


This package will use from Beautifulsoup4 and Request, to produce output in the form of JSON that's ready to be used in web or mobile applications
