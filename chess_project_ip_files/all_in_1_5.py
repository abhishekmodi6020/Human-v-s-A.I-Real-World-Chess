import cv2
import ctypes
import numpy as np
import matplotlib.pyplot as plt
import msvcrt as m
from lookup import *
from pprint import pprint
# vice = ctypes.cdll.LoadLibrary('E:\\chess_project\\Vice11\\Vice11\\Source\\vice.dll')

#################################### initilization ################################
np.set_printoptions(threshold = 'nan')
# img = []
# image = [[]]
# image = np.array(image)
# gray = []
# edges = []
# corners = []
# centroid = []
temp_4 = 0
temp_d_2 = 0
str_2 = ''
str_3 = ''
global image
global gray
global imag1
global imag2
global imag3
global imag4
global centroid
global change

################################## Functions #######################################
##def after_vice_kills(move_made):
##	global d_2
##	if (string[2] == 'a'):
##		conv = 1
##	if (string[2] == 'b'):
##		conv = 2
##	if (string[2] == 'c'):
##		conv = 3
##	if (string[2] == 'd'):
##		conv = 4
##	if (string[2] == 'e'):
##		conv = 5
##	if (string[2] == 'f'):
##		conv = 6
##	if (string[2] == 'g'):
##		conv = 7
##	if (string[2] == 'h'):
##		conv = 8
##
##	tup = (9 - int(string[3]), conv)
##	for k,v in d_2.iteritems():				## k- key, v- value
##		# print d_2[k]
##		if(tup == d_2[k]):
##			print "error"
##			temp = k
##	try:
##		del d_2[temp]
##	except:
##		print""
def imageshow(displayname, image):
    """ (enter string),( img/gray/cannyedges/) """ 
    cv2.namedWindow(displayname, cv2.WINDOW_NORMAL)
    cv2.imshow(displayname, image)
    print "image type=",type(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
def imageread(location):
    """ enter the image storin name nd location as a string"""
    # location = 'E:\\chess_project\\chess pics\\detect pieces\\z2.jpg'
##    location = 'E:\\chess_project\\chess pics\\others\\a7.jpg'
    global image
    image = cv2.imread(location)
    print 'image =',type(image)
    # imageshow('original',image)

def color_to_gray():
    """ enter the source image"""
##    global median
##    median = cv2.medianBlur(img,5)
##    imageshow('median',median)
##    global gaussian
##    gaussian = cv2.GaussianBlur(img,(5,5),0)
##    imageshow('gaussian',gaussian)
    global image
    # image = source_image
    
    global gray
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
##    print 'gray =',gray
##    imageshow('gray',gray)

def canny():
    """ canny edge detector """
    global edges
    edges = cv2.Canny(gray,150,250,apertureSize = 3,)
    imageshow('canny',edges)
    
##    global thresh
##    ret,thresh = cv2.threshold(gray,100,255,0)
##    imageshow('thres', thresh)
##    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
##    global borders
##    borders = cv2.drawContours(img, contours, -1,(200,0,0),3)
##    
##    imageshow('canny', borders) 
##    print 'cannyedges = ',cannyedges

def corner_detection():
    """detects and shows corners of an image by shi_tomasi_method"""
    global corners
    """ corners[rows,0,0 for x or 1 for y] """
##    corners = cv2.goodFeaturesToTrack(gray,81,0.01,10)
    corners = cv2.goodFeaturesToTrack(gray,81,0.0005,30)
##  arguments -- image,no.of corners, quality of image between 0 to 1 , euclidian distance      
    print 'corners_type =',type(corners)
    print 'corners_shape =',corners.shape
    print 'corners =',corners 
    count = 0
    for i in corners:
        x,y = i.ravel()
        cv2.circle(image,(x,y),4,(0,0,255),-1)
        """ cv2.circle(destination, position, radius,color,i guess thickness)"""
        count += 1
    print 'count =',count
    imageshow('corners', image)
    

def find_centroid():
    """ arranges the corner matrix and finds centroid """
    z = len(corners)
    ######### Ascending x axis
    for i in range(1,z-1):
        for j in range(z-1):
            y = corners[j,0,1]
    ##        a = corners[j,0]
            x = corners[j+1,0,1]
    ##        b = corners[j+1,0]           
            if corners[j,0,0] > corners[j+1,0,0]:
                temp = corners[j,0,0]
                temp1 = corners[j,0,1]
    ##            print 'temp =',temp
                corners[j,0,1] = corners[j+1,0,1]
                corners[j,0,0] = corners[j+1,0,0]
    ##            print 'y =',y
                corners[j+1,0,0] = temp
                corners[j+1,0,1] = temp1
    ##            print 'x =',x
    ########### ascending y region and appoximating small errors        
    for i in range(1,z-1):
        for j in range(z-1):
            y = corners[j,0,1]          #### corners[rows,0,0 for x or 1 for y]
    ##        a = corners[j,0]
            x = corners[j+1,0,1]
    ##        b = corners[j+1,0]
            if corners [j,0,1] > corners[j+1,0,1]:
                if corners [j,0,1] - corners[j+1,0,1] < 22.0:
                    corners [j+1,0,1] = corners[j,0,1]
            else: 
                if corners [j+1,0,1] - corners[j,0,1] < 22.0:
                    corners [j,0,1] = corners[j+1,0,1]
            if corners[j,0,1] > corners[j+1,0,1]:
                temp = corners[j,0,0]
                temp1 = corners[j,0,1]
    ##            print 'temp =',temp
                corners[j,0,1] = corners[j+1,0,1]
                corners[j,0,0] = corners[j+1,0,0]
    ##            print 'y =',y
                corners[j+1,0,0] = temp
                corners[j+1,0,1] = temp1
    print 'new corners = ',corners
    for i in corners:
        x,y = i.ravel()
        cv2.circle(image,(x,y),4,(0,255,0),-1)
        """ cv2.circle(destination, position, radius,color,i guess thickness)"""
    imageshow('corners', image)
    count = 1

    x1 = [0]*71
    x2 = [0]*71
    y1 = [0]*71
    y2 = [0]*71
    for i in range(z-1):
        if i + 10 <= z-1:
            x1[i] = corners[i,0,0]
            x2[i] = corners[i+1,0,0]
##            print 'count =',count
            count = count + 1
    print 'z =',z
    for j in range(z-1):
        if j + 10 <= z-1:
            y1[j] = corners[j,0,1]
            y2[j] = corners[j+9,0,1]
    print 'x1 =',x1
    print 'x2 =',x2
    print 'y1 =',y1
    print 'y2 =',y2
    x = [0]*71
    y = [0]*71
    count = 0
    print len(x1)

    #################### finding centroid using midpoint
    for i in range(len(x1)):
        if x2[i] > x1[i]:
            a =(x1[i] + x2[i])/2
            b =(y1[i] + y2[i])/2
            x[i] = int(a)
            y[i] = int(b)
##            cv2.circle(img,(int(x[i]),int(y[i])),4,(255,0,255),-1)
##        count = count + 1
    print 'length x =', len(x)       
    print 'length y =', len(y)
    print 'x =',x
    print 'y =',y
    while(1):       ######## TO REMOVE 0 FROM EVERY 9TH ELEMENT OF X
        try: x.remove(0)
        except: break
    while(1):       ######## TO REMOVE 0 FROM EVERY 9TH ELEMENT OF Y
        try: y.remove(0)
        except: break
    print 'length x =', len(x)       
    print 'length y =', len(y)
    print 'x =',x
    print 'y =',y
    for i in range(64):
        cv2.circle(image,(int(x[i]),int(y[i])),3,(255,0,255),-1)
##        imageshow('centroid', image)
       
    print 'length x =', len(x)       
    print 'length y =', len(y)
    print 'x =',x
    print 'y =',y
    global centroid
    centroid = zip(x,y)
    # imageshow('centroid', image) 
    cv2.namedWindow('centroid', cv2.WINDOW_NORMAL)
    cv2.imshow('centroid', image)
    print 'set the pieces nd press q'
    while(1):
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        break
    print 'centroid =',centroid
    
def wat_is_moved(change):
    global d_2
    global d_1
    global temp_d_2
    for i,v in d_2.iteritems():
        # print 'v =',v
        if(d_1[change] == d_2[i]):
            temp_d_2 = i
            print ''
            print 'the piece moved is',i, 'from',d_2[i]

    z = d_2[temp_d_2]
    print 'z = ',z
    if z[1] == 1:
        str_1 = 'a'
    if z[1] == 2:
        str_1 = 'b'
    if z[1] == 3:
        str_1 = 'c'
    if z[1] == 4:
        str_1 = 'd'
    if z[1] == 5:
        str_1 = 'e'
    if z[1] == 6:
        str_1 = 'f'
    if z[1] == 7:
        str_1 = 'g'
    if z[1] == 8:
        str_1 = 'h'
    global str_2
    str_2 = str_1 + str(9 - z[0])
    print ''
    print "str_2 = ",str_2 

def whr_is_it_moved(change):
    global d_2
    global d_1
    global temp_d_2
    for i,v in d_2.iteritems():
        # print 'v =',v
        # print 'now piece is at =',d_1[change]
        ae = d_1[change]
        d_2[temp_d_2] = ae
    print ''
    print 'the piece moved is',temp_d_2,'at', d_2[temp_d_2]

    z = d_2[temp_d_2]
    print 'z = ',z
    if z[1] == 1:
        str_1 = 'a'
    if z[1] == 2:
        str_1 = 'b'
    if z[1] == 3:
        str_1 = 'c'
    if z[1] == 4:
        str_1 = 'd'
    if z[1] == 5:
        str_1 = 'e'
    if z[1] == 6:
        str_1 = 'f'
    if z[1] == 7:
        str_1 = 'g'
    if z[1] == 8:
        str_1 = 'h'
    global str_3
    str_3 = str_1 + str(9 - z[0])
    print ''
##    print "str_3 = ",str_3 

def get_image():
# read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = cap.read()
    return im



##########################################################################################################################################
##########################################################################################################################################

###################### CENTROID PART #########################

imageread('E:\\chess_project\\chess pics\\testimage3.jpg')
# imageshow('org', image)
image = image[24:458,120:576]             ##change at remaining two places also
imageshow('cropped', image)
color_to_gray()
# imageshow('gray', gray)
corner_detection()
find_centroid()
# plt.imshow(image, interpolation = 'bicubic')
# plt.show()

#### make the program wait before doing anything else 
######################## database trying#############################
centroid_1 = centroid
d_1 = {}
for i in range(8):
    for j in range(8):
        d_1[centroid_1[i*8 + j]] = (i+1,j+1) 
# print 'centroid[3] =',d_1[(210,42)]
##pprint (d_1)
# print len(d_1)

##d_2 = {'rb1':(0,0), 'hb1':(0,1), 'bb1':(0,2), 'qb':(0,3), 'kb':(0,4), 'bb2':(0,5), 'hb2':(0,6), 'rb2':(0,7), 'pb1':(1,0), 'pb2':(1,1), 'pb3':(1,2), 'pb4':(1,3), 'pb5':(1,4), 'pb6':(1,5), 'pb7':(1,6), 'pb8':(1,7)}


###################### SUBTRACTION PART #####################

################### IMAGE 1

while(True):

    print ''
    raw_input("press enter after computer makes move.....")
    global cap
    cap = cv2.VideoCapture(1)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        camera_capture = get_image()
        camera_capture = camera_capture[24:458,120:576]
        file = 'E:\\chess_project\\chess pics\\testimage.jpg'
        cv2.imwrite(file, camera_capture)
        imag1 = cv2.imread('E:\\chess_project\\chess pics\\testimage.jpg')
##        print 'while loop 1 working'
        # if cv2.waitKey(0) & 0xFF == ord('q'):
        #   cv2.destroyAllWindows()
        break   
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    # imageshow('imag_1', imag1)
##    kill_check = raw_input("enter the move that vice made")
##    after_vice_kills(kill_check)

    print ''
    raw_input("Make your Move and Press Enter To Continue.....")

    #################### IMAGE 2

    cap = cv2.VideoCapture(1)
    while(True):
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        camera_capture = get_image()
        camera_capture = camera_capture[24:458,120:576]
        file = 'E:\\chess_project\\chess pics\\testimage_1.jpg'
        cv2.imwrite(file, camera_capture)
        imag2= cv2.imread('E:\\chess_project\\chess pics\\testimage_1.jpg')
        print 'while loop 2 working'
        # if cv2.waitKey(0) & 0xFF == ord('q'):
        #   cv2.destroyAllWindows()
        break   
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
##    imageshow('imag_2', imag2)


    ############### SUBTRACT

    imag3 = cv2.subtract(imag2, imag1)
    imag3 = cv2.cvtColor(imag3,cv2.COLOR_BGR2GRAY)
##    imageshow('2-1', imag3)
    # plt)


    imag4 = cv2.subtract(imag1, imag2)
##    imageshow('1-2', imag4)
    # plt.imshow(imag4, interpolation = 'bicubic')
    # plt.show()
    imag4 = cv2.cvtColor(imag4,cv2.COLOR_BGR2GRAY)

    ################################################### trying something new
    ### think for enpass and castling
    for i in range(len(centroid)):
        for j in range(30,255):
            temp_rows = centroid[i][1]
            temp_cols = centroid[i][0]
        
            if(imag3[temp_rows, temp_cols] == j):
                print "inside the if loop for wat is moved"
                #global temp_4
                temp_4 = i

    change = centroid[temp_4]
    wat_is_moved(change)
                

    for i in range(len(centroid)):
        for j in range(30,255):
            temp_rows = centroid[i][1]
            temp_cols = centroid[i][0]
            if(imag4[temp_rows, temp_cols] == j):
                print "inside the if loop for whr it is moved"
                #global temp_4
                temp_4 = i
    change = centroid[temp_4]
    whr_is_it_moved(change)
    str_main = str_2 + str_3
    print '     human made move ->',str_main
    
    ##print 'd_2 =',d_2

    
