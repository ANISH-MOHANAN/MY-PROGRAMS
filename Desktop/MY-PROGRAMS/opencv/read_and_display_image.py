# #to show image as color image
# import cv2
# img=cv2.imread('lena.jpg',1)
# cv2.imshow("image",img)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()

#to show image as balck and white image
import cv2
img=cv2.imread('lena.jpg',0)
cv2.imshow("image",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()