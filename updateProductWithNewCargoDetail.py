from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from zeep import helpers
import xmltodict
import json


class updateProductWithNewCargoDetail:
    def __init__(self,apiKey = '',sign = '',time = '' ,itemId = '',productId = '',ProductType = {'categoryCode' : '','title' : '','subtitle' : '','specs' :{'spec' : []},'photos' : {'photoId' : '','url' : '','pageTemplate' : '','description' : '','startDate' : '' , 'catalogFilter' : '','format' : 'S', 'buyNowPrice' : '','listingDays' : '','productCount' : '','cargoDetail' : {'city' : '','cargoCompanies':{'cargoCompany' : ''},'shippingPayment' : '','shippingWhere' : '' , 'cargoCompanyDetails' : {'cargoCompanyDetail' : {'name' : '','cityPrice' : '' ,'countryPrice' : ''}}, 'shippingTime' : {'days' : 'tomorrow','beforeTime' : ''}},'boldOption' : '','catalogOption' : '','vitrineOption' : '','marketPrice' : '','globalTradeItemNo' : '','manufacturerPartNo' : ''}},onSale = False,forceToSpecEntry = False,nextDateOption = False ,session = None):

        # Zeep Client

        client = Client(wsdl="https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductService?wsdl", transport=Transport(session=session))
        service = client.create_service('{https://product.individual.ws.listingapi.gg.com}IndividualProductServiceBinding' , 'https://dev.gittigidiyor.com:8443/listingapi/ws/IndividualProductService')
        with client.settings(raw_response=True):
            try:
                response = helpers.serialize_object(service.updateProductWithNewCargoDetail(apiKey,sign,time,itemId,productId,ProductType,onSale,forceToSpecEntry,nextDateOption,lang).content.decode('utf-8'),dict)
                #Parsing...

             
                jsondata = xmltodict.parse(response)
                jsondump = json.dumps(jsondata)
                jsonload = json.loads(jsondump)

                jsonList = jsonload['env:Envelope']['env:Body']['ns0:updateProductWithNewCargoDetailResponse']['return']
                self.asJson = jsonList
            except:
                self.asJson = None
                pass
            

                 
             
            
        
