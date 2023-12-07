import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { CardItem } from 'types/cardItem';

type CardItems={
  items: CardItem[]
}

const FoodTruckCard = ({items}: CardItems) => {
  return  (
  <ul>
    {
      items.map(
        (item) => {
          return (
            <li key={item.id}>
              <Card style={{ width: '18rem' }}>
              <Card.Img variant="top" src={item.image} />
              <Card.Body>
                <Card.Title>{item.title}</Card.Title>
                <Card.Text>{item.description}</Card.Text>
                <Button variant="primary">Go somewhere</Button>
              </Card.Body>
              </Card>
            </li>
          );
      }
      )
    }
  </ul>
  )    
}
  
export default FoodTruckCard;