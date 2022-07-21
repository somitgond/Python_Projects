# this is a word series game 
# in this game new word must start with ending letter of last entered value
# It uses file handling with python3

import time
import os

print("This is WordSeries v1.1 by TSunami")
print("DISCLAMER : This is an open source project so any one can distribute and modify it")
print("Feel Free to create your own version\n")
print("[-] Your device seems slower :(( \n[+]But please have patience")  # fun line
print("Loading ... ")

time.sleep(3)

print("\n\n")
print("WELcome")
print("0. To view previous score  ")
print("1. To start new game ")
print("2. To continue ...")

i="n"
d_list= ["n"]


def p_score():
    with open(".data.txt","r") as myf:            # data.txt  is file created during execution to save words
        data= myf.readlines()
    print("Highest previous score is ",len(data))
    return run()

def n_game():
    global i
    print("Lets start ... ")
    print("let start with  'n' ")
    print("if you want to quit anytime type : 0")
    with open(".data.txt","w") as nf:
        while i != "0" :
            i=input(">> ")
            if i=="0":
                break
            elif i.lower() in d_list :        # d_list  :  Entered values are appended in a list
                print("\n[-] Duplicate input Please try again\n start with \'{}\' of {}\n".format(d_list[-1][-1],d_list[-1]))
            elif i[0] != d_list[-1][-1]:
                print("\n UnmatchCharacterError : \n Please start with \'{}\' of {} \n".format(d_list[-1][-1],d_list[-1]))
            else:
                d_list.append(i)
            nf.write(i+"\n")
        if i== "0":
            print("Thanks for playing ")
            print("Your play time : ")

def p_game():
    global i
    print("Lets start ... ")
    with open("data.txt","r") as rf:
        val= rf.readlines()
        print("Last entered value is {} So lets start with ".format(val[-1]),val[-1][-1])
    print("if you want to quit anytime type : 0")
    with open(".data.txt","w") as nf:
        while i != "0" :
            i=input(">> ")
            if i=="0":
                break
            elif i.lower() in d_list :
                print("\n[-] Duplicate input Please try again\n start with \'{}\' of {} \n".format(d_list[-1][-1], d_list[-1]))
            elif i[0] != d_list[-1][-1]:
                print("\n UnmatchCharacterError : \n Please start with \'{}\' of {}\n".format(d_list[-1][-1], d_list[-1]))
            else:
                d_list.append(i)
            nf.write(i+"\n")
        if i== "0":
            print("Thanks for playing ")
            print("Your play time : ")
def run():
    try:
        u_in= input("> ")
        if u_in== "0" :
            p_score()
        if u_in== "1":
            n_game()
        if u_in=="2":
            p_game()
    except:
        print("\n[-] Exiting ..... An Error Ocurred")
    
run()
