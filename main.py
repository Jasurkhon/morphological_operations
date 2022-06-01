#importing opencv and numpy libraries
import numpy as np
import cv2 as cv

#function to apply scalling operation 
def scal():  
    #Reading original and binary Image 
    img_col = cv.imread('1.jpg')
    img_bin = cv.imread('binary.png')
    #Resizing using Cubic interpolation
    res_col = cv.resize(img_col,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
    res_bin = cv.resize(img_bin,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
    #showing original image with title "Original color" and "Original binary" on a window
    cv.imshow('Original color',img_col)
    cv.imshow('Original binary',img_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    #showing scalling image with title "Scalling color image with Cubic interpolation" and "Scalling binary image with Cubic interpolation" on a window
    cv.imshow('Scalling color image with Cubic interpolation',res_col)
    cv.imshow('Scalling binary image with Cubic interpolation',res_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    # Window shown waits for any key pressing event to destroy the previously created windows
    cv.destroyAllWindows()

#function to apply rotaion operation
def rotation():
    #reading original image and binary image
    img_col = cv.imread('1.jpg')
    img_bin = cv.imread('binary.png')
    # dividing height and width of the image by 2 to get the center of the image
    height, width = img_col.shape[:2]
    height, width = img_bin.shape[:2]
    #translation matrix by 90 degree with respect to center without scaling to get rotation matrix
    matrix = cv.getRotationMatrix2D((width/2,height/2), 90, 1)
    #applying the matrix to the image to rotate it
    translated_col = cv.warpAffine(img_col, matrix, (width, height))
    translated_bin = cv.warpAffine(img_bin, matrix, (width, height))
    #showing original image with title "Original col" and "Original bin" on a window
    cv.imshow('Original col', img_col)
    cv.imshow('Original bin', img_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    #showing the image on a new window with title "Rotated Image col" and "Rotated Image bin"
    cv.imshow('Rotated Image col', translated_col)
    cv.imshow('Rotated Image binary', translated_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    #window shown waits for any key pressing event to destroy the previously created windows
    cv.destroyAllWindows()

#function to apply translation operation
def translation():
    #reading original and binary image 
    img_col = cv.imread('1.jpg')
    img_bin = cv.imread('binary.png')
    # getting the width and height of the image
    height,width = img_col.shape[:2]
    height,width = img_bin.shape[:2]
    #translation matrix
    matrix = np.float32([[1,0,100],[0,1,50]])
    #applying the matrix to the image 
    trans_col = cv.warpAffine(img_col,matrix,(height,width))
    trans_bin = cv.warpAffine(img_bin,matrix,(height,width))
    #showing original image with title "Original color" and "Original bin" on a window
    cv.imshow('Original color', img_col)
    cv.imshow('Original bin', img_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    #Showing the image on a new window with title "Translational color Image" and "Translational binary Image"
    cv.imshow('Translational color Image',trans_col)
    cv.imshow('Translational binary Image',trans_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    # Window shown waits for any key pressing event to destroy the previously created windows
    cv.destroyAllWindows()

#function to apply erosion operation
def erosion_operation():
    # Reading the input image
    img_col = cv.imread('1.jpg')
    img_bin = cv.imread('binary.png')
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5,5), np.uint8)
    # 1st parameter is the original image,2nd is the matrix with which image is convolved and 3rd parameter is the number of iterations to erode the image
    img_erosion_col = cv.erode(img_col, kernel, iterations=1)
    img_erosion_bin = cv.erode(img_bin, kernel, iterations=1)
    #showing original image with title "Original color" and "Original binary" on a window
    cv.imshow('Original color', img_col)
    cv.imshow('Original binary', img_bin)
    # waits for a key event occuring
    cv.waitKey(0)
     #Showing the image on a new window with title "Erosion color" and "Erosion binary"
    cv.imshow('Erosion color', img_erosion_col)
    cv.imshow('Erosion binary', img_erosion_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    # Window shown waits for any key pressing event to destroy the previously created windows
    cv.destroyAllWindows()

#function to apply dilation operation
def dilation_operation():
    # Reading the input image
    img_col = cv.imread('1.jpg')
    img_bin = cv.imread('binary.png')
    #taking a matrix of size 5 as the kernel
    kernel = np.ones((5,5), np.uint8)
    # 1st parameter is the original image,2nd is the matrix with which image is convolved and 3rd parameter is the number of iterations to dilate the image
    img_dilation_col = cv.dilate(img_col, kernel, iterations=1)
    img_dilation_bin = cv.dilate(img_bin, kernel, iterations=1)
    #showing original image with title "Original col" and "Original bin" on a window
    cv.imshow('Original col', img_col)
    cv.imshow('Original bin', img_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    #Showing the image on a new window with title "Dilation col" and "Dilation bin"
    cv.imshow('Dilation col', img_dilation_col)
    cv.imshow('Dilation bin', img_dilation_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    # Window shown waits for any key pressing event to destroy the previously created windows
    cv.destroyAllWindows()

#function to apply opening operation
def opening_operation():
    # Reading the input image
    img_col = cv.imread('1.jpg')
    img_bin = cv.imread('binary.png')
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5,5), np.uint8)
    #applying opening operation
    opening_col = cv.morphologyEx(img_col, cv.MORPH_OPEN, kernel)
    opening_bin = cv.morphologyEx(img_bin, cv.MORPH_OPEN, kernel)
    #showing original image with title "Original col" and "Original bin" on a window
    cv.imshow('Original col', img_col)
    cv.imshow('Original bin', img_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    #Showing the image on a new window with title "Opening col" and "Opening bin"
    cv.imshow('Opening col', opening_col)
    cv.imshow('Opening bin', opening_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    # Window shown waits for any key pressing event to destroy the previously created windows
    cv.destroyAllWindows()

#function to apply closing operation
def closing_operation():
    # Reading the input image
    img_col = cv.imread('1.jpg')
    img_bin = cv.imread('binary.png')
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5,5), np.uint8)
    #applying closing operation
    closing_col = cv.morphologyEx(img_col, cv.MORPH_CLOSE, kernel)
    closing_bin = cv.morphologyEx(img_bin, cv.MORPH_CLOSE, kernel)
    #showing original image with title "Original col" and "Original bin" on a window
    cv.imshow('Original col', img_col)
    cv.imshow('Original bin', img_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    #Showing the image on a new window with title "Closing col" and "Closing bin"
    cv.imshow('Closing col', closing_col)
    cv.imshow('Closing bin', closing_bin)
    # waits for a key event occuring
    cv.waitKey(0)
    # Window shown waits for any key pressing event to destroy the previously created windows
    cv.destroyAllWindows()

#menu bar for the user to choose which operation to apply on image
print("1.Scalling\n2.Rotation\n3.Translational\n4.Erosion\n5.Dilation\n6.Opening\n7.Closing\n8.Quit")
#while loop works infinitely by asking user to make choice from given options until user selects "8" option (loop automatically stops)
while True:
    select = input("Choose one from options: ")
    if select == "1":
        scal()
    elif select == "2":
        rotation()
    elif select == "3":
        translation()
    elif select == "4":
        erosion_operation()
    elif select == "5":
        dilation_operation()
    elif select == "6":
        opening_operation()
    elif select == "7":
        closing_operation()
    elif select == "8":
        break





