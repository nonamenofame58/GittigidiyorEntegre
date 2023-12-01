from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class createApplication:
    def __init__(self,applicationInfo = {'applicationInfo' : {'developerId' : '','name' : '','description' : '','accesType' : '','appType' : '', 'descDetail' : '' , 'succesReturnUrl' : '' , 'failReturnUrl' : ''}},lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/ApplicationService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://application.anonymous.ws.listingapi.gg.com}ApplicationServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/ApplicationService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.createApplication(applicationInfo,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:createApplicationResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
