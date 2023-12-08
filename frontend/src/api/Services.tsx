import { Coordinates } from "types/coordinates";
import { ApiCoordinate, ApiFoodTruck } from "./types"
import { CardItem } from "types/cardItem";

export const getCoordinateOptions = async () => {
    const data  = await fetch('http://localhost:5050/api/locations/')
    const dataJson = await data.json();
    const mappedData: Coordinates = dataJson.results.map((item:ApiCoordinate) => {
        return {id: item.locationId, 
                latitude:item.latitude,
                longitude:item.latitude}
    } )
    return mappedData;
}


export const getFoodTrucks = async (locationId:number) => {
    const data  = await fetch(`http://localhost:5050/api/locations/${locationId}/`)
    const dataJson = await data.json();
    const mappedData: Omit<CardItem, 'image'>[] = dataJson.applicants.map((item:ApiFoodTruck ) => {
        return {id: item.id, 
                title:item.applicant,
                description:item.locationDescription}
    } )
    return mappedData;
}