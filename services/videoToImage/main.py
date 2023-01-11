import Queue
import cv2
import os
import shutil


Images = Queue.Queue()

def getImages(videoPath):
    video = cv2.VideoCapture(videoPath)
    currentframe = 0
    framenumber = 0
    directory = "VideoToImages"
    if os.path.exists(directory):
        shutil.rmtree(directory)
        os.makedirs(directory)
    else:
        os.makedirs(directory)
    videoName = os.path.splitext(videoPath)[0]
    FPS_CAP = video.get(cv2.CAP_PROP_FPS)
    while(True):
        isCorrect, frame = video.read()
        if isCorrect:
            if currentframe == 0:
                name = directory + '\\' + str(videoName) +  '(' + str(framenumber) + ').jpg'
                Images.push(frame)
                cv2.imwrite(name, frame)
                framenumber += 1
        else:
            break
        currentframe = (currentframe + 1) if currentframe < FPS_CAP else 0
    video.release()
    cv2.destroyAllWindows()


getImages("car1.mov")
print(Images.length())