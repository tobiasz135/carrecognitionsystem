import cv2
import skimage.filters.thresholding
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import imutils as im
from pytesseract import pytesseract
from skimage.filters import try_all_threshold



class Preprocessing:
    def __init__(self,path_to_classifier,size_of_image):
        # zaladowanie klasyfikatora
        self.haras=cv2.CascadeClassifier(path_to_classifier)
        # rozmiar obrazu
        self.size_of_image=size_of_image
    def find_plate(self,image):
        # zmiana rozmiaru obrazu
        img = imutils.resize(image, width=self.size_of_image)
        # zmiana koloru obrazu na szary
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # wykrywanie tablicy rejestracyjnej
        segments = self.haras.detectMultiScale(img_gray, 1.2)
        car_register = []
        # wyciecie wszystkich potencjalnych tablic rejestracyjnych
        for (x, y, w, h) in segments:
            car_register.append(img[y:y + h, x:x + w])
        # posortowanie tablic rejestracyjnych od najwiekszej do najmniejszej
        car_register = sorted(car_register, key=lambda x: x.shape[0] * x.shape[1], reverse=True)
        # zwracamy potencjalna tablice rejestracyjna o najwiekszym polu
        return car_register[0]
    def find_text(self,image):
        tmp_copy = image.copy()
        # wyblurowanie obrazu aby usunac szum i niepotrzebne elementy
        tmp_copy = cv2.GaussianBlur(tmp_copy, (5, 5), 0)
        # zmiana koloru obrazu na szary
        tmp_gray = cv2.cvtColor(tmp_copy, cv2.COLOR_RGB2GRAY)
        # zastosowanie metody Otsu do wykrycia obiektow ktore sa najasniesze
        otsu_thresh_val = skimage.filters.thresholding.threshold_otsu(tmp_gray)
        thresh_img = tmp_gray > otsu_thresh_val
        # wykrywanie konturów na obrazie z najaśniejszymi obiektami
        countours, _ = cv2.findContours(thresh_img.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # posortowanie konturów od najwiekszego do najmniejszego i wybranie 10 najwiekszych
        countours = sorted(countours, key=cv2.contourArea, reverse=True)[:10]
        for c in countours:
            # wyznaczenie prostokata otaczajacego kontur
            x, y, w, h = cv2.boundingRect(c)
            # sprawdzenie czy kontur jest prostokatem na podstawie stosunku dlugosci do szerokosci
            # zakres 4-7 najlepiej sprawdza sie dla tablic rejestracyjnych
            ar = w / h
            if ar >= 4 and ar <= 7:
                return image[y:y + h, x:x + w]
        return None



if __name__ == '__main__':
    img = cv2.imread('preprocessing/IMG_0892.jpg')
    P=None
    text=None
    plate=None
    try:
        P = Preprocessing('preprocessing/harascade_car.xml', 750)
    except:
        print('Problem with classifier')
        exit(0)
    try:
        plate = P.find_plate(img)
    except:
        print('Problem with finding plate')
        exit(0)
    try:
        text = P.find_text(plate)
    except:
        print('Problem with finding text')
        exit(0)
    if text is not None:
        plt.imshow(text)
        plt.show()


