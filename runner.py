import time
import cv2
from torch import imag
from fetchFile import FetchFile

if __name__ == '__main__':
    while True:
        print("""Face Detection Menu
            1. Detect with Image
            2. Detect with Video Feed
            3. Detect with Live Video Feed
            99. Exit
        """)
        command = input("Enter Index: ")
        if command.isdigit():
            index = int(command)
            faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
            if index == 1:
                imgsrc = FetchFile()
                image = cv2.imread(imgsrc)
                grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(grayScaleImage, 1.1, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                resizedImage = cv2.resize(image, (500, 600))
                cv2.imshow('Facial Recognizing', resizedImage)
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break
            elif index == 2:
                videosrc = FetchFile('videos')
                cap = cv2.VideoCapture(videosrc)
                # fps= int(cap.get(cv2.CAP_PROP_FPS))
                while True:
                    _, image = cap.read()
                    grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(grayScaleImage, 1.1, 4)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    resizedImage = cv2.resize(image, (500, 600))
                    cv2.imshow('Facial Recognizing', resizedImage)
                    k = cv2.waitKey(1) & 0xff
                    if k == 27:
                        break
                cap.release()
            elif index == 3:
                cap = cv2.VideoCapture(0)
                while True:
                    _, image = cap.read()
                    grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(grayScaleImage, 1.1, 4)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    resizedImage = cv2.resize(image, (500, 600))
                    cv2.imshow('Facial Recognizing', resizedImage)
                    k = cv2.waitKey(30) & 0xff
                    if k == 27:
                        break
                cap.release()
            elif index == 99:
                print("""Success
                Thanks for using our program
                """)
                exit()
            else:
                print("""Error
                Thanks for using our program
                """)
                exit()
        else:
            print("Invalid Option Choosed")