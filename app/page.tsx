'use client';
import CarEntry from '../components/carEntry';
import CarCounter from '../components/carCounter';
import { Server } from "socket.io";
import { useEffect, useState } from 'react'
import io from 'socket.io-client'
let socket: any;

export default function HomePage(){
    //var count = 5;
    const [count, setCount] = useState(0)

    useEffect(() => {
        console.log("fetching socket...")
        socket = io("http://localhost:8484");
        //socket = io()
        console.log(socket)
  
        socket.on('connect', () => {
            console.log('connected')
        })
    
        socket.on('countUpdate', (msg:any) => {
            setCount(msg)
        })
        return () => {
          console.log("This will be logged on unmount");
        }
      }, []);
  
  
    return(
        <div className="container">
            <span className="center"><h1>Projekt PSIO - rozpoznawanie rejestracji samochodów</h1></span>
            <CarCounter carCount={count}/>
            <CarEntry carEntryDate="2021-05-01" carLicensePlate="WAW1234"/>
            <CarEntry carEntryDate="2022-11-05" carLicensePlate="EWIWA81"/>
            <span className="center"><p>Home page body content</p></span>
        </div>
    );
}