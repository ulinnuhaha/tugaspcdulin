import numpy as np
import cv2

cap = cv2.VideoCapture(0) #inisialisasi webcam 
print(cap.isOpened())

while(True): #untuk looping syntax imshow
    ret, frame = cap.read() #untuk mengambil gambar dengan format BGR
    abu=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #konversi objek video dari yang sebelumnya berwarna menjadi grayscale 
    cv2.imshow('webcam', 255-abu) #mengubah gambar dari skala keabuan menjadi gambar negatif. 
    if cv2.waitKey(1) & 0xFF == ord('q'): #menghentikan program dengan menekan tombol q pada keyboard
        break


cap.realease()
cv2.destroyAllwindows()