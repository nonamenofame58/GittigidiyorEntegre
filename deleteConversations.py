from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class deleteConversations:
    def __init__(self,apiKey = '',sign = '',time = '',deleteConversationsRequest = {'conversationId' : [{'conversationId' : ''}],'lang' : ''},session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualUserConversationService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://conversation.individual.ws.listingapi.gg.com}IndividualConversationServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualUserConversationService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.deleteConversations(apiKey,sign,time,deleteConversationsRequest).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:deleteConversationsResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
