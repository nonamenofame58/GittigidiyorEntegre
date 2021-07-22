from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getStore:
    def __init__(self,apiKey = '',sign = '',time = '',lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualStoreService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://store.individual.ws.listingapi.gg.com}IndividualStoreServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualStoreService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getStore(apiKey,sign,time,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getStoreResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
