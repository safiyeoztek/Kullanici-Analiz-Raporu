print("----- KULLANICIANALİZRAPORU -----")

isim = input("İsim: ")
soyisim = input("Soyisim: ")
yas = int(input("Yaş: "))
teknolojiler = input("En sevdiğin 3 teknoloji: ")

isimSoyisim = (isim + " " + soyisim).upper()

print("isim Soyisim: " + str(isimSoyisim) + "\n" + "İsim Uzunluğu: " +str(len(isim + " " + soyisim)))

teknolojiList = teknolojiler.split()
print("Sevdiğin Teknolojiler:" +"\n"+ str(teknolojiList) + "\n" + "Toplam Teknoloji Sayısı: " +str(len(teknolojiList)))

print("Durum:" )

if yas > 18:
    print("Yazılım yolculuğuna hazırsın")
else:
    print("Erken başladın bu çok iyi")

if len(teknolojiList) == 3:
    print("Keşfetmeye açıksın")
else:
    print("Listeyi genişletebilirsin")




