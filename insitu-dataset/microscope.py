import cv2 as cv
from PIL import Image

micro = cv.VideoCapture(0)
if not micro.isOpened():
    print('Cannot access microscope')
    exit()
    
i = 0
while i < 2:

    ret, frame = micro.read()
    if not ret:
        print('Error')
        break

    cv.imshow('Microscope', frame)

    if cv.waitKey(1) == ord('r'):
        print('Are you sure to retrive this frame?, Y/N')
        i = 1
        if cv.waitKey(1) == ord('y'):
            print('Image Saved')
            #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame = cv.resize(frame, (1024, 1024))
            cv.imwrite('image7b.JPG',frame)
            i = 2
        if cv.waitKey(1) == ord('n'):
            i = 0

    if cv.waitKey(1) == ord('s'):
        print('Image Saved')
        #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.resize(frame, (1024, 1024))
        cv.imwrite('background4.JPG',frame)
        i = 2

    if cv.waitKey(1) & 0xFF == ord('q'):
        print('Quit')
        i = 2
        break

