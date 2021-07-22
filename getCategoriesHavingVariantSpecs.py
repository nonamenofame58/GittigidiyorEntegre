from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getCategoriesHavingVariantSpecs:
    def __init__(self,lang = 'tr',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/CategoryService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://category.anonymous.ws.listingapi.gg.com}CategoryServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/CategoryService')
        try:
            with client.settings(raw_response=True):
                response = helpers.serialize_object(service.getCategory(lang).content.decode('utf-8'),dict)
                print (response)
                # Parsing ...   
                jsondata = xmltodict.parse(response)            
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getCategoryResponse']['return']['categories']['category']

             
        except:
            pass
        
