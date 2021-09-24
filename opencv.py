import cv2
import speedtest

img = cv2.imread("2.png")
# #cap.set(id,value) id = 3 for width adn 4 for hieght and 10 for brightness
# # cv2.imshow("output",img)
# cap = cv2.VideoCapture(0)
# cap.set(3,460)
# cap.set(4,560)
# cap.set(10,10)
# while True:
#     success, img = cap.read()
#     cv2.imshow("vedio",img)
#     if cv2.waitKey(1) and 0xFF ==ord('l'):
#         break
# imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(imggrey,(7,7),0)
# cv2.imshow("grey",imggrey)
# cv2.imshow("grey",blur)
# cv2.waitKey(0)
test = speedtest.__version__
print(test.)