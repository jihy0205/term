# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import *

#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Quit program:   q")
    print("�Ⱓ�� �˻�: p")
    print("������ �˻�: a")
    print("�з��� �˻�: r")    
    print("������ �˻�: g")
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
    elif menu == 'a':
        ISBN = str(input ('insert ISBN :'))
        title = str(input ('insert Title :'))
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == 'e':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
        
    elif menu == 'a':
        sido = str(input('���� �̸�(��/��)�� �Է��ϼ���: '))
        gungu = str(input('(��/��)�� �Է��ϼ���: '))
        getAreaData(sido, gungu)
        
    elif menu == 'p':
        start = str(input('���� ���ڸ� �Է��ϼ���: '))
        end = str(input('������ ���ڸ� �Է��ϼ���: '))
        getPeriodData(start, end)
    elif menu == 'r':
        code = str(input('�з��ڵ带 �Է��ϼ���: '))
        getRealmData(code)
        
    
    elif menu == 'g': 
        isbn = str(input ('input isbn to get :'))
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
