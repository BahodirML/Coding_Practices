import cv2
import os


#importing hand detector
from cvzone.HandTrackingModule import HandDetector


#camera setup
width, height = 1280, 720
    
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)


#get list of ppt images

folderPath = 'Presentation'
pathImages= sorted(os.listdir(folderPath), key = len)
#qprint(pathImages)


#variables
imageNumber = 0
hs, ws = int(120*1.2), int(213*1.2)
gestureThreshold = 300
buttonPressed = False
buttonCounter =0 
buttonDelay = 30
#hand detector
detector = HandDetector (detectionCon=0.8, maxHands=1)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[3])
    imgCurrent = cv2.imread(pathFullImage)



    hands, img = detector.findHands(img)
    cv2.line(img,(0,gestureThreshold), (width, gestureThreshold), (0,255,0), 10)




    if hands and buttonPressed is False:
        hand = hands[0]
        fingers=detector.fingersUp(hand)
        cx,cv = hand['center']
        lmList = hand['lmList']
        indexFinger = lmList[8][0], lmList[8][1]
        if cv<=gestureThreshold: #if hand is at the height of the face

            #Gesture 1 - Left
            if fingers ==[1,0,0,0,0]:
                print('left')
                buttonPressed = True
                if imageNumber > 0:
                    imageNumber -= 1
            #Gesture 2 - Right
            if fingers ==[0,0,0,0,1]:
                print('Right')
                buttonPressed = True

                if imageNumber < len(pathImages)-1:
                    imageNumber += 1

        #Gesture 3 - Show pointer
        if fingers ==[0,1,1,0,0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0,0,255), cv2.FILLED)      

    #button pressed iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay :
            buttonCounter = 0
            buttonPressed = False

    #adding webcam image on the slides
    imgsmall = cv2.resize(img, (ws,hs))
    h, w, _ = imgCurrent.shape

    #assigning metrics
    imgCurrent[0:hs, w - ws:w] = imgsmall




    cv2.imshow("Image", img)
    cv2.imshow('Slides', imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break