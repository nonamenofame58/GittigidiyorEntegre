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




# GETS
from getCategoriesHavingVariantSpecs import getCategoriesHavingVariantSpecs
from getParentCategories import getParentCategories
from getSubCategories import getSubCategories
from getCities import getCities
from getCategory import getCategory
from getCategorySpecs import getCategorySpecs
from getDeepestCategories import getDeepestCategories
from getCategoryVariantSpecs import getCategoryVariantSpecs
from getRequiredCategorySpecs import getRequiredCategorySpecs
from getCategorySpecsWithDetail import getCategorySpecsWithDetail




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

            





apiKey = 'JRJXp3EnpWPWeC6d2NfYVp8kJfa3eH9d'
secretKey = 'VjyzKWAbvBxETyQv'
timeStamp = round(time.time() * 1000)
hashStr = apiKey + secretKey + str(timeStamp)
sign = hashlib.md5(hashStr.encode()).hexdigest()

session = Session()
session.auth = HTTPBasicAuth('ugurcannazli2129', '7qDsZv8KmrzfNP8QNjr6JjfceJXhQyQf')




host = '127.0.0.1'
port = 65432



import pickle
def getParentCategoriesM(data,conn):    
    try:
        print (data)
        jsonData = getParentCategories(False,False,False,'tr',session).asJson
        jsonData = json.dumps(jsonData, indent=2).encode('utf-8')
        conn.sendall(b'getParentCategories')
        time.sleep(0.1)
        conn.sendall(bytes(jsonData))
    except:
        pass
    
    

    
def getSubCategoriesM(data,conn):

    
    data = data.encode('utf-8')

    jsonData = getSubCategories(data,False,False,False,'tr',session).asJson
    if jsonData == None:
        conn.sendall(b'Marka')
        
        jsonData = getCategorySpecs(data,session).asJson[0]
        jsonData = json.dumps(jsonData,indent = 2).encode('utf-8')
        conn.sendall(jsonData)
    else:
            
        jsonData = json.dumps(jsonData,indent = 2).encode('utf-8')
        conn.sendall(b'getSubCategories')
        time.sleep(0.1)
        conn.sendall(jsonData)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print ('Listening')
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.sendall(b'Connected')
        while True:
            data = conn.recv(2048)
            data = data.decode('utf-8')
            if data[:3] == '001':
                getParentCategoriesM(data[3:],conn)
            if data[:3] == '002':
                getSubCategoriesM(data[3:],conn)
            if not data:
                break
            














