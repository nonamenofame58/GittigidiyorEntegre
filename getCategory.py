from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getCategory:
    def __init__(self,categoryCode = '',withSpecs = False,withDeepest = False,withCatalog = False,lang = 'tr',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        try:
            with client.settings(raw_response=True):
                response = helpers.serialize_object(service.getCategory(categoryCode,withSpecs,withDeepest,withCatalog,lang).content.decode('utf-8'),dict)
                # Parsing ...   
                jsondata = xmltodict.parse(response)            
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getCategoryResponse']['return']['categories']['category']
                categoriesArray = jsonload['env:Envelope']['env:Body']['ns0:getCategoryResponse']['return']['categories']['category']['categoryName']
                categoryCode = jsonload['env:Envelope']['env:Body']['ns0:getCategoryResponse']['return']['categories']['category']['categoryCode']
                categorySpecs = {}
                #print (jsonList)
                try :
                    categorySpecs[jsonList['categoryName']] = {}
                    for spec in jsonList['specs']['spec']:
                        
                        
                        categorySpecs[jsonList['categoryName']][spec['@name']] = {}
                        categorySpecs[jsonList['categoryName']][spec['@name']] = { 'type' : spec['@type'] , 'required' : spec['@required'] , 'values' : spec['values']['value'] } 
                           
    
                except:
                    pass

                 
                self.category = categoriesArray
                self.specs = categorySpecs
                self.code = categoryCode
                self.asJson = jsonList
                print (categorySpecs)
        except:
            self.category = None
            self.specs = None
            self.code = None
            self.asJason = None
            pass
                 
             
            
        
