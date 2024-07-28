import random
Elemanlar = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Num = int(input("Şifre kaç karakterli olsun ?"))
Parola = ""
print("Oluşturulan şifre ;")
for i in range(Num):
    Parola += random.choice(Elemanlar)
print(Parola) 
