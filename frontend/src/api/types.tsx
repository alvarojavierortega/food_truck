
export type ApiCoordinate = {
    locationId: number;
    latitude: string;
    longitude: string;
  };


export type ApiFoodTruck = {
  id: number;
  applicant: string;
  facilityType: string;
  cnn: number,
  locationDescription: string,
  location: number
}