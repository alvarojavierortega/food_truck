import { CardItem } from 'types/cardItem';
import FoodTruckForm from '../components/Form';
import Trucks from '../components/Trucks';
import styles from './Pages.module.scss'
import React, { useEffect, useState } from "react";

export default function FoodTruckPage() {

  const initialCoordinateOptions: { [key: string]: string[] } = {
    "": [""],
  }
  
  const [coordinateOptions, setCoordinateOptions] = useState(initialCoordinateOptions)
  const latitudeOptions = Object.keys(coordinateOptions); 
  const [selectedLatitude, setSelectedLatitude] = useState(latitudeOptions[0])
  const [longitudeOptions, setLongitudeOptions] = useState(coordinateOptions[selectedLatitude])

  useEffect(() => {
    // fetch('http://localhost:8080/db')
    //       .then(resposta => resposta.json())
    //       .then(datos => {setRacas(dados)})   
   
    const coordinateOptions: { [key: string]: string[] } = {
      "lat1": ["lon11", "lon12", "lon13"],
      "lat2": ["lon22", "lon22"],
    }
    setCoordinateOptions(coordinateOptions)     
    const latitudeOptions = Object.keys(coordinateOptions); 
    setSelectedLatitude(latitudeOptions[0])
    setLongitudeOptions(coordinateOptions[latitudeOptions[0]])

  },[])  


  const initialItems: CardItem[] = []
  const [items, setItems] = useState(initialItems)

  return (
    <>
      <h1 className={styles.title}> Find your amazing food banner </h1>
      <FoodTruckForm 
        coordinateOptions={coordinateOptions}
        selectedLatitude={selectedLatitude}
        setSelectedLatitude={(value:string) => setSelectedLatitude(value)}
        latitudeOptions={latitudeOptions}
        longitudeOptions={longitudeOptions}
        setLongitudeOptions={(value:string[]) => setLongitudeOptions(value)}
        setItems={(value:CardItem[]) => setItems(value)}
      />
      <Trucks 
        items={items}
      />
    </>
  )
}


  