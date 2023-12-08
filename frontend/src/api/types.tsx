
export type ApiCoordinate = {
    locationId: number;
    latitude: string;
    longitude: string;
    applicants: []
  };


export type ApiFoodTruck = {
  id: number;
  applicant: string;
  facilityType: string;
  cnn: number,
  locationDescription: string,
  location: number
}