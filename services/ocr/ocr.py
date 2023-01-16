import re

from PIL import Image
from pytesseract import pytesseract


class Ocr:
    def __init__(self, preprocessed_image):
        self.preprocessed_image = preprocessed_image

    def convert_preprocessed_image_to_text(self):
        # Otwórz obraz
        image = Image.fromarray(self.preprocessed_image)

        # Konwertuj obraz do formatu RGB
        rgb_image = image.convert('RGB')

        # Pobierz dane obrazu jako tablicę
        image_data = rgb_image.getdata()

        # Stwórz nową tablicę z danymi obrazu, zmieniając kolory oprócz ciemnych na białe
        new_image_data = []
        for pixel in image_data:
            # Jeśli kolor jest wystarczająco ciemny, aby uznać go za czarny, zostaw go bez zmian
            if pixel[0] < 150 and pixel[1] < 150 and pixel[2] < 150:
                new_image_data.append(pixel)
            # W przeciwnym razie zamień go na biały
            else:
                new_image_data.append((255, 255, 255))

        # Stwórz nowy obraz z nowymi danymi
        new_image = Image.new('RGB', image.size)
        new_image.putdata(new_image_data)

        # pyplot.imshow(new_image)
        # pyplot.show()

        # Przetwórz obraz na tekst używając biblioteki pytesseract
        config = '-l eng --oem 3 --psm 6'
        predicted_result = pytesseract.image_to_string(new_image, config=config)
        # print(predicted_result)
        ocr_res = re.sub(r'\W+', '', predicted_result)
        # print(ocr_res)
        return ocr_res

    def license_plate_validation(self):
        ocr_result = self.convert_preprocessed_image_to_text()
        pattern_list_2_letter_distinction = [r'^[A-Z]{2}[0-9]{4}[1-9]{1}$',
                                             r'^[A-Z]{2}[0-9]{3}[1-9]{1}[A-Z]{1}$',
                                             r'^[A-Z]{2}[0-9]{2}[1-9]{1}[A-Z]{2}$',
                                             r'^[A-Z]{2}[1-9]{1}[A-Z]{1}[0-9]{2}[1-9]{1}$',
                                             r'^[A-Z]{2}[1-9]{1}[A-Z]{2}[0-9]{1}[1-9]{1}$']
        pattern_list_3_letter_distinction = [r'^[A-Z]{4}[0-9]{2}[1-9]{1}$',
                                             r'^[A-Z]{3}[0-9]{1}[1-9]{1}[A-Z]{2}$',
                                             r'^[A-Z]{3}[1-9]{1}[A-Z]{1}[0-9]{1}[1-9]{1}$',
                                             r'^[A-Z]{3}[0-9]{1}[1-9]{1}[A-Z]{1}[1-9]{1}$',
                                             r'^[A-Z]{3}[1-9]{1}[A-Z]{2}[1-9]{1}$',
                                             r'^[A-Z]{5}[0-9]{1}[1-9]{1}$',
                                             r'^[A-Z]{3}[0-9]{4}[1-9]{1}$',
                                             r'^[A-Z]{3}[0-9]{3}[1-9]{1}[A-Z]{1}$',
                                             r'^[A-Z]{3}[0-9]{2}[1-9]{1}[A-Z]{2}$',
                                             r'^[A-Z]{4}[0-9]{1}[1-9]{1}[A-Z]{1}$',
                                             r'^[A-Z]{4}[1-9]{1}[A-Z]{2}$']
        for pattern in pattern_list_2_letter_distinction:
            if re.match(pattern, ocr_result):
                list_2_letter_distinction = open("services/ocr/2_letter_distinction", "r").read().split("\n")
                letter_distinction = ocr_result[0:2]
                for letter in list_2_letter_distinction:
                    if letter_distinction == letter:
                        return True
                return False
        for pattern in pattern_list_3_letter_distinction:
            if re.match(pattern, ocr_result):
                list_3_letter_distinction = open("services/ocr/3_letter_distinction", "r").read().split("\n")
                letter_distinction = ocr_result[0:3]
                for letter in list_3_letter_distinction:
                    if letter_distinction == letter:
                        return True
                return False
        return False


if __name__ == '__main__':
    test = Ocr("output from find_text method")
    # ocr = test.convert_preprocessed_image_to_text()
    # print(ocr)
    print(test.license_plate_validation())
