from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class cancelSale:
    def __init__(self,apiKey = '',sign = '',time = '',saleCode = 2312,reasonId = 1,lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualSaleService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://sale.individual.ws.listingapi.gg.com}IndividualSaleServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualSaleService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.cancelSale(apiKey,sign,time,saleCode,reasonId,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:cancelSaleResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
