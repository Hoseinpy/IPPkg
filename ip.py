import os

import requests
import IP2Location


class IPPkg:


    def show_menu(self):
        print('WELCOME TO MY MINI IP PKG')
        print('-'*65)
        print("""
1 - get my ip
2 - get ip info
3 - exit
    """)
        try:
            user_choice = int(input('select one option: '))
            return user_choice
        except ValueError:
            print('invalid choice')

    
    def ip_location_address(self, latitude, longitude):
        url = f"https://api.slpy.com/v1/search?level=10&lat={latitude}&lon={longitude}&key=2a2398e8f3e3322026e11bdef"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['properties']
            print(data)
        
        else:
            print('cannot connect to api. try again')


    def full_IP_info(self, ip):
        database = IP2Location.IP2Location(os.path.join("./", "IPV6-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE-ADDRESSTYPE-CATEGORY-DISTRICT-ASN.SAMPLE.BIN"))

        rec = database.get_all(ip)

        print('-'*65)
        print('IP: ', ip)
        print("Country Code: " + rec.country_short)
        print("Country Name: " + rec.country_long)
        print("Region Name: " + rec.region)
        print("City Name: " + rec.city)
        print("ISP Name: " + rec.isp)
        print("Latitude: " + rec.latitude)
        print("Longitude: " + rec.longitude)
        print("Domain Name: " + rec.domain)
        print("ZIP Code: " + rec.zipcode)
        print("Time Zone: " + rec.timezone)
        print("Net Speed: " + rec.netspeed)
        print("Area Code: " + rec.idd_code)
        print("IDD Code: " + rec.area_code)
        print("Weather Station Code: " + rec.weather_code)
        print("Weather Station Name: " + rec.weather_name)
        print("MCC: " + rec.mcc)
        print("MNC: " + rec.mnc)
        print("Mobile Carrier: " + rec.mobile_brand)
        print("Elevation: " + rec.elevation)
        print("Usage Type: " + rec.usage_type)
        print("Address Type: " + rec.address_type)
        print("Category: " + rec.category)
        print("District: " + rec.district)
        print("ASN: " + rec.asn)
        print("AS: " + rec.as_name)
        print('-'*65)
        self.ip_location_address(rec.latitude, rec.longitude)


        return rec.latitude, rec.longitude


    def get_my_ip(self):
        url = 'https://api.ipify.org/'
        response = requests.get(url)
        if response.status_code == 200:
            self.full_IP_info(response.text)


if __name__ == "__main__":
    ippkg = IPPkg()

    user_choice = ippkg.show_menu()

    if user_choice == 1:
        ippkg.get_my_ip()

    elif user_choice == 2:
        ip = input('enter ip: ')
        if len(ip.split('.')) == 4:
            ippkg.full_IP_info(ip)
        else:
            print('invalid ipv4')

    elif user_choice == 3:
        print('bye!')
        exit