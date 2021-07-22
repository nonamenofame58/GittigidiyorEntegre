from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


        
class getCategoryVariantSpecs:

    
    def __init__(self,categoryCode = '' , lang = 'tr', session = None):
        
        # Zeep Client
        
        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        try:
            with client.settings(raw_response=True):
                response = helpers.serialize_object(service.getCategoryVariantSpecs(categoryCode,lang).content.decode('utf-8'),dict)
                # Parsing...
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getCategoryVariantSpecsResponse']['return']['specs']['spec']
        
                self.specBase = jsonList['@base']
                self.specType = jsonList['@type']
                self.specName = jsonList['@name']
                self.specNameId = jsonList['@nameId']
                self.specValuesDict = jsonList['specValues']['specValue']
                self.specValues = []
                self.specOrderNumbers = []
                self.specValueIds = []
                for value in self.specValuesDict:
                    self.specValues.append(value['@value']),
                    self.specOrderNumbers.append(value['@orderNumber'])
                    self.specValueIds.append(value['@valueId'])
    
                    
                categorySpecs = {}

        except:
            self.specBase = None
            self.specType = None
            self.specName = None
            self.specNameId = None
            self.specValuesDict = None
            self.specValues = None
            self.specOrderNumbers = None
            self.specValueIds = None
            pass
    def loopValues(self):
        try:
            
            for val in self.specValues:
                print (val)
        except:
            pass
    def loopOrderNumbers(self):
        try:
            for ordNumb in self.specOrderNumbers:
                print (ordNumb)
        except:
            pass
    def loopValueIds(self):
        try:
            
            for valId in self.specValueIds:
                print (valId)
        except:
            pass
