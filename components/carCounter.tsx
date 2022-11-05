import {useState} from 'react';

export default function CarCounter(carNumber: any) {
    console.log(carNumber['carCount']);
    return (
        <div className="carCounter">
            <h2>Liczba pojazdów na parkingu: {carNumber['carCount']} </h2>

        </div>
    );
}