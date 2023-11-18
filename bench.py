#* .lib *#
import time
import os

#* .func *#
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#* .data *#
print("Produced by Bordless-ita\ngithub.com/Bordless-ita\nDistributed under Mozilla Public License 2.0\n\n\n")
print("__________________________________________________\n|1. Mini test (For checking if the cpu works only)|\n__________________________________________________\n|2. Standard test (Print only elapsed time)       |\n__________________________________________________\n|3. Advanced test                                 |\n__________________________________________________\n|4. Brute test                                    |\n__________________________________________________")
inpt=input("Select a number: ")
clc=0

#* .code *#
if inpt=="1":
    l=range(100,1001) # Inizializzazione range di valori da inserire nel ciclo
    #chs="Mini test [Elaboration of number from 100 to 1000](For checking if the cpu works)"
    start = time.time()
elif inpt=="2":
    l=range(100,10001)
    #chs="Standard test [Elaboration of number from 100 to 10000] (Don't return ratio)"
    start = time.time()
elif inpt=="3":
    l=range(100,100001)
    start = time.time()
    #chs="Advanced test [Elaboration of number from 100 to 100000] (Return ratio scale)"
elif inpt=="4":
    l=range(100,1000001)
    start = time.time()
    #chs="Brute test [Elaboration of number from 100 to 1000000] (Return ratio scale)"
else:
    print ("Exiting...")
    exit
#print("Chosen test:",chs)
print("Elapsing...")
for i in l: # Ciclo di stampa
    print(i) # Stampa numero
    clc=clc+1
end = time.time()
cls()
elps=end-start
elaps=str(elps)
print("Calculations performed:",clc)
if inpt=="3":
    print("Elapsed time:",elaps[:5],"Seconds")
    if elps<10.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "10" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<30.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "9" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<60.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "8" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<75.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "7" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<100.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "6" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<300.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "5" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<600.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "4" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<900.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "3" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<1800.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "2" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<3600.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "1" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps>3601.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "0" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    else:
        print("Error!")
if inpt=="4":
    print("Elapsed time:",elaps[:6],"Seconds")
    if elps<60.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "10" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<120.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "9" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<300.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "8" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<600.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "7" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<900.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "6" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<300.00:
        print('The processor is up-to-date and ops(Operations per Seconds) ratio returned a score of "5" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<1800.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "4" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<2700.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "3" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<3600.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "2" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps<4500.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "1" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    elif elps>4501.00:
        print('The processor is outdated and ops(Operations per Seconds) ratio returned a score of "0" on a 0-10 scale')
        time.sleep(120)
        print("Exiting...")
        exit
    else:
        print("Error!")
        exit