# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:04:41 2022

@author: Kumush
"""


a=int(input("juft son kiriting   "))
if a%2==0:
    print('rahmat!')
else:
    print('bu son juft emas')
    #-----
a=int(input("yoshingiz nechida   "))
if a<4 or a>60:
    print('sizga chipta bepul')
elif a<18:
    print('chipta narxi 10000 so\'m')
else:
    print("chipta narxi 20000 so'm")
#------
a=int(input("1- sonni kiriting   "))
b=int(input("2- sonni kiriting   "))
if a>b:
    print('1-son katta')
elif b>a:
    print('2-son katta')
else :
    print('sonlar teng')
  #-----mahsulot tanlaw

    mahsulotlar=['anor','olma','uzum','shaftoli','tarvuz','qovun','sabzi','pomidor','bodring','lavlagi']
    savat=[]
    savat.append((input("1-mahsulotni kiriting:   ")))
    savat.append(input("2-mahsulotni kiriting:   "))
    savat.append(input("3-mahsulotni kiriting:   "))
    savat.append(input("4-mahsulotni kiriting:   "))
    savat.append(input("5-mahsulotni kiriting:   "))
    bor_mahsulotlar=[]
    mavjud_emas=[]

    for mahsulot in savat:
            if mahsulot.lower() in mahsulotlar :
                bor_mahsulotlar.append(mahsulot)
                #print(f'dokonda {mahsulot} bor')
            else:
                mavjud_emas.append(mahsulot)
               # print(f'dokonda {mahsulot} yoq')
    print(f"dokonda quyidagi mahsulotlar yoq:\n")
    print(mavjud_emas) 
 #login tanlaw---------
    foydalanuvchilar=['kumush','nazira','lola','aziza','nodir']     
    a=(input('yangi login tanlang: '))
    if  a.lower() in foydalanuvchilar:
        print('login band boshqa login tanlang')
    else:
        print('xush kelibsiz foydalanuvchi')
# qoldiqsiz bolinishi------
a=int(input("butun son kiriting:  "))
if a%2==0:
    print(f"{a} soni 2 ga qoldiqsiz bo'linadi")
if (a%100)%4==0:
    print(f"{a} soni 4 ga qoldiqsiz bo'linadi")
if a%6==0:
    print(f"{a} soni 6 ga qoldiqsiz bo'linadi")
if a%8==0:
    print(f"{a} soni 8 ga qoldiqsiz bo'linadi")
if a%10==0:
    print(f"{a} soni 10 ga qoldiqsiz bo'linadi")
if a%3==0:
    print(f"{a} soni 3 ga qoldiqsiz bo'linadi")
if a%5==0:
    print(f"{a} soni 5 ga qoldiqsiz bo'linadi")
if a%7==0:
    print(f"{a} soni 7 ga qoldiqsiz bo'linadi")
if a%9==0:
    print(f"{a} soni 9 ga qoldiqsiz bo'linadi")
    