from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class payPrice:
    def __init__(self,apiKey = '',sign = '',time = '',paymentVoucher = '',ccOwnerName = '',ccOwnerSurname = '',ccNumber = '',cvv = '' , expireMonth = '',expireYear = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductPaymentService?wsdl", transport=Transport(session=session))
        service = client.create_service('{https://payment.product.individual.ws.listingapi.gg.com}IndividualProductPaymentServiceBinding' , 'https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductPaymentService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.payPrice(apiKey,sign,time,paymentVoucher,ccOwnerName,ccOwnerSurname,ccNumber,cvv,expireMonth,expireYear,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:payPriceResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
