# -*- coding:UTF-8 -*-
import os, time
import urllib.request

from bs4 import BeautifulSoup
from openpyxl import load_workbook
from datetime import date, datetime
'''
url pattern

https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=1

https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&LH_ItemCondition=3&_pgn=1 ~~~ New Condition 처리
https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=2

https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc 
https://www.ebay.com/sch/i.html?_from=R40&_nkw=kf94+mask&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=2
                                               +KEY_WORD                                               +CONDITION / NONE or &LH_ItemCondition=3
                                                                                                                           +PAGE_INDEX
condition 처리 + &LH_ItemCondition=3&_png=1

"https://www.ebay.com/sch/i.html?_from=R40&_nkw=" kf94+mask "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=" 2
"https://www.ebay.com/sch/i.html?_from=R40&_nkw=" kf94+mask "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc" &LH_ItemCondition=3 "&_pgn=" 1 
'''

KEY_WORD = "kf94+mask" #띄어쓰기시 중간에 + 붙일것 
CONDITION = None
#CONDITION = "&LH_ItemCondition=3" 신제품 검색시
PAGE_INDEX = 1

#URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + KEY_WORD + "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc" + CONDITION + "&_pgn=" + str(PAGE_INDEX)
URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + KEY_WORD +  "&_sacat=0&LH_TitleDesc=0&_sop=12&LH_All=1&rt=nc&_pgn=" + str(PAGE_INDEX)
prevtime = time.time()

    
if __name__ == "__main__":


    print("걸린시간이여 : %0.5f" %(time.time() - prevtime) )
