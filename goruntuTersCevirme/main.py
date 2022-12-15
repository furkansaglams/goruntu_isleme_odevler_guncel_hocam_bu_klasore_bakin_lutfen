import cv2
import numpy as np

kelebek = cv2.imread("kelebek.jpg", 0)
cv2.imshow("kelebek", kelebek)

yukseklik,genislik=kelebek.shape

for i in range(yukseklik):
    for j in range(genislik):
        kelebek[i][j]= np.max(kelebek) - kelebek[i][j]


cv2.imshow("Kelebek yeni", kelebek)
cv2.waitKey()