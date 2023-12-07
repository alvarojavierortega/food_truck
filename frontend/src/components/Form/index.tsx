import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import styles from './Form.module.scss';

export default function FoodTruckForm() {

    return (
      <Form>
        <fieldset>

          <Form.Group className="mb-3" >
            <Form.Label htmlFor="LatitudeSelect" className={styles.formLabel}>Latitude options</Form.Label>
            <Form.Select id="LatitudeSelect">
              <option>option 1</option>
            </Form.Select>
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label htmlFor="LongitudeSelect" className={styles.formLabel}>Longitude options</Form.Label>
            <Form.Select id="LongitudeSelect">
              <option>option 1</option>
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
  