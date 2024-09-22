import numpy as np 
import cv2 
import pickle

def capture():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("C:\\Users\\moses\\Desktop\\opencv\\trainner.yml")
    labels={}
    xy=""

    with open("C:\\Users\\moses\\Desktop\\opencv\\labels.pickle","rb") as f:
        og_labels=pickle.load(f)
        labels={v:k for k,v in og_labels.items()}
    cap = cv2.VideoCapture(0)

    while (True):
        #toma frame por frame
        ret, frame = cap.read()
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces =face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=1,minSize=(30, 30))

        for (x,y,w,h ) in faces:
            #print(x,y,w,h)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=frame[y:y+h,x:x+w]

            id_,conf=recognizer.predict(roi_gray)
            if conf>=45 and conf<=85:
                #print(id_)
                #print(labels[id_])
                font=cv2.FONT_HERSHEY_SIMPLEX
                name= labels[id_]
                xy = name
                stroke=2
                color=(255,255,255)
                cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
                
            #img_item = "my-image.png"
            #cv2.imwrite(img_item,roi_gray)
            else:
                font=cv2.FONT_HERSHEY_SIMPLEX
                name= "unknown"
                stroke=2
                color=(255,255,255)
                cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            color =(255,0,0) #bgr
            stroke= 2
            end_cord_x =x + w
            end_cord_y =y + h
            cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
           

        #show the frame
        cv2.imshow('Frame',frame)
        # if xy !="unknown":
        #     print(xy)
        #     break
             

        if cv2.waitKey(20) & 0xFF == ord('q'):
         
            cap.release()
            cv2.destroyAllWindows()
            return name
           

    
    

result = capture()
print(result)    



#gpt

# import numpy as np 
# import cv2 
# import pickle

# def recognize_faces():
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.read("C:\\\\Users\\\\muham\\\\Desktop\\\\opencv\\\\opencv\\\\trainner.yml")

#     labels = {}
#     with open("C:\\\\Users\\\\muham\\\\Desktop\\\\opencv\\\\opencv\\\\labels.pickle", "rb") as f:
#         labels = pickle.load(f)
#         labels = {v: k for k, v in labels.items()}

#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

#         for (x, y, w, h) in faces:
#             roi_gray = gray[y:y+h, x:x+w]
#             id_, conf = recognizer.predict(roi_gray)
            
#             if conf >=50 and conf <= 85:
#                 name = labels[id_]
#             else:
#                 name = "unknown"

#             font = cv2.FONT_HERSHEY_SIMPLEX
#             color = (255, 255, 255)
#             stroke = 2
#             cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#         cv2.imshow('Frame', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# recognize_faces()
