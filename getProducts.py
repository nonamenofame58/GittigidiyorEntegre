from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getProducts:
    def __init__(self,apiKey = '',sign = '',time = '',startOffSet = 1,rowCount = 1 ,status = ,withData = False,lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductService?wsdl", transport=Transport(session=session))
        service = client.create_service('{https://product.individual.ws.listingapi.gg.com}IndividualProductServiceBinding' , 'https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getProducts(apiKey,sign,time,startOffSet,rowCount,withData,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getProductsResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
