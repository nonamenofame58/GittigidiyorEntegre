from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class registerDeveloper:
    def __init__(self,nick = '', password = '',lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/DeveloperService?wsdl", transport=Transport(session=session))
        service = client.create_service('https://developer.anonymous.ws.listingapi.gg.com}DeveloperServiceBinding' , 'https://dev.gittigidiyor.com:8443/listingapi/ws/DeveloperService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.registerDeveloper(nick,password,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:registerDeveloperResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
