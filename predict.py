import numpy as np
from keras.models import model_from_json
import operator
import cv2
import random
import pygame
import glob
import sys, os

# Loading the model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)

# load weights into new model
loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

font = cv2.FONT_HERSHEY_COMPLEX_SMALL

cap = cv2.VideoCapture(0)

# Category dictionary
categories = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE','a':'A','b':'B','bstofluck':'All The Best','c':'C','d':'D','e':'E','h':'H','i':'I','l':'L','namasthe':'Namasthe','o':'O','p':'P','u':'U','x':'X','y':'Y','z':'Z'}

while True:
    _, frame = cap.read()
    height,width = frame.shape[:2]
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Got this from collect-data.py
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]

    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.resize(roi, (64, 64)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    # Batch of 1
    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))

    prediction = {'ZERO': result[0][0], 
                  'ONE': result[0][1], 
                  'TWO': result[0][2],
                  'THREE': result[0][3],
                  'FOUR': result[0][4],
                  'FIVE': result[0][5],
                  'A' : result[0][6],
                  'B' : result[0][7],
                  'All The Best' : result[0][8],
                  'C' : result[0][9],
                  'D' : result[0][10],
                  'E' : result[0][11],
                  'H' : result[0][12],
                  'I' : result[0][13],
                  'L' : result[0][14],
                  'Namasthe' : result[0][15],
                  'O' : result[0][16],
                  'P' : result[0][17],
                  'U' : result[0][18],
                  'X' : result[0][19],
                  'Y' : result[0][20],
                  'Z' : result[0][21]}

    sa = max(result[0]*100)
    
    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    
    # Displaying the predictions
    cv2.rectangle(frame, (x1, y1+260) , (x2, y2) , (0,0,0),-6)

    if sa>99:
        # Displaying the predictions
        cv2.putText(frame,"  "+prediction[0][0],(x1, y1+290), font, 1,(255,255,255),1,cv2.LINE_AA)

        pred = prediction[0][0]

        songs = glob.glob("voice/%s.mp3"%pred)
        song = random.choice(songs)
        pygame.mixer.init()
        music = pygame.mixer.music.load(song)
        pygame.mixer.music.play()
                
        time = 0
                
        while (pygame.mixer_music.get_busy()):
            pygame.time.Clock().tick(10)
            time+=1
            if time == 14:
                pygame.mixer_music.stop()
                time = 0
                    
    #cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)    
    cv2.imshow("Frame", frame)
    
    interrupt = cv2.waitKey(1)
    if interrupt & 0xFF == ord('s'): # esc key
        break
        
 
cap.release()
cv2.destroyAllWindows()
