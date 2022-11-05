export default function CarEntry(carData: any) {
    const {carEntryDate, carLicensePlate} = carData || {};
    return (
        <div className="carEntry">
            <h2>Informacje o pojeździe</h2>
            <div className="inner">
                <div className="carDetails">
                    <div className="carEntryDate">
                        <h3>Data wjazdu:</h3> {carEntryDate}
                    </div>
                    <div className="carLicensePlate">
                        <h3>Numer rejestracyjny:</h3> {carLicensePlate}
                    </div>

                </div>
                <img className="carImage" src="https://thedrinkitgame.pl/DrinkIt_new2.png" alt="DrinkIt logo" width="100"/>  
            </div>
        </div>
    );
}