from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getCities:
    def __init__(self,session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CityService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://city.anonymous.ws.listingapi.gg.com}CityServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CityService')
        try:
            with client.settings(raw_response=True):
                 response = helpers.serialize_object(service.getCities('0','84','tr').content.decode('utf-8'),dict)

                 # Parsing...
                 jsondata = xmltodict.parse(response)
                 jsondump = json.dumps(jsondata)
                 jsonload = json.loads(jsondump)
                 jsonList = jsonload['env:Envelope']['env:Body']['ns0:getCitiesResponse']['return']['cities']['city']
                 cityNames = []
                 cityCodes = []
                 cities = {}

                 for city in jsonList:
                     cityNames.append(city['cityName'])
                     cityCodes.append(city['trCode'])
                     cities[city['cityName']] = city['trCode']

                 # Return
             
                 self.names = cityNames
                 self.codes = cityCodes
                 self.cities = cities
        except:
            self.names = None
            self.codes = None
            self.cities = None
            pass
    def loopCityNames(self):
        for name in self.Names:
            print(name)

    def loopCityCodes(self):
        for code in self.Codes:
            print(code)
                 
             
            
        
