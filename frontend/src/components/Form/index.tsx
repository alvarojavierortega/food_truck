import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import styles from './Form.module.scss';
import { CardItem } from 'types/cardItem';
import { Coordinate, Coordinates } from 'types/coodinates';


type Props = {
  coordinateOptions:  Coordinates,
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

    
    // fetch('http://localhost:8080/db')
    //       .then(resposta => resposta.json())
    //       .then(datos => {setRacas(dados)})  

    const items: Omit<CardItem, 'image'>[] = [
      {
        id:1,
        title:'my title',
        description: 'some description'
      },
      {
        id:2,
        title:'my title',
        description: 'some description'
      },
      {
        id:3,
        title:'my title',
        description: 'some description'
      },
      {
        id:4,
        title:'my title',
        description: 'some description'
      },
      {
        id:5,
        title:'my title',
        description: 'some description'
      },
      {
        id:6,
        title:'my title',
        description: 'some description'
      },
      {
        id:7,
        title:'my title',
        description: 'some description'
      },
      {
        id:8,
        title:'my title',
        description: 'some description'
      }
    ]

    const items1:CardItem[] = items.map(obj => ({ ...obj, image: getRandomImage() }))

    setItems(items1)

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
  