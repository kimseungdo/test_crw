# -*- coding:UTF-8 -*-
import os, time
import requests
import pandas

from bs4 import BeautifulSoup
from openpyxl import load_workbook
from datetime import date, datetime

'''
url pattern

https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=1
https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=2

https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&LH_ItemCondition=3&_pgn=1 ~~~ New Condition 처리

"https://www.ebay.com/sch/i.html?_from=R40&_nkw=" kf94+mask "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=" 2
"https://www.ebay.com/sch/i.html?_from=R40&_nkw=" kf94+mask "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc" &LH_ItemCondition=3 "&_pgn=" 1 
                                                 ~KEY_WORD~                                                                                ~PAGE_INDEX 
https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=2
                                               +KEY_WORD                                               +CONDITION / NONE or &LH_ItemCondition=3
                                                                                                                           +PAGE_INDEX
class="s-item__title s-item__title--has-tags" # h3 class="s-item__title
class="s-item__location s-item__itemLocation" # span class="s-item__location 
class="s-item__price" # span class="s-item__price


name = SOUP.find("h3", {"class": "s-item__title"}).get_text(separator=u" ")
price = SOUP.find("span", {"class": "s-item__price"}).get_text()
location = SOUP.find("span", {"class": "s-item__location"}).get_text()
    
print(name + "  " + price + "  " + location + "\n")
'''

KEY_WORD = "kf94+mask" # 공백자는 중간에 + 붙일것
PAGE_INDEX = 1
#URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + KEY_WORD +  "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=" + str(PAGE_INDEX)


prevtime = time.time()
now = datetime.now()
def What_time_now():  
    day = datetime.now()
    return str('{0.year:04}{0.month:02}{0.day:02}_{0.hour:02}h{0.minute:02}m{0.second:02}s'.format(day) )


if __name__ == "__main__":

    '''
    URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + KEY_WORD + "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&LH_ItemCondition=3&_pgn=" + str(PAGE_INDEX) #신제품 검색시 
    #URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + KEY_WORD +  "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=" + str(PAGE_INDEX)


    res = requests.get(URL)
    web = res.text
    SOUP = BeautifulSoup(web, 'html.parser')

    KF_title = SOUP.select('.s-item__title')
    KF_country = SOUP.select('.s-item__location')
    KF_price = SOUP.select('.s-item__price')
    
    
    print(str(enumerate(KF_price)) + " " +str(len(KF_price)) + str(type(KF_price)) )
    a=1
    
    for n in range(len(KF_title)):
        print(str(a)+ "   " + str(KF_title[n].get_text()) + "  " + str(KF_price[n].get_text()) + "  " + str(KF_country[n].get_text()) )
        a+=1

    '''
    Ltotal_kf_info = []

    Dtotal_kf_info = {}
    Lkf_title = []
    Lkf_price = []
    Lkf_country = []
    
    total = 1
    while PAGE_INDEX <= 15:
        URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + KEY_WORD + "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&LH_ItemCondition=3&_pgn=" + str(PAGE_INDEX) #신제품 검색시
        
        a=1

        res = requests.get(URL)
        web = res.text
        SOUP = BeautifulSoup(web, 'html.parser')

        KF_title = SOUP.select('.s-item__title')
        KF_country = SOUP.select('.s-item__location')
        KF_price = SOUP.select('.s-item__price')

        Lkf_info = []
        for n in range(len(KF_title)):
            #print("page : " + str(PAGE_INDEX) + "  index : " + str(a)+ "  " + str(total) + "   " + str(KF_title[n].get_text()) + "  " + str(KF_price[n].get_text()) + "  " + str(KF_country[n].get_text()) )
    
            Lkf_info.append(KF_title[n].get_text())
            Lkf_info.append(KF_price[n].get_text())
            Lkf_info.append(KF_country[n].get_text())

            Lkf_title.append(KF_title[n].get_text())
            Lkf_price.append(KF_price[n].get_text())
            Lkf_country.append(KF_country[n].get_text())
            
            a+=1
            total+=1

        
        Ltotal_kf_info.append(Lkf_info)
        Dtotal_kf_info = {"title" : Lkf_title, "price" : Lkf_price, "country" : Lkf_country}
        df = pandas.DataFrame(Dtotal_kf_info)
        
        PAGE_INDEX += 1

    outputFileName = '%sy%sm%sd %sh%sm%ss 마스크 수탈기록.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    df.to_excel(outputFileName, sheet_name='sheet1')
    
    print("걸린시간이여 : %0.5f" %(time.time() - prevtime) )
    print("총 반출 : " + str(total))
