"""
A project using sql database accessed with python3 language .
In this program you can make a bookshelf for yourself 
It can open url ordering books
It uses a website to fetch data using book ISBN address
"""
import requests as req
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import webbrowser as wb
import logging
try:
    from termcolor import colored , cprint
except:
    print("[-] Kindly install \'termcolor\' python module")
try:
    import mysql.connector as ms
except:
    print("[-] Kindly install \'mysq.connector\' python module")

cprint("+"*60,'red','on_white',attrs=[])
cprint(r"""                                             
        |```````\    /`````\     /`````\    |    /
        |       /   |       |   |       |   |   /
        |------     |       |   |       |   |__/
        |       \   |       |   |       |   |   \
        |_______/    \_____/     \_____/    |    \    """,'cyan',attrs=['bold'])
cprint(r"""
        |           /`````\     /`````\    |    /
        |          |       |   |       |   |   /
        |          |       |   |       |   |__/
        |          |       |   |       |   |   \
        |======     \_____/     \_____/    |    \   -By SG
        """,'cyan',attrs=['bold'])
cprint("+"*60,'red','on_white',attrs=[])
print("""THIS IS A BOOK FINDING AND ORDRING SOFTWARE""")
cprint("NOTE: INTERNET CONNECTION IS REQUIRED ",'yellow')
print("""
    ENTER 
    1. To search a book by its TITLE 
    2. To search a book by its ISBN code
    3. For Books Recommendations
    4. Manage your Bookshelf
    5. Search History
    6. For instructions to use
    0. To exit 
""")
logging.basicConfig(filename='.history.log',level=logging.DEBUG,format='%(message)s')
try:
    choice = int(input('[choice]:> '))
    logging.debug(choice)
    if choice>6:
        cprint("\n[-] Error : OUT OF RANGE VALUE \nTry again!!", 'red',attrs=['bold','blink'])
except:
    cprint("\n[-] Error : Invalid request...", 'red',attrs=['bold','blink'])
    choice=0

def connect(host='https://www.google.com'):
    try:
        ur.urlopen(host)
        return True
    except:
        return False
def joins(l):
    s=''
    for i in l:
        s=s+i+' '
    return s

def bk_manage():
    #try:
        print("""This is BOOK MANAGEMENT SECTION 
        Books are managed using SQL database system
        Install mysql in your system and enter details...""")
        
        hst=input("Enter host name: ")
        usr= input("Enter user name: ")
        paswd= input("Enter password : ")
        db= input("Enter database name: ")
        logging.debug(hst+'\n'+usr+'\n'+paswd+'\n'+db)
        mycon=ms.connect(host=hst, user=usr, passwd=paswd, database=db)
        if mycon.is_connected():
            print("[+] Database connectivity successful :)")
            cursor= mycon.cursor()
            cursor.execute("create table if not exists bookshelf(title char(25),author_name char(25), isbn char(15), genre varchar(50));")
            mycon.commit()
            cursor.execute("select * from bookshelf;")
            data= cursor.fetchall()
            for i in data:
                print(i[0],'  ',i[1],'  ', i[2], '  ', i[3])
            print("Setup Complete ... ")
            while True:
                print()
                cursor.execute("create table if not exists bookshelf(title char(25),author_name char(25), isbn char(15), genre varchar(50));")
                mycon.commit()
                print(
                    """Type 
                    1. to insert data
                    2. to display data
                    3. to update data
                    4. to delete data
                    5. to delete bookshelf
                    0. for exit"""
                )
                try:
                    ch2= int(input("[choice]:> "))
                    logging.debug(ch2)
                except:
                    print("try again")
                if ch2== 1:
                    n=int(input("How many book details you want to enter ? "))
                    for i in range(n):                        
                        b_name= input("Enter book name: ")
                        authn= input("Enter book author name: ")
                        isbn2= input("Enter isbn number: ")
                        genre= input("Enter book genre : ")
                        cursor.execute(f"insert into bookshelf values(\'{b_name}\',\'{authn}\',\'{isbn2}\',\'{genre}\');")
                        logging.debug(b_name+'\n'+authn+'\n'+isbn2+'\n'+genre)
                        mycon.commit()
                elif ch2==2:
                    cursor.execute("select * from bookshelf;")
                    data= cursor.fetchall()
                    for i in data:
                        print(i)
                elif ch2==3:
                    print("Book name cannot be updated ....")
                    nb_name=input("Enter book name to update: ")
                    con= input("What do you want to update ? ")
                    logging.debug(nb_name)
                    if con.lower()=='y':
                        isb=input("Enter new isbn number: ")
                        authna=input("Entre new author name: ")
                        gen= input("Enter new genre: ")
                        cursor.execute(f"update bookshelf set isbn=\'{isb}\', author_name=\'{authna}\' , genre= \'{gen}\' where title=\'{nb_name}\'; ")
                        mycon.commit()
                        cursor.execute("select * from bookshelf;")
                        logging.debug(isb)
                        logging.debug(authna)
                        logging.debug(gen)
                        d= cursor.fetchall()
                        for i in d:
                            print(i)
                elif ch2==4:
                    db_name=input("Enter book name to delete : ")
                    logging.debug(db_name)
                    cursor.execute(f"delete from bookshelf where title=\'{db_name}\';")
                    mycon.commit()
                    cursor.execute("select * from bookshelf;")
                    d= cursor.fetchall()
                    for i in d:
                        print(i)
                elif ch2==5:
                    d=input("Do you want to delete bookshelf [\'y\',\'n\']: ")
                    if d.lower()=='y':
                        cursor.execute("drop table if exists bookshelf;")
                        mycon.commit()
                elif ch2==0:
                    raise KeyboardInterrupt
                else:
                    print("Try again")
        else:
            print("[-] Database connectivity unsuccesfull :(")
        
    #except:
    #    cprint("[-] Error: Database error....",'red' ,attrs=['blink'])
          
def title_search(title):
    n_title= title.replace(" ","%2B")   #FLAG
    url="https://isbndb.com/search/books/"+n_title
    response = req.get(url)
    data= response.content
    soup= bs(data, 'html.parser')
    text= soup.get_text()            #FLAG
    with open(".chache.txt","w") as my:
        my.write(text)
    print()
    display()
    print()
    order()

def isbns(isbn):
    url="https://isbndb.com/search/books/"+isbn     #FLAG 
    try:
        response = req.get(url)
        data= response.content
        soup= bs(data, 'html.parser')
        text= soup.get_text()            #FLAG
        with open(".chache.txt","w") as my:
            my.write(text)
    except:
        cprint("\n[-] Error: Data fetching error ", 'red',attrs=['bold','blink'])    
    print()
    display()
    print()
    order()

def display():
    l=k=[]
    d={}
    with open(".cache.txt","r") as my:
        f=my.readlines()
        for i in f:
            j=i.strip().split()
            if len(j) !=0:
                if j[0] != "View":
                    k.append(j)
    cprint("BOOK FOUNDS : ", 'blue')   #FLAG
    if choice==1:
        for i in range(len(l)):
            if l[i][0].lower()== "isbn:" and l[i][1].isdigit():
                print(joins(l[i-3]))
                print(joins(l[i-2]+l[i-1]))
                print(joins(l[i]))
                print("---------------------------")
    if choice==2:
        for i in range(len(l)):
            if l[i][0].lower() == "isbn" and l[i][1].isdigit():
                cprint(joins(l[i-2]),'red' , attrs=['bold','underline'])
                print(joins(l[i-1]))
                print(joins(l[i]))
                print(joins(l[i+1]))
                print("----------------------------")

def order():
    v=''
    print("DO YOU WANT TO ORDER BOOK [Y/N] ")
    ch= input("[choice]:> ")
    if ch.lower() == "y" :
        wb.open("https://www.amazon.com")
        wb.open("https://www.flipkart.com/")
    else:
        print("Bye :)")

def main():
    global choice    
    try:
        if choice==1:
            b_title= input("Enter Book Title : ")
            logging.debug(b_title)
            if connect():
                title_search(b_title)
            else:
                print("[-] PLEASE CONNECT TO INTERNET :(")
        elif choice == 2 :
            isbn= input("Enter ISBN13 [without hyphen(-)] : ")
            logging.debug(isbn)
            if len(isbn)== 13:
                if connect():
                    isbns(isbn)
                else:
                    print("[-] PLEASE CONNECT TO INTERNET :(")               
            else:              
                print("Invalid isbn ")
        elif choice== 3:
            if connect():
                print("""HERE ARE FEW RECOMENDATIONS: """)
                url='https://raw.githubusercontent.com/sg0admin/pro/main/booklist.txt'
                resp= req.get(url)
                data= resp.content
                print(data.decode('utf-8'))
            else:
                print("[-] PLEASE CONNECT TO INTERNET :( ")
        elif choice== 4:
            bk_manage()
        elif choice==5:
            with open(".history.log",'r') as myf:
                data= myf.readlines()
                for i in data:
                    print(i)
        elif choice==6:
            print("""
    Instructions to use this program:
    -this is software provide following function 
        - to search a book online by using book name and isbn number
        - to create a bookshelf and 
            - add books to it using book name , book\'s author name and isbn number
            - to delete , update book name
            - to delete bookshelf
    you will find these options by selection of your choice

    [+] NOTE: Internet connection is required for searching and recommendations of book
            and sql.connector, termcolor library required for mysql database connectivity
            and for text formating respectivily
            """)
        elif choice == 0:
            raise KeyboardInterrupt
    except KeyboardInterrupt :
        print("[-] Exiting ... ",end=' ')
        cprint(":)", 'red',attrs=['bold','blink'])

if __name__ == '__main__':
    main()
