import os
import numpy as np
import cv2
import pickle
from PIL import Image

# def trainfaces():
#     # BASE_DIR=os.path.dirname(os.path.abspath(__file__))
#     BASE_DIR="C:\\\\Users\\\\muham\\\\Desktop\\\\opencv\\\\opencv"
#     image_dir=os.path.join(BASE_DIR,"data")
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     recognizer = cv2.face.LBPHFaceRecognizer_create()

#     current_id=0
#     label_ids={}
#     y_labels=[]
#     x_train=[]

#     for root,dirs,files in os.walk(image_dir):
#         for file in files:
#             if file.endswith("png") or file.endswith("jpg"):
#                 path= os.path.join(root,file)
#                 # path=cv2.cvtColor(path,cv2.COLOR_BGR2GRAY) 
#                 label =os.path.basename(os.path.dirname(path)).replace(" ","-")
#                 #print(label,path)
#                 if not label in label_ids:
#                     label_ids[label]=current_id
#                     current_id+=1
                
#                 id_=label_ids[label]
#                 #print(label_ids)
#                 # y_labels.append(label) 
#                 # x_train.append(path)
#                 # pil_image = Image.open(path).convert("L")

#                 pil_image=cv2.imread(path)
#                 img = cv2.cvtColor(pil_image,cv2.COLOR_BGR2GRAY)
#                 size =(550,550)
#                 # final_image=pil_image.resize(size,Image.ANTIALIAS)
#                 # final_image=cv2.resize(img,)
#                 # image_array = np.array(final_image,"uint8")
#                 image_array = np.array(img,"uint8") 
#                 #print(image_array)                       
#                 faces =face_cascade.detectMultiScale(image_array,scaleFactor=1.5, minNeighbors=5)

#                 for (x,y,w,h) in faces:
#                     roi= image_array[y:y+h,x:x+w]
#                     x_train.append(roi)
#                     y_labels.append(id_)

#     print(y_labels)
#     print(x_train)

#     with open("labels.pickle","wb") as f:
#         pickle.dump(label_ids,f)

#     recognizer.train(x_train,np.array(y_labels))
#     recognizer.save("trainner.yml")
# trainfaces()  # Call the trainfaces function to perform face recognition training



#gpt

import os
import numpy as np
import cv2
import pickle

def train_faces():
    BASE_DIR = "C:\\Users\\moses\\Desktop\\opencv\\data"  # Base directory containing subfolders for each person
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    label_ids = {}  # Dictionary to map face labels to IDs
    x_train = []    # List to store face images
    y_labels = []   # List to store face labels

    for root, dirs, files in os.walk(BASE_DIR):
        for dir_name in dirs:  # Each subfolder represents a person
            label = dir_name
            if label not in label_ids:
                label_ids[label] = len(label_ids)  # Assign a unique ID to each person
            label_id = label_ids[label]

            dir_path = os.path.join(root, dir_name)
            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                if file.endswith("png") or file.endswith("jpg"):
                    image = cv2.imread(file_path)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                    for (x, y, w, h) in faces:
                        roi = gray[y:y+h, x:x+w]
                        x_train.append(roi)
                        y_labels.append(label_id)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainner.yml")

    with open("labels.pickle", "wb") as f:
        pickle.dump(label_ids, f)

    print("Training completed successfully.")

train_faces()
