from cv2 import cv2

platecascade = cv2.CascadeClassifier("data\haarcascade_russian_plate_number.xml")
frameWidth  = 640
frameHeight = 400
livecap = cv2.VideoCapture(0)
livecap.set(3, frameWidth)      
livecap.set(4, frameHeight)
livecap.set(10, 150)
count = 0
while True:
    success, img = livecap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = platecascade.detectMultiScale(imgGray,1.1,4)
    for (x, y, w, h)  in plates:
        area = w*h
        if area > 500:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img, "number_plate", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), 1)
            plateArea = img[y:y+h,x:x+w]
            cv2.imshow("live cam", plateArea)
    cv2.imshow("live cam", img)        
    if cv2.waitKey(1) & 0xFF ==ord('s'):     # once it detected numeber plate press s to save the plate imge in directory as written in imwrite
        cv2.imwrite("data\scannedPlates\plate_"+str(count)+".jpg",plateArea)
        count+= 1
        
