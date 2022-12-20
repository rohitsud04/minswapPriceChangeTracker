import pytz
from datetime import datetime

def readDataFromFile():
    #print("")
    f = open("./LastPriceDetails.txt", "r")
    str1 = f.read()
    #print(str1)
    return str1

def writeDataToFile(currentprice):
    print("inside writeDataToFile")
    f = open("./LastPriceDetails.txt", "w+")
    f.truncate(0)

    f.write(str(currentprice))
    print("Final String:"+str(currentprice))
    f.close()

#readDataFromFilw()
