import pytz
from datetime import datetime
import os.path
import settings

def readDataFromFile():
    #print("")
    check_file = os.path.exists(settings.filepath)
    if(check_file):
        f = open("./LastPriceDetails.txt", "r")
        str1 = f.read()
        print(str1 + "$$")
        if(str1.strip()!=''):
            print(str1 + "%%")
            return None
        else:
            print(str1 + "^^")
            return None
    else:
        #print(str1 + "##")
        return None

def writeDataToFile(currentprice):
    print("inside writeDataToFile")
    f = open("./LastPriceDetails.txt", "w+")
    f.truncate(0)

    f.write(str(currentprice))
    print("Final String:"+str(currentprice))
    f.close()

#readDataFromFilw()
