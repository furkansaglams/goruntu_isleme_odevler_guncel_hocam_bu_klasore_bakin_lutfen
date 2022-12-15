import cv2
import numpy as np

kartalResmi = cv2.imread("kartal.jpg", 0)
cv2.imshow("Kartal", kartalResmi)

histogramDizisi = np.zeros(256) #Histogram hesabı için 0 'lardan oluşan boş bir dizi oluşturdum.
yukseklik,genislik=kartalResmi.shape #Görüntünün boyutları alındı çünkü for döngüsünde sınırları belirlememiz gerekiyordu.

for i in range(yukseklik):
    for j in range(genislik):
        pikselDegeri=kartalResmi[i][j] #Görüntünün  piksel değerleri sıra ile alındı.
        histogramDizisi[pikselDegeri]= histogramDizisi[pikselDegeri] + 1 #okunan değerin index ine gidilip 1 artırıldı.


np.set_printoptions(suppress=True) #histogram dizisini yazdırırken üst biçiminde yazıyordu onu engellemek için yapıldı.Örn:2.97351e+05  nin yerine 297351 yazımı gibi daha saegözükmesi için

print(histogramDizisi)
print("\nHistogram dizisinin en çok tekrar eden değeri: ",np.max(histogramDizisi))


cv2.waitKey()




