from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from zeep.exceptions import Fault
from zeep.wsse.username import UsernameToken
import time
import hashlib
import requests
import json
from zeep import xsd
import xmltodict
import socket





# Application Service

from createApplication import createApplication
from deleteApplication import deleteApplication
from getApplicationList import getApplicationList

# Category Service

from getCategoriesHavingVariantSpecs import getCategoriesHavingVariantSpecs
from getParentCategories import getParentCategories
from getSubCategories import getSubCategories
from getCategory import getCategory
from getCategorySpecs import getCategorySpecs
from getDeepestCategories import getDeepestCategories
from getCategoryVariantSpecs import getCategoryVariantSpecs
from getRequiredCategorySpecs import getRequiredCategorySpecs
from getCategorySpecsWithDetail import getCategorySpecsWithDetail

# City Service

from getCities import getCities
from getModifiedCities import getModifiedCities
from getCity import getCity
from getCitiesByCodes import getCitiesByCodes

# Developer Service
from registerDeveloper import registerDeveloper
from isDeveloper import isDeveloper

# Catalog Service

from searchCatalog import searchCatalog

# Search Service

from search import search


# Accounting Service

from getBalances import getBalances
from getDebtCollection import getDebtCollection
from getSrsProcessSaleItem import getSrsProcessSaleItem
from getSrsProcessDetailsSaleItem import getSrsProcessDetailsSaleItem

# Product Service

from cloneProduct import cloneProduct
from deleteProduct import deleteProduct
from getNewlyListedProductIdList import getNewlyListedProductIdList
from calculatePriceForShoppingCart import calculatePriceForShoppingCart
from getProduct import getProduct
from updateStock import updateStock
from updateVariantStock import updateVariantStock
from relistProducts import relistProducts
from getStockAndPrice import getStockAndPrice
from getProductDescription import getProductDescription
from getProductSpecs import getProductSpecs
from updatePriceByPercentage import updatePriceByPercentage
from updateProductWithNewCargoDetail import updateProductWithNewCargoDetail
from getProductsByIds import getProductsByIds
from getProductIds import getProductIds
from checkForItemId import checkForItemId
from getProductStatuses import getProductStatuses
from updateItemId import updateItemId
from updateProductVariants import updateProductVariants
from getProductVariants import getProductVariants
from updateStockAndActivateProduct import updateStockAndActivateProduct
from updateMarketPrice import updateMarketPrice
from updateVariantStockAndActivateProduct import updateVariantStockAndActivateProduct
from getItemIdDetails import getItemIdDetails
from updateProductSales import updateProductSales
from applySameDayDeliveryFeature import applySameDayDeliveryFeature

# Product Option Service

from getOptionFeaturesInfo import getOptionFeaturesInfo
from addOptionsToCart import addOptionsToCart
from removeOptionsFromCart import removeOptionsFromCart
from calculateOptionsPrice import calculateOptionsPrice
from payPrice import payPrice

# Sale Service

from getPagedSales import getPagedSales
from getSale import getSale
from getSalesByDateRange import getSalesByDateRange
from giveRateAndComment import giveRateAndComment
from replySaleComment import replySaleComment
from remindForApproval import remindForApproval
from getReasonsToCancelSale import getReasonsToCancelSale
from cancelSale import cancelSale
from getAccountTransactionsV3 import getAccountTransactionsV3
from getSaleProcessReportV2 import getSaleProcessReportV2
from removeSaleFromList import removeSaleFromList
from getItemBuyers import getItemBuyers
from receiveRemandedItem import receiveRemandedItem
from giveApprovalForRemandedItem import giveApprovalForRemandedItem
from cancelSaleAfterEarlyCancellationRequest import cancelSaleAfterEarlyCancellationRequest

# User Messages Service

from getConversations import getConversations
from getConversationsCount import getConversationsCount
from getMessages import getMessages
from getConversationById import getConversationById
from postConversation import postConversation
from putMessage import putMessage
from markAsUnread import markAsUnread
from markAsRead import markAsRead
from deleteConversation import deleteConversation
from deleteConversations import deleteConversations

# Cargo Service

from getCargoInformation import getCargoInformation
from sendCargoInformation import sendCargoInformation
from getCargoCompany import getCargoCompany
from createShippingRequest import createShippingRequest
from cancelShippingRequest import cancelShippingRequest
from getShippingRequest import getShippingRequest
from getUserShippingAgreements import getUserShippingAgreements
from getShippingAgreementContent import getShippingAgreementContent
from cancelShipment import cancelShipment

# Activity Service
from getUnsoldItems import getUnsoldItems
from getSoldItems import getSoldItems
from getWatchItems import getWatchItems

# Store Service

from getStore import getStore












### JSON ###
# .asJson       ////// Json olarak getirir



# *********** SPECS
 # ??rnek eri??im (dict)
 #------------------------
 # [CatName] : {
 #  ['specName'] : { 
 #      ['type']     :{}
 #      ['required'] :{}
 #      ['values']   :{}
 # }

#### PARENT CATEGOR??ES #####

 # getParentCategories(Boolean withSpecs ,Boolean withDeepest , Boolean withCatalog ,String lang, session).Categories                //// Kategorileri getirir (array) 
 # getParentCategories(Boolean withSpecs ,Boolean withDeepest , Boolean withCatalog ,String lang, session).CategoryCodes                //// Kategori kodlar??n?? getirir getirir (array)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #withSpecs: boolean
    #    E??er true g??nderilirse ekstra kategori detay bilgisi g??nderilir. false olarak belirtilmi??se g??nderilmez.
    #withDeepest: boolean
    #    E??er true g??nderilirse kategorinin alt veya ana kategori oldu??unu belirten withDeepest parametresi d??ner. false olarak belirtilmi??se bu parametre g??nderilmez.
    #withCatalog: boolean
    #    E??er true g??nderilirse katalog durumunu belirten withCatalog parametresi d??ner. false olarak belirtilmi??se bu parametre g??nderilmez.
    #lang: String
    #    Olas?? bir hata an??nda d??nen hata mesaj??n??n dilini belirtmek i??in kullan??l??r.
    #    Hata mesaj?? lang=tr ise T??rk??e,
    #    lang=en ise ??ngilizce olarak ????kar.
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # SPECS
    #------------------------
        # *getParentCategories(True,True,True,'tr',session).Specs['Foto??raf & Kamera']['Marka']['values']
        # >>>['Canon', 'Case Logic', 'Case Logic', 'Dji', 'Duracell', 'Energizer', 'Goldmaster', 'Gp', 'Joby', 'Koala', 'Lomography', 'Nikon', 'Sony', 'Valja', 'Vpw', 'Hongdak', 'Raypro', 'Knmaster...



### SUB CATEGOR??ES ###
        
    # *getSubCategories(String categoryCode, Boolean withSpecs, Boolean withDeepest, Boolean withCatalog, String lang).Names    //// Alt Kategori isimlerini getirir (array)     /// Kategori kodu gerekir..
    # *getSubCategories(String categoryCode, Boolean withSpecs, Boolean withDeepest, Boolean withCatalog, String lang).Codes    ///// Alt Kategori isim kodlar??n?? getirir (dict) /// kategori kodu gerekir ...
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #categoryCode: String
    #    ??stenilen kategorinin kodu.
    #withSpecs: boolean
    #   E??er true g??nderilirse ekstra kategori detay bilgisi g??nderilir. false olarak belirtilmi??se g??nderilmez.
    #withDeepest: boolean
    #    E??er true g??nderilirse kategorinin alt veya ana kategori oldu??unu belirten withDeepest parametresi d??ner. false olarak belirtilmi??se bu parametre g??nderilmez.
    #withCatalog: boolean
    #    E??er true g??nderilirse katalog durumunu belirten withCatalog parametresi d??ner. false olarak belirtilmi??se bu parametre g??nderilmez.
    #lang: String
    #    Olas?? bir hata an??nda d??nen hata mesaj??n??n dilini belirtmek i??in kullan??l??r.
    #Hata mesaj?? lang=tr ise T??rk??e,
    #    lang=en ise ??ngilizce olarak ????kar.
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # SPECS
    #---------------------------
        # *getSubCategories('b',True,True,True,'tr',session).Specs['Diz??st?? Bilgisayar (Laptop)']['Marka']['values']
        # >>>['Diz??st?? Bilgisayar (Laptop)', 'Diz??st?? Bilgisayar (Laptop) Aksesuar', 'Masa??st?? (Desktop) Bilgisayar', '??evre Birimleri', 'Bilgisayar Bile??enleri', 'Tablet', 'Tablet Akse...
    

### C??T??ES ###

    # *getCities(session).names                                                       ///// ??ehirleri getirir           (array)
    # *getCities(sessi??n).codes                                                      /////  ??ehir Kodlar??n?? getirir     (array)
    # *getCities(session).loopCityNames                                                 //  ??ehir isimlerini d??nd??r??r   (loop)
    # *getCities(session).loopCityCodes                                                 //  ??ehir codlar??n?? d??nd??r??r    (loop)
    #------------------------------------------------------------------------------------------------------------------------------------------
    
### CATEGORY ###
    # *getCategory(String categoryCode, boolean withSpecs, boolean withDeepest, boolean withCatalog, String lang, session).Categories    ////   Kategorileri getirir      /// Kategori kodu gerekir..
    # *getCategory(String categoryCode, boolean withSpecs, boolean withDeepest, boolean withCatalog, String lang, session).Code                   //// Kategori kodunu getirir  /// Kategori kodu gerekir..
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # SPECS
    #----------------------------
        # *getCategory('bt',True,True,True,'tr',session).Specs['Elektronik Devre Elemanlar??']['??r??n Tipi']['values'] 
        # >>> ['Bask??l?? Devreler', 'Entegreler', 'Klemensler', 'Konnekt??rler', 'LCD, LED & Display', 'Mikroi??lemciler', 'Pasif Devre Elemanlar??', 'R??leler', 'Servisler i??in Ara?? & Gere...

        
### CATEGORY SPCES ###
        
    # getCategorySpecs.Specs(categoryCode,session )   // Kategori speclerini getirir (de??i??ir)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         #  Spec names   *getCategorySpecs().Names               //////     isimleri getirir (array)
         #  Spec values *getCategorySpecs().Values              /////////   de??erleri getirir (dict) isime g??re de??er arraylar??n?? getirmek i??in     *getCategorySpecs.Values['Marka'] (Array)
         #  Spec types  *getCategorySpecs().Types               //////       tipleri getirir (dict)   isime g??re tip getirmek i??in                  *getCategorySpecs.Types['Marka']
         #  Spec Required *getCategorySpecs().Required          /////       gereklilikleri getirir (dict)  isime g??re tip getirmek i??in             *getCategorySpecs.Required['Marka']
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### DEEPEST CATEGOR??ES ###
         
    #getDeepestCategories((int startOffSet , int rowCount , boolean withSpecs , String lang , session )
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         # *print( getDeepestCategories(1,2,True,'tr',session).categorySpecs.keys())
               #  >>> dict_keys(['Di??er Antikalar, Sanat', 'Diz??st?? Bilgisayar (Laptop)'])
         # *getDeepestCategories(1,2,True,'tr',session).categorySpecs['Di??er Antikalar']
               #  >>>{'code': 'az', 'Listeleyen': {'type': 'Combo', 'required': 'false', 'values': ['Sanat????', 'Sat??c??', 'Di??er']}, 'Orijinal / Reprod??ksiyon': {'type': 'Combo', 'required': 'false', 'values': ['Oriji...
         # *getDeepestCategories(1,2,True,'tr',session).categorySpecs['Di??er Antikalar']['Listeleyen']['type']       /// kategori tipi
         #                                                                                                   |/spec ismi /|['required']   //// gereklilik (bool)
         #                                                                       //kodu getirmek i??in           ['code']    ['values']     //// de??erleri
         #

### CATEGORY VARIANT SPECS ###
         # *getCategoryVariantSpecs(String categoryCode, String lang , session) // Sub category code //
             #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                 #*getCategoryVariantSpecs('gd','tr',session).specBase                  ////  spec base code                    (bool)
                 #*getCategoryVariantSpecs('gd','tr',session).specType                  ////  spec type
                 #*getCategoryVariantSpecs('gd','tr',session).specName                  ////  spec name
                 #*getCategoryVariantSpecs('gd','tr',session).specNameId                ///   spec name ID
                 #*getCategoryVariantSpecs('gd','tr',session).specValuesDict             ///  spec values                       (dict)
                 #*getCategoryVariantSpecs('gd','tr',session).specValues                ////  spec values                       (array)
                 #*getCategoryVariantSpecs('gd','tr',session).specOrderNumbers         ////// spec Order Numbers                (array)
                 #*getCategoryVariantSpecs('gd','tr',session).specValueIds              ///// spec Value ids                    (array)
                 #*getCategoryVariantSpecs('gd','tr',session).loopValues()             ///    de??erleri d??nd??r??r                (loop)
                 #*getCategoryVariantSpecs('gd','tr',session).loopOrderNumbers()         //// order numberleri d??nd??r??r         (loop)
                 #*getCategoryVariantSpecs('gd','tr',session).loopValueIds()            ///// value ids leri d??nd??r??r           (loop)
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### REQU??RED CATALOG SPECS ###
         
         #*getRequiredCategorySpecs(String categoryCode, String lang, session)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                 #*getRequiredCategorySpecs('ngv','tr',session).catalogRequired            /// katalog gereklili??ini getirir           (bool)
                 #*getRequiredCategorySpecs('ngv','tr',session).Count                      /// gerekli katalog spec say??s??n?? getirir   (int)
                 #*getRequiredCategorySpecs('ngv','tr',session).requiredSpecsDict          /// gerekli kataloglar?? getirir             (dict)
                 #*getRequiredCategorySpecs('ngv','tr',session).requiredSpecNames          /// gerekli katalog isimlerini getirir      (array)
                 #*getRequiredCategorySpecs('ngv','tr',session).loopRequiredSpecs()        /// gerekli katalog isimlerini d??nd??r??r     (loop)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### CATEGORY SPEC DETA??LS ###

         # *getCategorySpecsWithDetail(String categoryCode, String lang,session)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
             #*getCategorySpecsWithDetail('upf','tr',session).specs                                       /// spec details getirir                   (dict)
             #*getCategorySpecsWithDetail('upf','tr',session).specs['Marka']+/['childSpecId']
             #                                                                ['specId']                  
             #                                                                ['type']
             #                                                                ['required']
             #                                                                ['values']                                                             (array)
             #*getCategorySpecsWithDetail('upf','tr',session).loopSpecNames                              /// spec isimlerini d??nd??r??r                (loop)
             #*getCategorySpecsWithDetail('upf','tr',session).loopSpecValueNames                         /// spec de??erlerinin isimlerini d??nd??r??r   (loop)
             #*getCategorySpecsWithDetail('upf','tr',session).loopSpecValueSpecId                        /// spec de??erinin specid ini d??nd??r??r      (loop
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            
### GET BALANCES ###
             #*getBalances(String apiKey, String sign, long time, String lang, String startDate, String endDate, int pageNumber, int pageSize,String balanceTransferStatus,session)
             
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
             #apiKey: String
                  #Uygulaman??z??n anahtar??.
             #sign: String
                #Uygulaman??n o anki iste??inin imzas??.
             #time: long
                #????lemin ger??ekle??tirildi??i zaman. ///timeStamp
             #lang: String
                #Olas?? bir hata an??nda d??nen hata mesaj??n??n dilini belirtmek i??in kullan??l??r.
             #startDate: String
                #Ba??lang???? tarihi.
             #endDate: String
                #Biti?? tarihi.
             #pageNumber: Int
                #Ka????nc?? sayfadan ba??layacak?
             #pageSize: Int
                #Ka?? kay??t listelenecek?
             #balanceTransferStatus: String
                #COMPLETED = ????lemi tamamlanm???? ve sat??c??ya aktar??lm???? para transferleri
             #WAITING_FOR_STATUS = Sat??c??ya aktar??lmas?? beklenen para transferleri
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### GET DEBT COLLECTION ###
             #*getDebtCollection(String apiKey, String sign, long time, String lang, queryDebtCollectionRequest = {'balanceCode' : '' , 'pageNumber' : '' , 'pageSize' : ''} ,session)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            # apiKey: String
                            #      Uygulaman??z??n anahtar??.
                            # sign: String
                            #       Uygulaman??n o anki iste??inin imzas??.
                            #  time: long
                            #       O anki zaman.
                            #  lang: String
                            #       Olas?? bir hata an??nda d??nen hata mesaj??n??n dilini belirtmek i??in kullan??l??r.
                            #       Hata mesaj?? lang=tr ise T??rk??e,lang=en ise ??ngilizce olarak ????kar.
                            #  balanceCode: String
                            #       Bakiye kodu.
                            #  pageNumber: Int
                            #       Ka????nc?? sayfadan ba??layacak?
                            #  pageSize: Int
                            #       Ka?? kay??t listelenecek?
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### GET SRS PROCESS SALES ###
                            
                #*getSrsProcessSaleItem(String apiKey, String sign, long time, String lang, getSrsProcessSaleItem = {'balanceCode' : '' , 'pageNumber' : '' , 'pageSize' : ''} ,session)

                #------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #apiKey: String
                #    Uygulaman??z??n anahtar??.
                #sign: String
                #    Uygulaman??n o anki iste??inin imzas??.
                #time: long
                #    O anki zaman.
                #lang: String
                #    Olas?? bir hata an??nda d??nen hata mesaj??n??n dilini belirtmek i??in 
                #kullan??l??r.
                #    Hata mesaj?? lang=tr ise T??rk??e,
                #    lang=en ise ??ngilizce olarak ????kar.
                #balanceCode: String
                #    Bakiye kodu.
                #pageNumber: Int
                #    Ka????nc?? sayfadan ba??layacak?
                #pageSize: Int
                #    Ka?? kay??t listelenecek?
                #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
### GET SRS PROCESS DETAILS ###
                #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #*getSrsProcessDetailsSaleItem(apiKey = '',sign = '',time = '',lang = SrsProcessSaleItemRequest {'memberId' : '','pageNumber':'','pageSize':'','salesCode' : ['1','2'],session)
                    #apiKey: String
                    #    Uygulaman??z??n anahtar??.
                    #sign: String
                    #    Uygulaman??n o anki iste??inin imzas??.
                    #time: long
                    #    O anki zaman.
                    #lang: String
                    #    Olas?? bir hata an??nda d??nen hata mesaj??n??n dilini belirtmek i??in 
                    #kullan??l??r.
                    #    Hata mesaj?? lang=tr ise T??rk??e,
                    #    lang=en ise ??ngilizce olarak ????kar.
                    #saleCodes: String
                    #    Sat???? kodu listesi.
                    #pageNumber: Int
                    #    Ka????nc?? sayfadan ba??layacak?
                    #pageSize: Int
                    #    Ka?? kay??t listelenecek?
                #------------------------------------------------------------------------------------------------------------------------------------------------------------------




### DELETE PRODUCT ###
                    
            #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #*deleteProduct(apiKey = '',sign = '',time = '',productIdList = {'item' : []},itemIdList = {},lang = '',session)
                #apiKey: String
                #    Uygulaman??z??n anahtar??.
                #sign: String
                #    Uygulaman??n o anki iste??inin imzas??.
                #time: long
                #    ????lemin ger??ekle??tirildi??i zaman.
                #productIdArray: Integer[]
                #    Silinmek istenen ??r??nlerin tekil anahtar dizisi.
                #itemIdArray: String[]
                #    Silinmek istenen ??r??nlerin entegrasyon yapan firma taraf??ndaki ??r??n tekil anahtar dizisi.
                #lang: String
                #    Olas?? bir hata an??nda d??nen hata mesaj??n??n dilini belirtmek i??in kullan??l??r.
                #
                #    Hata mesaj?? lang=tr ise T??rk??e,
                #    lang=en ise ??ngilizce olarak ????kar.
            #--------------------------------------------------------------------------------------------------------------------------------------------------------------------




### Api key ###
             
apiKey = ''

### Secret Key ###
secretKey = ''


timeStamp = round(time.time() * 1000)
hashStr = apiKey + secretKey + str(timeStamp)
sign = hashlib.md5(hashStr.encode()).hexdigest()

session = Session()


### Auth Role Name ve Password
session.auth = HTTPBasicAuth('', '')






    















