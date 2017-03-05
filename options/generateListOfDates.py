import datetime
import time

def ListOf30DaysAhead():
    a = datetime.date.today()
    numdays = 30
    dateList = []
    for x in range (0, numdays):
        dateList.append(a + datetime.timedelta(days = x))
    #print (dateList)

    textList=[]
    for i in dateList:
        text=(str(i.isoformat()))
        textList.append(text)
    print (textList)
    return(textList)

ListOf30DaysAhead()