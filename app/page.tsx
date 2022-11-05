import CarEntry from '../components/carEntry';
import CarCounter from '../components/carCounter';

export default function HomePage(){
    var count = 5;
    return(
        <div>
            <h1>Home Page</h1>
            <CarCounter carCount={count}/>
            <CarEntry carEntryDate="2021-05-01" carLicensePlate="WAW1234"/>
            <CarEntry carEntryDate="2022-11-05" carLicensePlate="EWIWA81"/>
            <p>Home page body content</p>
        </div>
    );
}