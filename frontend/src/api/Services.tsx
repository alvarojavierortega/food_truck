import { Coordinates } from "types/coordinates";
import { ApiCoordinate } from "./types"

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