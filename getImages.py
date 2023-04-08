import time
import cv2

num=0

# Initialize the camera
cap = cv2.VideoCapture(0)

# Set the resolution of the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# Wait for the camera to warm up
time.sleep(2)

while 1:
   # Capture an image from the camera
   ret, img = cap.read()

   img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
   cv2.imshow('Img',img)

   k = cv2.waitKey(2)

   if k == ord('q'):
       break
   elif k == ord('s'): # wait for 's' key to save and exit
       cv2.imwrite('images/img' + str(num) + '.png', img)
       print("image saved!")
       num += 1

#close the window
cv2.destroyAllWindows()

