from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getMessages:
    def __init__(self,apiKey = '',sign = '',time = '',getMessagesRequest = {'conversationId' : '','rowCount' : '','startOffset' : '','lang' : ''},session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualUserConversationService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://conversation.individual.ws.listingapi.gg.com}IndividualConversationServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualUserConversationService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getMessages(apiKey,sign,time,getMessagesRequest).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getMessagesResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
