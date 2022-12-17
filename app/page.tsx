'use client';
import CarEntry from '../components/carEntry';
import CarCounter from '../components/carCounter';
import EmptyCarLot from '../components/emptyCarLot';
import { Server } from "socket.io";
import { useEffect, useState } from 'react'
import io from 'socket.io-client'
let socket: any;

export default function HomePage(){
    //var count = 5;
    const [count, setCount] = useState(0)
    const [carList, setCarList] = useState([])
    useEffect(() => {
        console.log("fetching socket...")
        socket = io("http://localhost:8484");
        //socket = io()
        console.log(socket)
  
        socket.on('connect', () => {
            console.log('connected')
        })

        socket.on("carListUpdate", (msg:any) => {
            console.log(msg);
            setCarList(JSON.parse(msg));
        })
    
        socket.on('countUpdate', (msg:any) => {
            setCount(msg)
        })
        return () => {
          console.log("This will be logged on unmount");
        }
      }, []);

    useEffect(() => {
        console.log("Changing background image");
        document.getElementById("root").style.backgroundImage = carList.length === 0 ? 'url("/652.jpg")' : 'url("/1736.jpg")';
        //document.body.style.backgroundImage = carList.length === 0 ? 'url("/1915.jpg")' : 'url("/613.jpg")';
    }, [count, carList]);
  
  
    return(
        <div className="container">
            <span className="center"><h1>Projekt PSIO - rozpoznawanie rejestracji samochodów</h1></span>
            <CarCounter carCount={count}/>
            {carList.length > 0 ? carList.map((car: any) => {
                return <CarEntry key={car.carLicensePlate} carEntryDate={car.carEntryDate} carLicensePlate={car.carLicensePlate} carImage={car.pathToImage}/>
            }) : <EmptyCarLot/>
            }
        </div>
    );
}