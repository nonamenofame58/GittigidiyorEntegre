from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getSubCategories:
    def __init__(self,categoryCode = 'gdk',withSpecs = False, withDeepest = False , withCatalog = False ,lang = 'tr' ,session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getSubCategories(categoryCode,withSpecs,withDeepest,withCatalog,'tr').content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getSubCategoriesResponse']['return']['categories']['category']
                subCategoryNames = []
                subCategoryCodes = {}
                subCategorySpecs = {}
                for subCat in jsonList:
                    subCategoryNames.append(subCat['categoryName'])
                    subCategoryCodes[subCat['categoryName']] = subCat['categoryCode']
                    try :
                        subCategorySpecs[subCat['categoryName']] = {}
                        for spec in subCat['specs']['spec']:
                            
                            subCategorySpecs[subCat['categoryName']][spec['@name']] = {}
                            
                            subCategorySpecs[subCat['categoryName']][spec['@name']] = { 'type' : spec['@type'] , 'required' : spec['@required'] , 'values' : spec['values']['value'] } 
                           
    
                    except:
                        
                        pass
    
                    



             # Return
             
                self.names = subCategoryNames
                self.codes = subCategoryCodes
                self.specs = subCategorySpecs
                self.asJson = jsonload['env:Envelope']['env:Body']['ns0:getSubCategoriesResponse']['return']['categories']
                
            except:
                self.names = None
                self.codes = None
                self.specs = None
                self.asJson = None
                
                pass
                 
             
            
        
