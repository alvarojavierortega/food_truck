import { CardItem } from 'types/cardItem';
import FoodTruckForm from '../components/Form';
import Trucks from '../components/Trucks';
import styles from './Pages.module.scss'
import React, { useEffect, useState } from "react";
import { Coordinate, Coordinates } from 'types/coodinates';
import { getCoordinateOptions} from '../api/Services';



export default function FoodTruckPage() {

  const initialCoordinateOptions: Coordinates = [
    {id:0, latitude:"", longitude:""}
  ]
  const initialItems: CardItem[] = []
  const [items, setItems] = useState(initialItems)
  const [coordinateOptions, setCoordinateOptions] = useState(initialCoordinateOptions)
  const [selectedCoordinate, setSelectedCoordinate] = useState(initialCoordinateOptions[0])
  

  useEffect(() => {

    const fetchData = async () => {
      const coordinateOptions = await getCoordinateOptions();
      setCoordinateOptions(coordinateOptions)     
      setSelectedCoordinate(coordinateOptions[0])
    }

    fetchData()

  },[])  


  

  return (
    <>
      <h1 className={styles.title}> Find your amazing food banner </h1>
      <FoodTruckForm 
        coordinateOptions={coordinateOptions}
        setSelectedCoordinate={(value:Coordinate) => setSelectedCoordinate(value)}
        setItems={(value:CardItem[]) => setItems(value)}
      />
      <Trucks 
        items={items}
      />
    </>
  )
}


  