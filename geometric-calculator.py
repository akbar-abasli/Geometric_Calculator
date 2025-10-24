import math
import time
a = (input("""
Seçin[1,2]
1--> Çevrənin Uzunluğu
2--> Dairənin Sahəsi              
"""))

#Dairə
def daire(): 
    r = float(input("Radiusu yaz: "))
    s = math.pi * pow(r,2)
    print("Hesablanır Gözləyin.. ")
    time.sleep(2) 
    print(f"Dairənin Sahəsi: {s}")
    print(f"Yuvarlaqlaşdırılmış Sahəsi: {round(s)}")
    
#Çevrə
def cevre():
    r1 = float(input("Radiusu yaz: "))
    u = math.pi * r1 * 2
    print("Hesablanır Gözləyin.. ")
    time.sleep(2) 
    print(f"Çevrənin Uzunluğu: {u}")
    print(f"Yuvarlaqlaşdırılmış Uzunluğu: {round(u)}")

if a == "1":
    cevre()

elif a == "2":
    daire()

else:
    print("Error!..")
