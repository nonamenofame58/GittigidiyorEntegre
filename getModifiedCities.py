from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getModifiedCities:
    def __init__(self,changeTime = 123123, startOffSet = 2,rowCount = 2,lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CityService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://city.anonymous.ws.listingapi.gg.com}CityServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CityService')
        try:
            with client.settings(raw_response=True):
                 response = helpers.serialize_object(service.getModifiedCities(changeTime,startOffSet,rowCount,lang).content.decode('utf-8'),dict)

                 # Parsing...
                 jsondata = xmltodict.parse(response)
                 jsondump = json.dumps(jsondata)
                 jsonload = json.loads(jsondump)
                 jsonList = jsonload['env:Envelope']['env:Body']['ns0:getModifiedCitiesResponse']['return']
                 self.asJson = jsonList
        except:
            self.asJson = None
            pass
             
            
        
