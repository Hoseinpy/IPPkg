import os, sys
import IP2Location


def full_IP_info(ip):
    database = IP2Location.IP2Location(os.path.join("./", "IPV6-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE-ADDRESSTYPE-CATEGORY-DISTRICT-ASN.SAMPLE.BIN"))

    rec = database.get_all(ip)
    print('-'*65)
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


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if len(sys.argv[1].split('.')) == 4:
            ip = sys.argv[1]
            full_IP_info(ip)
        else:
            print('invalid ipv4')
    else:
        print('USEAGE: python3 ip.py {`ip to lockup`}')
