import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { CardItem } from 'types/cardItem';
import { useState } from 'react';
import CardModal from '../Modal';


type CardItems={
  items: CardItem[]
}

const FoodTruckCard = ({items}: CardItems) => {
  const [show, setShow] = useState(false)
  const [modalBody, setModalBody] = useState("")
  const [modalTitle, setModalTitle] = useState("")  
  
  const handleShow = (item:CardItem) => {
    setShow(true)
    setModalTitle(item.title)
    setModalBody(JSON.stringify(item.modal, null, 4))
  };

  return  (
  <ul>
    {show && <CardModal 
          setShow={(value:boolean) => setShow(value)} 
          show={show}
          modalBody={modalBody}
          modalTitle={modalTitle}/>}
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
                <Button variant="primary" onClick={()=>handleShow(item)}>See details</Button>
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