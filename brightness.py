import numpy as np
import cv2

cap = cv2.VideoCapture(0) #inisialisasi pada webcam.
print(cap.isOpened())


while(True): #looping imshow
    ret, frame = cap.read() #menangkap gambar dengan format berwarna /BGR
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 0) #meningkatkan nilai kecerahan gambar
    cv2.imshow('webcam',bright) #menampilkan gambar yang telah diubah tingkat kecerahannya.
    if cv2.waitKey(1) & 0xFF == ord('q'): #menghentikan program dengan menekan tombol q pada keyboard
        break


cap.realease()
cv2.destroyAllwindows()