import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import styles from './Form.module.scss';
import { CardItem } from 'types/cardItem';


type Props = {
  coordinateOptions: { [key: string]: string[] },
  selectedLatitude: string,
  setSelectedLatitude: (valor:string) => void,
  latitudeOptions:string[],
  longitudeOptions:string[],
  setLongitudeOptions: (valor:string[]) => void,
  setItems: (valor:CardItem[]) => void,
}

export default function FoodTruckForm(
  {
    coordinateOptions,
    selectedLatitude, 
    setSelectedLatitude, 
    latitudeOptions, 
    longitudeOptions,
    setLongitudeOptions,
    setItems }:Props) {

  const changeLatitude = (event:React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedLatitude(event.target.value);
    setLongitudeOptions(coordinateOptions[event.target.value]);
  }

  const searchTrucks = (event:React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    function getRandomImage() {
      const index = 1 + Math.floor(Math.random() * 5);
      return `assets/food_truck${index}.png`
    }

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
          <Form.Label htmlFor="LatitudeSelect" className={styles.formLabel}>Latitude options</Form.Label>
          <Form.Select id="LatitudeSelect" onChange={changeLatitude}>
            {
              latitudeOptions.map((latitude,index) => <option key={index} value={latitude} >{latitude}</option>)
            }
          </Form.Select>
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label htmlFor="LongitudeSelect" className={styles.formLabel}>Longitude options</Form.Label>
          <Form.Select id="LongitudeSelect">
            {
              longitudeOptions.map((longitude, index) => <option key={index} value={longitude}>{longitude}</option>)
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
  