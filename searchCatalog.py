from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class searchCatalog:
    def __init__(self,page = 1,rowCount = 1,criteria = {'keywords' : '','categoryCode' : ''},lang = 'tr',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CatalogV2Service?wsdl", transport=Transport(session=session))
        service = client.create_service('http://catalogv2.anonymous.ws.listingapi.gg.com}CatalogV2ServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CatalogV2Service')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.searchCatalog(page,rowCount,criteria,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:searchCatalogResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
