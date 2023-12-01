from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class markAsUnread:
    def __init__(self,apiKey = '',sign = '',time = '',markAsUnreadRequest = {'conversationId' : '','lang' : ''},session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualSaleService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://sale.individual.ws.listingapi.gg.com}IndividualSaleServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualSaleService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.markAsUnread(apiKey,sign,time,markAsUnreadRequest).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:markAsUnreadResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
