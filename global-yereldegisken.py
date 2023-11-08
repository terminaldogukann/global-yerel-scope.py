#Python'da her bir değişkenin ve fonksiyonun, class'ların kendine ait kapsamı (scope) bulunur.
# Python herbir değişkeni isimm alanında(namespace)'de tanımlar.
# Değişkenin isim alanı ise, bu değişkenlerin nerelerde var olduğunu ve nerelerde kullanılabileceğini gösterir

#GLOBAL VE YEREL DEĞİŞKENLER.

def myfunction():
    a = 10
    print("YEREL DEĞİŞKEN SİLİNMEDEN TANIMLANIYOR... " ,a)

myfunction()
#print(a)
# print a ile çağırmak istersek hata verecektir, çünkü ;
# fonksiyon içerisindeki yerel değişkenler işlem bittikten sonra silinir
# Silinen bir veri tipini is not defined olur.
#YEREL DEĞİŞKEN.



#GLOBAL DEĞİŞKEN
#global'daki değişkenler de her yerden ulaşabiliriz.
b = 5 
def fonksiyon():
    print("GLOBAL DEĞİŞKEN, HER YERDEN ULAŞILABİLİR.",b)
fonksiyon()



#örnek
#hiyerarşik yapıyı bozma, is not defined hatası alabilirsin. çünkü function bitiyor.
"""
def fonksiyon():
    print(s)
fonksiyon()
s = "python"
"""


# burada global ve yerel değişkeni aynı anda kullanıyoruz.
# c = 2'ye tanımlanıyor. dhaa sonra yazdırılıyor, yazdırıldıktan sonra
# fonksiyon değeri bittiği için global değişken kullanılmaya başlıyor.
c = 10
def fonksiyon():
    c = 2 
    print("yerel değişken" ,c)
fonksiyon()
print("global değişken ", c)



# global deyimi.
# peki bir fonksiyonda globalde tanımlanmış bir değişkeni nasıl kullanacağız ?
# bunun için pythonda global ifadesi bulunmaktadır. 
# çok fazla kullanılan bir ifade değildir. her koşula göre özel veri tipleri olması daha mantıklıdır.
d = 5
def fonksiyon():
    global d
    d = 13
    print(d)
fonksiyon()
print("global değişken " , d)



if True:
    e = 4
    print(e)
print(e)