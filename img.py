import cv2
img=cv2.imread("ice cream.jpg")
print(img)
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imwrite('rgb.jpg',rgb)
cv2.imwrite('gre.jpg',gry)
