from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getSrsProcessDetailsSaleItem:
    def __init__(self,apiKey = '',sign = '',time = '',lang = '',getSrsProcessDetailsSaleItem = {'memberId' : '','pageNumber':'','pageSize':'','salesCode' : ['1','2']} ,session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualAccountingService?wsdl", transport=Transport(session=session))
        service = client.create_service('{http://accounting.individual.ws.listingapi.gg.com}IndividualAccountingServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualAccountingService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getSrsProcessSaleItem(apiKey,sign,time,lang,getSrsProcessDetailsSaleItem ).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)
                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getSubCategoriesResponse']['return']
                self.asJson = jsonList
                
                
            except:
                self.asJson = None
                pass

             
            
        
