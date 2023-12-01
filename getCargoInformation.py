from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getCargoInformation:
    def __init__(self,apiKey = '',sign = '',time = '',saleCode = 12321,lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualCargoService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://cargo.individual.ws.listingapi.gg.com}IndividualCargoServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualCargoService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getCargoInformation(apiKey,sign,time,saleCode,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getCargoInformationResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
