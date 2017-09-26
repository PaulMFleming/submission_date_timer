import time

n = int(input("Countdown from: "))


while n>0:
    time.sleep(1)
    print n
    n-=1

if n==0:
    print "Fin"
    
