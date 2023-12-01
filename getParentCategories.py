from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json



        
class getParentCategories:
    def __init__(self,withSpecs = False,withDeepest = False,withCatalog = False,lang = 'tr' , session = None):

        # Zeep Client
        
        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        try:
            
            with client.settings(raw_response=True):
                response = helpers.serialize_object(service.getParentCategories(withSpecs,withDeepest,withCatalog,'tr').content.decode('utf-8'),dict)
                # Parsing...
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getParentCategoriesResponse']['return']['categories']['category']
                jsonLists = jsonload['env:Envelope']['env:Body']['ns0:getParentCategoriesResponse']['return']['categories']
                categoryList = []
                categoryCodeList = {}
                categorySpecs = {}
                
                for js in jsonList:
                    categoryCodeList[js['categoryName']] = js['categoryCode'] 
                    categoryList.append(js['categoryName'])
    
                    try :
                        categorySpecs[js['categoryName']] = {}
                        for spec in js['specs']['spec']:
                            categorySpecs[js['categoryName']][spec['@name']] = {}
                            categorySpecs[js['categoryName']][spec['@name']] = { 'type' : spec['@type'] , 'required' : spec['@required'] , 'values' : spec['values']['value'] } 
                           
    
                    except:
                        pass
    
                    
    
                # Return
                self.specs = categorySpecs
                self.names = categoryList
                self.codes = categoryCodeList
                self.asJson = jsonLists
                
        except:
            self.specs = None
            self.names = None
            self.codes = None
            self.asJson = None
            pass
         
