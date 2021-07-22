from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getSoldItems:
    def __init__(self,apiKey = '',sign = '',time = '',startOffSet = 2,rowCount= 2,withData = False,lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualActivityService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://activity.individual.ws.listingapi.gg.com}IndividualActivityServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualActivityService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getSoldItems(apiKey,sign,time,startOffSet,rowCount,withData,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getSoldItemsResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
