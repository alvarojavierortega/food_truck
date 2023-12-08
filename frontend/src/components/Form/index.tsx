import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import styles from './Form.module.scss';
import { CardItem } from 'types/cardItem';
import { Coordinate, Coordinates } from 'types/coordinates';
import { getFoodTrucks } from '../../api/Services';


type Props = {
  coordinateOptions:  Coordinates,
  selectedCoordinate: Coordinate,
  setSelectedCoordinate: (valor:Coordinate) => void,
  setItems: (valor:CardItem[]) => void,
}

function getRandomImage() {
  const index = 1 + Math.floor(Math.random() * 5);
  return `assets/food_truck${index}.png`
}


export default function FoodTruckForm(
  {
    coordinateOptions,
    selectedCoordinate,
    setSelectedCoordinate, 
    setItems }:Props) 
  {

  const changeSelectedCoordinate = (event:React.ChangeEvent<HTMLSelectElement>) => {
    const id = Number(event.target.value)
    const selectedCoordinate = coordinateOptions.filter(function(element){
      return element.id == id;
    });
    setSelectedCoordinate(selectedCoordinate[0]);
  }

  const searchTrucks = (event:React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    const fetchData = async () => {
      const items = await getFoodTrucks(selectedCoordinate.id);
      const items1:CardItem[] = items.map(obj => ({ ...obj, image: getRandomImage() }))
      setItems(items1)
    }

    fetchData()

  }

  return (
    <Form onSubmit={searchTrucks}>
      <fieldset>

        <Form.Group className="mb-3" >
          <Form.Label htmlFor="coordinateSelect" className={styles.formLabel}>Coordinate options</Form.Label>
          <Form.Select id="coordinateSelect" onChange={changeSelectedCoordinate}>
            {
              coordinateOptions.map(
                (coordinate) => <option key={coordinate.id} value={coordinate.id} >
                  latitude: {coordinate.latitude} longitude: {coordinate.longitude}
                  </option>
              )
            }
          </Form.Select>
        </Form.Group>

        <Button 
          type="submit" 
          style={{fontSize:'24px', margin:'auto', width:'100%'}}
          >
          Find food trucks
        </Button>

      </fieldset>
    </Form>
  )
  }
  