from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getOptionFeaturesInfo:
    def __init__(self,apiKey = '',sign = '',time = '',productsIds = [], lang = 'tr',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductPaymentService?wsdl", transport=Transport(session=session))
        service = client.create_service('{https://payment.product.individual.ws.listingapi.gg.com}IndividualProductPaymentServiceBinding' , 'https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductPaymentService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getOptionFeaturesInfo(apiKey,sign,time,productIds,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getOptionFeaturesInfoResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
