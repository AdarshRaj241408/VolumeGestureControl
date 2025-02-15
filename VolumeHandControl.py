import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import pulsectl


def get_volume():
    with pulsectl.Pulse('volume-hand-control') as pulse:
        sink = pulse.sink_list()[0]  # Get first output device
        volume = sink.volume.value_flat * 100  # Convert to percentage
        return volume

# print(f"Current Volume: {get_volume()}%")

def set_volume(volume_percent):
    with pulsectl.Pulse('volume-hand-control') as pulse:
        for sink in pulse.sink_list():
            pulse.volume_set_all_chans(sink, volume_percent / 100)

minVol = 0
maxVol = 100
volBar = 400
volume = 0
volPer = 0


#############################
wCam, hCam = 640,480
#############################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
    
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy),10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        # hand range is from 20 to 260
        # volume range is 0 to 100

        volume = np.interp(length, [20, 200], [minVol, maxVol])
        volBar = np.interp(length, [20, 200], [400, 150])
        volPer = np.interp(length, [20, 200], [0, 100])
        print(volume)
        set_volume(volume)

        if length < 30:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        
    cv2.rectangle(img, (50, 150), (85, 400), (255, 85, 45), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 85, 45), cv2.FILLED)
    cv2.putText(img, f'{(int(volPer))} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 85, 45), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {(int(fps))}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 85, 45), 3)
    cv2.imshow("Img", img)
    cv2.waitKey(1)