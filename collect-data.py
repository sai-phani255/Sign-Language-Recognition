import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    os.makedirs("data/train/a")
    os.makedirs("data/test/a")
    os.makedirs("data/train/b")
    os.makedirs("data/test/b")
    os.makedirs("data/train/bstofluck")
    os.makedirs("data/test/bstofluck")
    
    os.makedirs("data/train/c")
    os.makedirs("data/test/c")
    
    os.makedirs("data/train/d")
    os.makedirs("data/test/d")

    os.makedirs("data/train/e")
    os.makedirs("data/test/e")
    
    os.makedirs("data/train/h")
    os.makedirs("data/test/h")

    os.makedirs("data/train/i")
    os.makedirs("data/test/i")

    os.makedirs("data/train/l")
    os.makedirs("data/test/l")
    
    os.makedirs("data/train/o")
    os.makedirs("data/test/o")
    
    os.makedirs("data/train/u")
    os.makedirs("data/test/u")

    os.makedirs("data/train/p")
    os.makedirs("data/test/p")

    os.makedirs("data/train/namasthe")
    os.makedirs("data/test/namasthe")

    os.makedirs("data/train/x")
    os.makedirs("data/test/x")
    
    os.makedirs("data/train/y")
    os.makedirs("data/test/y")
    os.makedirs("data/train/z")
    os.makedirs("data/test/z")


# Train or test 
mode = 'train'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'a': len(os.listdir(directory+"/a")),
             'b': len(os.listdir(directory+"/b")),
             'bstofluck': len(os.listdir(directory+"/bstofluck")),
             'c': len(os.listdir(directory+"/c")),
             'd': len(os.listdir(directory+"/d")),
             'e': len(os.listdir(directory+"/e")),
             'namasthe': len(os.listdir(directory+"/namasthe")),
             'i': len(os.listdir(directory+"/i")),
             'l': len(os.listdir(directory+"/l")),
             'u': len(os.listdir(directory+"/u")),
            'h': len(os.listdir(directory+"/h")),
            'o': len(os.listdir(directory+"/o")),
             'p': len(os.listdir(directory+"/p")),
             'x': len(os.listdir(directory+"/x")),
             'y': len(os.listdir(directory+"/y")),
             'z': len(os.listdir(directory+"/z")),
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ZERO : "+str(count['zero']), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "A : "+str(count['a']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Bstofluck : "+str(count['bstofluck']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.putText(frame, "B : "+str(count['b']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "P : "+str(count['p']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.putText(frame, "H : "+str(count['h']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.putText(frame, "O : "+str(count['o']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.putText(frame, "X : "+str(count['x']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.putText(frame, "U : "+str(count['u']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
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
    roi = cv2.resize(roi, (64, 64)) 
 
    cv2.imshow("Frame", frame)
    
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
        
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'a/'+str(count['a'])+'.jpg', roi)
    #if interrupt & 0xFF == ord('b'):
    #    cv2.imwrite(directory+'b/'+str(count['b'])+'.jpg', roi)

    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'bstofluck/'+str(count['bstofluck'])+'.jpg', roi)
    
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'c/'+str(count['c'])+'.jpg', roi)

    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'d/'+str(count['d'])+'.jpg', roi)

    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'e/'+str(count['e'])+'.jpg', roi)

    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'h/'+str(count['h'])+'.jpg', roi)

    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'namasthe/'+str(count['namasthe'])+'.jpg', roi)
    
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'i/'+str(count['i'])+'.jpg', roi)

    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'l/'+str(count['l'])+'.jpg', roi)

    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'o/'+str(count['o'])+'.jpg', roi)

    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'x/'+str(count['x'])+'.jpg', roi)


    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'p/'+str(count['p'])+'.jpg', roi)

    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'u/'+str(count['u'])+'.jpg', roi)

        
cap.release()
cv2.destroyAllWindows() 

