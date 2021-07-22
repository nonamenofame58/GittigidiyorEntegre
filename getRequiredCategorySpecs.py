from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json



        
class getRequiredCategorySpecs:
    
    def __init__(self,categoryCode = '',lang = 'tr', session = None):
        # Zeep Client
        
        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryV2Service?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://categoryv2.anonymous.ws.listingapi.gg.com}CategoryV2ServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryV2Service')
        try:
            with client.settings(raw_response=True):
                response = helpers.serialize_object(service.getRequiredCategorySpecs(categoryCode,lang).content.decode('utf-8'),dict)
                
                # Parsing...
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getRequiredCategorySpecsResponse']['return']
                print (jsonList)
                self.catalogRequired = jsonList['catalogRequired']
                self.count = jsonList['count']
                self.requiredSpecsDict = jsonList['requiredSpecs']['spec']
                requiredSpecNames = []
                for names in self.requiredSpecsDict:
                    requiredSpecNames.append(names['@name'])
                self.requiredSpecNames = requiredSpecNames
                
        except:
            self.catalogRequired = None
            self.count = None
            self.requiredSpecsDict = None
            self.requiredSpecNames = None
            pass
    def loopRequiredSpecs(self):
        for specs in self.requiredSpecNames:
            print (specs)
        
