from colorama import Fore , init
from time import sleep
from sys import exit
from os import system
init()
try:
    while True:
        def __start__():
            try:
                system("cls" or "clear")
                print(Fore.LIGHTCYAN_EX+"\n*******************************************"+Fore.LIGHTYELLOW_EX+"")
                sleep(2)
                first=int(input("[!] Enter The First Number : "))
                print(Fore.LIGHTCYAN_EX+"*******************************************"+Fore.LIGHTYELLOW_EX+"")
                sleep(1)
                second=int(input("[!] Enter The Second Number : "))
                print(Fore.LIGHTCYAN_EX+"*******************************************"+Fore.LIGHTYELLOW_EX+"")
                sleep(1)
                third=int(input("[!] Enter The Third Number : "))
                if first == second == third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"First=Second=Third=",first) 
                if first>second>third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTWHITE_EX,"Middle Number= ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , third)
                elif first>third>second:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTWHITE_EX,"Middle Number= ",third)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , second)
                elif second>first>third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTWHITE_EX,"Middle Number= ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , third)
                elif second>third>first:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTWHITE_EX,"Middle Number= ",third)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " ,first)
                elif third>second>first:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",third)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTWHITE_EX,"Middle Number= ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " ,first)
                elif third>first>second:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",third)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTWHITE_EX,"Middle Number= ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " ,second)
                elif second==first>third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest= ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , third)
                elif second==first<third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",third)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest= ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , second)
                elif second>first==third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest= ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , third)
                elif second<first==third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",third)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , second)
                elif first>second==third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",first)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest= ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , third)
                elif first<second==third:
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",second)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTGREEN_EX,"The Biggest = ",third)
                    print(Fore.LIGHTCYAN_EX+"*******************************************")
                    sleep(1)
                    print(Fore.LIGHTRED_EX,"The Smallest = " , first)

            except Exception:
                exit()
            except KeyboardInterrupt:
                print("\nBye")
                sleep(2)
                exit()
        __start__()
        print(Fore.LIGHTCYAN_EX+"*******************************************"+Fore.LIGHTYELLOW_EX+"")
        sleep(1)
        print("[4] Restart\n[1] Exit")
        sleep(3)
        decision=input("[!] Enter Your Number:")
        if decision==4:
            system("cls " or "clear")
            sleep(1)
            __start__()
        elif decision==1:
            sleep(1)
            exit()
        elif decision=="":
            sleep(1)
            __start__()
        # else:
        #     sleep(1)
        #     system("cls" or "clear")
        #     exit()
except KeyboardInterrupt:
        print("\nBye")
        sleep(2)
        exit() 
except Exception:
        print("Bye!")
        sleep(5)
        exit() 
