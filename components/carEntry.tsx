export default function CarEntry(carData: any) {
    const {carEntryDate, carLicensePlate, carImage} = carData || {};
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
                <img className="carImage" src={carImage} alt="Car image here" width="100"/>  
            </div>
        </div>
    );
}