import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_image():
# read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = cap.read()
    return im
###################################### first uncomment this nd run
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

##################################### comment the above and thn run this for cropping coordinates

# cap = cv2.VideoCapture(1)

# while(True):
# 	# Capture frame-by-frame
# 	ret, frame = cap.read()
# 	camera_capture = get_image()
# 	file = 'E:\\chess_project\\chess pics\\testimage3.jpg'
# 	cv2.imwrite(file, camera_capture)
# 	img = cv2.imread('E:\\chess_project\\chess pics\\testimage3.jpg')
# 	# imageshow('org',img)
# 	# plt.imshow(img, interpolation = 'bicubic')
# 	# plt.show()
# 	break

# # cap.release()
# # cv2.destroyAllWindows()
# plt.imshow(img, interpolation = 'bicubic')
# plt.show()
