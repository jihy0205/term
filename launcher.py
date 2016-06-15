# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import *

#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Quit program:   q")
    print("기간별 검색: p")
    print("지역별 검색: a")
    print("분류별 검색: r")    
    print("상세정보 검색: g")
    print("----------------------------------------")
    print("send maIl : i")
    print("sTart Web Service: t")
    print("========Menu==========")
    
def launcherFunction(menu):
    if menu ==  'l':
        LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'b':
        PrintBookList(["title",])
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == 'e':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
        
    elif menu == 'a':
        sido = (input('지역 이름(시/도)을 입력하세요: '))
        getAreaData(sido)
        
    elif menu == 'p':
        start = str(input('시작 일자를 입력하세요(20xxmmdd): '))
        end = str(input('끝나는 일자를 입력하세요(20xxmmdd): '))
        getPeriodData(start, end)
    elif menu == 'r':
        code = str(input('분류코드를 입력하세요: \n- 연극/뮤지컬-A000, 국악-B000, 무용-C000, 전시/박물관-D000\n'))
        getRealmData(code)
        
    
    elif menu == 'g': 
        isbn = str(input ('공연/전시 정보의 고유번호를 입력하세요:'))
        #isbn = '0596513984'
        ret = getBookDataFromISBN(isbn)
        AddBook(ret)
    elif menu == 'm':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == 'i':
        sendMain()
    elif menu == "t":
        startWebService()
    else:
        print ("error : unknow menu key")

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()
    
##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")
