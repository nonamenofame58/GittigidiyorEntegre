from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json



        
class getDeepestCategories:
    
    def __init__(self,startOffSet = 1 ,rowCount = 1 ,withSpecs = True ,lang = 'tr', session = None):
        # Zeep Client
        
        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        try:
            
            with client.settings(raw_response=True):
                
                response = helpers.serialize_object(service.getDeepestCategories(startOffSet,rowCount,withSpecs,lang).content.decode('utf-8'),dict)
                # Parsing...
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getDeepestCategoriesResponse']['return']['categories']['category']
                categorySpecs = {}

                if rowCount > 1 :
                    
                    Category = jsonload['env:Envelope']['env:Body']['ns0:getDeepestCategoriesResponse']['return']['categories']['category']
                    for Cat in Category:
                        
                        categoryCode = Cat['categoryCode']
                        categoryName = Cat['categoryName']
                        cSpecs = Cat['specs']['spec']

                        categorySpecs[categoryName] = {'code' : categoryCode }            
                        for specs in cSpecs:
                            
                            categorySpecs[categoryName][specs['@name']] = { 'type' : specs['@type'], 'required' : specs['@required'] , 'values' : specs['values']['value'] }

                else:

                    categoryCode = jsonload['env:Envelope']['env:Body']['ns0:getDeepestCategoriesResponse']['return']['categories']['category']['categoryCode']
                    categoryName = jsonload['env:Envelope']['env:Body']['ns0:getDeepestCategoriesResponse']['return']['categories']['category']['categoryName']
                    cSpecs = jsonload['env:Envelope']['env:Body']['ns0:getDeepestCategoriesResponse']['return']['categories']['category']['specs']['spec']
                    categorySpecs = {}
                    categorySpecs[categoryName] = {'code' : categoryCode }            
                    for specs in cSpecs:
                        categorySpecs[categoryName][specs['@name']] = { 'type' : specs['@type'], 'required' : specs['@required'] , 'values' : specs['values']['value'] }

                self.categorySpecs = categorySpecs
        except:
            self.categorySpecs = None
            pass
        
        
