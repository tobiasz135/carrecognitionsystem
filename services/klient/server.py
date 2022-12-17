import socket
import json
from threading import Thread
from time import sleep
import socketio

#HOST i PORT to stałe które określają adres i port na którym nasłuchuje serwer
HOST = "127.0.0.1"
PORT = 8484

#Klasa Server obiekt tej klasy będzie nasłuchiwał na określonym porcie i adresie
class Server(Thread):
    def __init__(self):
        super().__init__()
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sio= socketio.Client()

        self.sio.connect('http://localhost:8484')
        print("Connected to server")
        self.car_list = []

    def run(self):
        self.listen()
    #Funkcja dodająca samochód do listy wraz z jego parametrami
    def addCar(self,pathToImage,carRegister,Date):
        new_car = {
            "pathToImage": pathToImage,
            "carLicensePlate": carRegister,
            "carEntryDate": Date,
        }
        self.car_list.append(new_car)
        self.send_car_list(self.car_list)
    #Funkcja usuwająca samochód z listy
    def removeCar(self,carRegister):
        for car in self.car_list:
            if car["carLicensePlate"] == carRegister:
                self.car_list.remove(car)
                self.send_car_list(self.car_list)
                return True
        return False
    #Zamykanie połączenia
    def close(self):
        self.sio.disconnect()
    #Funkcja nasłuchująca na połączenie z klientem i odbierająca dane od klienta, uruchamiana w osobnym wątku
    def listen(self):
        self.sio.wait()
        print("Connection closed")
        self.close()
    #Funkcja wysyłająca dane do klienta w formacie json
    def send_car_list(self,carListJson):
        print("Sending data to client")
        self.sio.send(json.dumps(carListJson))
if __name__ == '__main__':
    server=Server()
    #server.start()
    server.addCar("path/to/image","EWI 123","2019-01-01")
    server.addCar("path/to/image", "EWI 1234", "2019-01-01")
    #server.send_car_list(server.car_list)
    sleep(5)
    #server.removeCar("EWI 123")
    if(server.removeCar("EWI 123")):
        print("Car removed")
        server.send_car_list(server.car_list)
    sleep(5)
    if(server.removeCar("EWI 1234")):
        print("Car removed")
        #server.send_car_list(server.car_list)
    
    server.close()

    #server.join()


