from services.videoToImage.Queue import Queue
import cv2
import os
import shutil


Images = Queue()



def getImages(videoPath):
    if(os.path.exists(videoPath)==False):
        raise FileNotFoundError
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
                name = directory + '/' + str(videoName) +  '(' + str(framenumber) + ').jpg'
                tmp=frame
                Images.push(tmp)
                cv2.imwrite(name, frame)
                framenumber += 1
        else:
            break
        currentframe = (currentframe + 1) if currentframe < FPS_CAP else 0
    video.release()
    # cv2.destroyWindow()


# getImages("car1.mov")
# print(Images.length())