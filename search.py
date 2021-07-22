from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class search:
    def __init__(self,keyword = '',criteria = {'format' : '','freeshipping' : '','startFromOne' : '','catalogOption' : '','newProduct' : '','minPrice' : '','maxPrice' : '','city' : '','runOutItems' : '','seller' : '','categoryCode' : '','catalogId' : '','categorySpecs' : {'categorySpec' : [{'name' : ''} , {'value' : ''}]}},startOffSet = 1,rowCount = 1,includeDescription = False, withData = False,orderBy = '',lang = 'tr',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/SearchService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://search.anonymous.ws.listingapi.gg.com}SearchServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/SearchService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.search(keyword,criteria,startOffSet,rowCount,includeDescription,withData,orderBy,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:searchResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
