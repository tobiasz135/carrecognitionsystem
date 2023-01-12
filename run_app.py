from datetime import datetime
from time import sleep

import cv2
import matplotlib.pyplot as plt

import services.preprocessing as preprocessing
import services.ocr as ocr
import services.klient as klient
import services.videoToImage.main
from services.videoToImage.Queue import Queue
from services.videoToImage.main import getImages
from services.preprocessing.preprocessing import Preprocessing
from services.ocr.ocr import Ocr
from services.klient.klient import Server


def add_car_name_to_file(name):
    with open("car_base.txt", "w") as file:
        file.write(name)
        file.write('\n')


def delete_car_name_from_file(name):
    with open("car_base.txt", 'r') as file:
        lines = file.readlines()

    with open("car_base.txt", 'w') as file:
        for line in lines:
            if line.strip("\n") != name:
                file.write(line)


if __name__ == '__main__':
    client = Server()
    h = 0
    preprocessing = Preprocessing('services/preprocessing/harascade_car.xml', 750)
    getImages("services/videoToImage/car1.mov")
    queue = services.videoToImage.main.Images
    print(queue.length())
    while not queue.isEmpty():
        tmp = queue.pop()
        image = tmp[0]
        path = tmp[1]
        plt.imshow(image)
        plt.show()
        try:
            image = preprocessing.find_plate(image)
            image = preprocessing.find_text(image)
            ocr = Ocr(image)
            text = ocr.convert_preprocessed_image_to_text()
            if ocr.license_plate_validation():
                add_car_name_to_file(text)
                print(text)
                path = f'/registers/photo{h}.jpg'
                cv2.imwrite(f'public/registers/photo{h}.jpg', tmp[0])
                h += 1
                client.addCar(path, text, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                break
        except:
            continue
    # client.send_car_list(client.car_list)
    sleep(5)
    client.close()
