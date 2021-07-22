from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class getSaleProcessReportV2:
    def __init__(self,apiKey = '',sign = '',time = '',startDate = '',endDate = '',startOffSet = 2,rowCount = 2,lang = '',session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualSaleService?wsdl", transport=Transport(session=session))
        service = client.create_service('http://sale.individual.ws.listingapi.gg.com}IndividualSaleServiceBinding' , 'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualSaleService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.getSaleProcessReportV2(apiKey,sign,time,startDate,endDate,startOffSet,rowCount,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:getSaleProcessReportV2Response']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
