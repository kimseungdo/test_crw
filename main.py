import os
import time

from openpyxl import load_workbook
from datetime import date, datetime
prevtime = time.time()

path = './'
print(os.path.dirname(path))

fileEX = load_workbook(filename = 'test.xlsx')
Sheet1 = fileEX['Sheet1']

# url = https://www1.president.go.kr/petitions/584936
# 개재앙 씹재앙

# def __init__program():


    
def what_time_now():
    day = datetime.now()
    return str('{0.year:04}{0.month:02}{0.day:02}_{0.hour:02}h{0.minute:02}m{0.second:02}s'.format(day) )

if __name__ == "__main__":
    print(type(fileEX))

    Sheet1['A1'] = 'jhel'
    
    print(Sheet1['A1'].value)
    
    fileEX.save(filename=fileEX)
    
    fileEX.close()
    print(what_time_now())
    print("걸린시간이여 : %0.5f" %(time.time() - prevtime) )
    
