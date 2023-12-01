from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json



        
class getCategorySpecsWithDetail:
    
    def __init__(self,categoryCode = '',lang = 'tr', session = None):
        # Zeep Client
        
        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        try:
            with client.settings(raw_response=True):
                response = helpers.serialize_object(service.getCategorySpecsWithDetail(categoryCode,lang).content.decode('utf-8'),dict)
                
                # Parsing...
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getCategorySpecsWithDetailResponse']['return']
                specs = {}
                if jsonList['specs']:
                    for spc in jsonList['specs']['spec']:
                        specs[spc['@name']] = {}
                        specs[spc['@name']] = {'childSpecId' : spc['@childSpecId'],'specId' : spc['@specId'], 'type' : spc['@type'] , 'required' : spc['@required'] , 'values' : spc['values']['value']}
                self.specs = specs
                            
        except:
            self.specs = None
            pass

        
    def loopSpecNames(self):
        for names in self.specs:
            print(names)

            
    def loopSpecValueNames(self):
        for vNames in self.specs:
            print ('#- ' + vNames + ' -#')
            for names in self.specs[vNames]['values']:
                print(names['name'])

                
    def loopSpecValueSpecId(self):
        for vNames in self.specs:
            print ('#- ' + vNames + ' -#')
            for ids in self.specs[vNames]['values']:
                print(ids['@specId'])
