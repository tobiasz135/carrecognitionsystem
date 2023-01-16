from datetime import datetime
from time import sleep

import cv2

import services.videoToImage.main
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
    try:
        client = Server()
    except:
        print("Wlacz serwer node.js")
        exit(1)
    h = 0

    preprocessing = Preprocessing('services/preprocessing/harascade_car.xml', 750)
    while True:

        path_to_image=input("Podaj sciezke\n")
        if path_to_image=='q':
            break
        try:
            getImages(path_to_image)
        except:
            continue
        queue = services.videoToImage.main.Images
        while not queue.isEmpty():
            image = queue.pop()
            image_tmp=image.copy()
            ocr=None
            text=None
            try:
                image = preprocessing.find_plate(image)
                image = preprocessing.find_text(image)
                ocr = Ocr(image)
                text = ocr.convert_preprocessed_image_to_text()
            except:
                continue
            try:
                if ocr.license_plate_validation():
                    add_car_name_to_file(text)
                    print(text)
                    path = f'/registers/photo{h}.jpg'
                    cv2.imwrite(f'public/registers/photo{h}.jpg', image_tmp)
                    h += 1
                    client.addCar(path, text, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    break
            except:
                print("Nie prawidlowa rejestracja")
                continue
            print("Nie znaleziono rejestracji samochodowej")
    sleep(5)
    client.close()
    exit(0)
