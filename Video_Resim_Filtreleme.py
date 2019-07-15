import cv2

import numpy as np

kamera = cv2.VideoCapture(0)

while (True):
    ret, frame=kamera.read()     # kameramızı açtırıyoruz, okuyoruz

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    # videmuzu color_BGR2HSV ile filtreleme işlemine tabi tutuyoruz.

    sari = np.array([5,100,100])
    sari1 = np.array([40,255,255])     # sari tonda iki renk belirledik. bu iki değer arası sari tonlardan oluşacak. mavi tondaki cisimleri okuyacak

    mask = cv2.inRange(hsv, sari,sari1) # bu renk tonlarını mask değişkenine atadık.

    son = cv2.bitwise_and(frame,frame, mask=mask)   # şimdi bitwise ile maskelenen videomuzu son değişkenine atadık

    cv2.imshow('Orjinal', frame)      # kullanıcıya çalışmamızı gösteriyoruz. 'orjinal ' hali
    cv2.imshow('mask', mask)          #  maskelenmiş hali
    cv2.imshow('son hali', son)        # ve son hali

    if cv2.waitKey(25) & 0xFF==ord('q'):    # kameramız 'q' ya basılmadığı müddetçe açık kalıcak,
        break                               # sonlandır

kamera.release()
cv2.destroyAllWindows()

# evet arkadaşlar bu dersimizinde sonuna geldik, iyi çalışmalar dilerim...