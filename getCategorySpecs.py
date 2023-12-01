from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getCategorySpecs:
    def __init__(self,categoryCode,session = None):

        # Zeep Client
        
        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        try:
            
            with client.settings(raw_response=True):
                 response = helpers.serialize_object(service.getCategorySpecs(categoryCode,'tr').content.decode('utf-8'),dict)

                 #Parsing...
                 jsondata = xmltodict.parse(response)
                 #print (jsondata)
                 jsondump = json.dumps(jsondata)
                 jsonload = json.loads(jsondump)
                 jsonList = jsonload['env:Envelope']['env:Body']['ns0:getCategorySpecsResponse']['return']['specs']['spec']
                 self.specs = jsonList # / array
                 self.names = []
                 self.values = {}
                 self.types = {}
                 self.required = {}
                 self.asJson = jsonList
                 for spec in self.specs:
                     self.names.append([spec['@name']])
                     self.values[spec['@name']] = spec['values']['value']
                     self.types[spec['@name']] = spec['@type']
                     self.required[spec['@name']] = spec['@required']

        except:
            self.specs = None
            self.names = None
            self.values = None
            self.types = None
            self.required = None
            self.asJson = None
            
            pass
                 

             



        
