import cv2,time

video = cv2.VideoCapture(0)

while  True:
    check, frame = video.read()

    gray  =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow('Capturing', gray)

    key = cv2.waitKey(1000)

    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows