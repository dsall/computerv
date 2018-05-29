#import required libraries
#import OpenCV library
import cv2
import numpy as np
import os
import time

Color = (255,0,0)
image = cv2.imread('jibby.jpg')
def detect_face(photo):
    face_cascade = cv2.CascadeClassifier('lb_front.xml')
    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(photo, 1.2, 5);
    if (len(face) == 0):
        return None, None

    (x, y, w, h) = face[0]
    return gray[y:y+w, x:x+h], face[0]
    print("Number of faces:", face)

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    #list to hold all subject faces
    faces = []
    #list to hold labels for all subjects
    labels = []

    #let's go through each directory and read images within it
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue;
    label = int(dir_name.replace("s", ""))
    subject_dir_path = data_folder_path + "/" + dir_name
    for image_name in subject_images_names:
        if image_name.startswith("."):
            continue;
    image_path = subject_dir_path + "/" + image_name
          
detection = detect_face(image)

cv2.imshow("photo",detection)

cv2.waitKey(0)
cv2.destroyAllWindows()
