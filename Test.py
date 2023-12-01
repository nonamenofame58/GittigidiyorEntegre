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
 # örnek erişim (dict)
 #------------------------
 # [CatName] : {
 #  ['specName'] : { 
 #      ['type']     :{}
 #      ['required'] :{}
 #      ['values']   :{}
 # }

#### PARENT CATEGORİES #####

 # getParentCategories(Boolean withSpecs ,Boolean withDeepest , Boolean withCatalog ,String lang, session).Categories                //// Kategorileri getirir (array) 
 # getParentCategories(Boolean withSpecs ,Boolean withDeepest , Boolean withCatalog ,String lang, session).CategoryCodes                //// Kategori kodlarını getirir getirir (array)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #withSpecs: boolean
    #    Eğer true gönderilirse ekstra kategori detay bilgisi gönderilir. false olarak belirtilmişse gönderilmez.
    #withDeepest: boolean
    #    Eğer true gönderilirse kategorinin alt veya ana kategori olduğunu belirten withDeepest parametresi döner. false olarak belirtilmişse bu parametre gönderilmez.
    #withCatalog: boolean
    #    Eğer true gönderilirse katalog durumunu belirten withCatalog parametresi döner. false olarak belirtilmişse bu parametre gönderilmez.
    #lang: String
    #    Olası bir hata anında dönen hata mesajının dilini belirtmek için kullanılır.
    #    Hata mesajı lang=tr ise Türkçe,
    #    lang=en ise İngilizce olarak çıkar.
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # SPECS
    #------------------------
        # *getParentCategories(True,True,True,'tr',session).Specs['Fotoğraf & Kamera']['Marka']['values']
        # >>>['Canon', 'Case Logic', 'Case Logic', 'Dji', 'Duracell', 'Energizer', 'Goldmaster', 'Gp', 'Joby', 'Koala', 'Lomography', 'Nikon', 'Sony', 'Valja', 'Vpw', 'Hongdak', 'Raypro', 'Knmaster...



### SUB CATEGORİES ###
        
    # *getSubCategories(String categoryCode, Boolean withSpecs, Boolean withDeepest, Boolean withCatalog, String lang).Names    //// Alt Kategori isimlerini getirir (array)     /// Kategori kodu gerekir..
    # *getSubCategories(String categoryCode, Boolean withSpecs, Boolean withDeepest, Boolean withCatalog, String lang).Codes    ///// Alt Kategori isim kodlarını getirir (dict) /// kategori kodu gerekir ...
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #categoryCode: String
    #    İstenilen kategorinin kodu.
    #withSpecs: boolean
    #   Eğer true gönderilirse ekstra kategori detay bilgisi gönderilir. false olarak belirtilmişse gönderilmez.
    #withDeepest: boolean
    #    Eğer true gönderilirse kategorinin alt veya ana kategori olduğunu belirten withDeepest parametresi döner. false olarak belirtilmişse bu parametre gönderilmez.
    #withCatalog: boolean
    #    Eğer true gönderilirse katalog durumunu belirten withCatalog parametresi döner. false olarak belirtilmişse bu parametre gönderilmez.
    #lang: String
    #    Olası bir hata anında dönen hata mesajının dilini belirtmek için kullanılır.
    #Hata mesajı lang=tr ise Türkçe,
    #    lang=en ise İngilizce olarak çıkar.
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # SPECS
    #---------------------------
        # *getSubCategories('b',True,True,True,'tr',session).Specs['Dizüstü Bilgisayar (Laptop)']['Marka']['values']
        # >>>['Dizüstü Bilgisayar (Laptop)', 'Dizüstü Bilgisayar (Laptop) Aksesuar', 'Masaüstü (Desktop) Bilgisayar', 'Çevre Birimleri', 'Bilgisayar Bileşenleri', 'Tablet', 'Tablet Akse...
    

### CİTİES ###

    # *getCities(session).names                                                       ///// Şehirleri getirir           (array)
    # *getCities(sessiın).codes                                                      /////  Şehir Kodlarını getirir     (array)
    # *getCities(session).loopCityNames                                                 //  şehir isimlerini döndürür   (loop)
    # *getCities(session).loopCityCodes                                                 //  şehir codlarını döndürür    (loop)
    #------------------------------------------------------------------------------------------------------------------------------------------
    
### CATEGORY ###
    # *getCategory(String categoryCode, boolean withSpecs, boolean withDeepest, boolean withCatalog, String lang, session).Categories    ////   Kategorileri getirir      /// Kategori kodu gerekir..
    # *getCategory(String categoryCode, boolean withSpecs, boolean withDeepest, boolean withCatalog, String lang, session).Code                   //// Kategori kodunu getirir  /// Kategori kodu gerekir..
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # SPECS
    #----------------------------
        # *getCategory('bt',True,True,True,'tr',session).Specs['Elektronik Devre Elemanları']['Ürün Tipi']['values'] 
        # >>> ['Baskılı Devreler', 'Entegreler', 'Klemensler', 'Konnektörler', 'LCD, LED & Display', 'Mikroişlemciler', 'Pasif Devre Elemanları', 'Röleler', 'Servisler için Araç & Gere...

        
### CATEGORY SPCES ###
        
    # getCategorySpecs.Specs(categoryCode,session )   // Kategori speclerini getirir (değişir)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         #  Spec names   *getCategorySpecs().Names               //////     isimleri getirir (array)
         #  Spec values *getCategorySpecs().Values              /////////   değerleri getirir (dict) isime göre değer arraylarını getirmek için     *getCategorySpecs.Values['Marka'] (Array)
         #  Spec types  *getCategorySpecs().Types               //////       tipleri getirir (dict)   isime göre tip getirmek için                  *getCategorySpecs.Types['Marka']
         #  Spec Required *getCategorySpecs().Required          /////       gereklilikleri getirir (dict)  isime göre tip getirmek için             *getCategorySpecs.Required['Marka']
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### DEEPEST CATEGORİES ###
         
    #getDeepestCategories((int startOffSet , int rowCount , boolean withSpecs , String lang , session )
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         # *print( getDeepestCategories(1,2,True,'tr',session).categorySpecs.keys())
               #  >>> dict_keys(['Diğer Antikalar, Sanat', 'Dizüstü Bilgisayar (Laptop)'])
         # *getDeepestCategories(1,2,True,'tr',session).categorySpecs['Diğer Antikalar']
               #  >>>{'code': 'az', 'Listeleyen': {'type': 'Combo', 'required': 'false', 'values': ['Sanatçı', 'Satıcı', 'Diğer']}, 'Orijinal / Reprodüksiyon': {'type': 'Combo', 'required': 'false', 'values': ['Oriji...
         # *getDeepestCategories(1,2,True,'tr',session).categorySpecs['Diğer Antikalar']['Listeleyen']['type']       /// kategori tipi
         #                                                                                                   |/spec ismi /|['required']   //// gereklilik (bool)
         #                                                                       //kodu getirmek için           ['code']    ['values']     //// değerleri
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
                 #*getCategoryVariantSpecs('gd','tr',session).loopValues()             ///    değerleri döndürür                (loop)
                 #*getCategoryVariantSpecs('gd','tr',session).loopOrderNumbers()         //// order numberleri döndürür         (loop)
                 #*getCategoryVariantSpecs('gd','tr',session).loopValueIds()            ///// value ids leri döndürür           (loop)
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### REQUİRED CATALOG SPECS ###
         
         #*getRequiredCategorySpecs(String categoryCode, String lang, session)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                 #*getRequiredCategorySpecs('ngv','tr',session).catalogRequired            /// katalog gerekliliğini getirir           (bool)
                 #*getRequiredCategorySpecs('ngv','tr',session).Count                      /// gerekli katalog spec sayısını getirir   (int)
                 #*getRequiredCategorySpecs('ngv','tr',session).requiredSpecsDict          /// gerekli katalogları getirir             (dict)
                 #*getRequiredCategorySpecs('ngv','tr',session).requiredSpecNames          /// gerekli katalog isimlerini getirir      (array)
                 #*getRequiredCategorySpecs('ngv','tr',session).loopRequiredSpecs()        /// gerekli katalog isimlerini döndürür     (loop)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### CATEGORY SPEC DETAİLS ###

         # *getCategorySpecsWithDetail(String categoryCode, String lang,session)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
             #*getCategorySpecsWithDetail('upf','tr',session).specs                                       /// spec details getirir                   (dict)
             #*getCategorySpecsWithDetail('upf','tr',session).specs['Marka']+/['childSpecId']
             #                                                                ['specId']                  
             #                                                                ['type']
             #                                                                ['required']
             #                                                                ['values']                                                             (array)
             #*getCategorySpecsWithDetail('upf','tr',session).loopSpecNames                              /// spec isimlerini döndürür                (loop)
             #*getCategorySpecsWithDetail('upf','tr',session).loopSpecValueNames                         /// spec değerlerinin isimlerini döndürür   (loop)
             #*getCategorySpecsWithDetail('upf','tr',session).loopSpecValueSpecId                        /// spec değerinin specid ini döndürür      (loop
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            
### GET BALANCES ###
             #*getBalances(String apiKey, String sign, long time, String lang, String startDate, String endDate, int pageNumber, int pageSize,String balanceTransferStatus,session)
             
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
             #apiKey: String
                  #Uygulamanızın anahtarı.
             #sign: String
                #Uygulamanın o anki isteğinin imzası.
             #time: long
                #İşlemin gerçekleştirildiği zaman. ///timeStamp
             #lang: String
                #Olası bir hata anında dönen hata mesajının dilini belirtmek için kullanılır.
             #startDate: String
                #Başlangıç tarihi.
             #endDate: String
                #Bitiş tarihi.
             #pageNumber: Int
                #Kaçıncı sayfadan başlayacak?
             #pageSize: Int
                #Kaç kayıt listelenecek?
             #balanceTransferStatus: String
                #COMPLETED = İşlemi tamamlanmış ve satıcıya aktarılmış para transferleri
             #WAITING_FOR_STATUS = Satıcıya aktarılması beklenen para transferleri
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### GET DEBT COLLECTION ###
             #*getDebtCollection(String apiKey, String sign, long time, String lang, queryDebtCollectionRequest = {'balanceCode' : '' , 'pageNumber' : '' , 'pageSize' : ''} ,session)
             #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            # apiKey: String
                            #      Uygulamanızın anahtarı.
                            # sign: String
                            #       Uygulamanın o anki isteğinin imzası.
                            #  time: long
                            #       O anki zaman.
                            #  lang: String
                            #       Olası bir hata anında dönen hata mesajının dilini belirtmek için kullanılır.
                            #       Hata mesajı lang=tr ise Türkçe,lang=en ise İngilizce olarak çıkar.
                            #  balanceCode: String
                            #       Bakiye kodu.
                            #  pageNumber: Int
                            #       Kaçıncı sayfadan başlayacak?
                            #  pageSize: Int
                            #       Kaç kayıt listelenecek?
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### GET SRS PROCESS SALES ###
                            
                #*getSrsProcessSaleItem(String apiKey, String sign, long time, String lang, getSrsProcessSaleItem = {'balanceCode' : '' , 'pageNumber' : '' , 'pageSize' : ''} ,session)

                #------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #apiKey: String
                #    Uygulamanızın anahtarı.
                #sign: String
                #    Uygulamanın o anki isteğinin imzası.
                #time: long
                #    O anki zaman.
                #lang: String
                #    Olası bir hata anında dönen hata mesajının dilini belirtmek için 
                #kullanılır.
                #    Hata mesajı lang=tr ise Türkçe,
                #    lang=en ise İngilizce olarak çıkar.
                #balanceCode: String
                #    Bakiye kodu.
                #pageNumber: Int
                #    Kaçıncı sayfadan başlayacak?
                #pageSize: Int
                #    Kaç kayıt listelenecek?
                #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
### GET SRS PROCESS DETAILS ###
                #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #*getSrsProcessDetailsSaleItem(apiKey = '',sign = '',time = '',lang = SrsProcessSaleItemRequest {'memberId' : '','pageNumber':'','pageSize':'','salesCode' : ['1','2'],session)
                    #apiKey: String
                    #    Uygulamanızın anahtarı.
                    #sign: String
                    #    Uygulamanın o anki isteğinin imzası.
                    #time: long
                    #    O anki zaman.
                    #lang: String
                    #    Olası bir hata anında dönen hata mesajının dilini belirtmek için 
                    #kullanılır.
                    #    Hata mesajı lang=tr ise Türkçe,
                    #    lang=en ise İngilizce olarak çıkar.
                    #saleCodes: String
                    #    Satış kodu listesi.
                    #pageNumber: Int
                    #    Kaçıncı sayfadan başlayacak?
                    #pageSize: Int
                    #    Kaç kayıt listelenecek?
                #------------------------------------------------------------------------------------------------------------------------------------------------------------------




### DELETE PRODUCT ###
                    
            #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #*deleteProduct(apiKey = '',sign = '',time = '',productIdList = {'item' : []},itemIdList = {},lang = '',session)
                #apiKey: String
                #    Uygulamanızın anahtarı.
                #sign: String
                #    Uygulamanın o anki isteğinin imzası.
                #time: long
                #    İşlemin gerçekleştirildiği zaman.
                #productIdArray: Integer[]
                #    Silinmek istenen ürünlerin tekil anahtar dizisi.
                #itemIdArray: String[]
                #    Silinmek istenen ürünlerin entegrasyon yapan firma tarafındaki ürün tekil anahtar dizisi.
                #lang: String
                #    Olası bir hata anında dönen hata mesajının dilini belirtmek için kullanılır.
                #
                #    Hata mesajı lang=tr ise Türkçe,
                #    lang=en ise İngilizce olarak çıkar.
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






    















