import FoodTruckForm from '../components/Form';
import FoodTruckCard from '../components/Card';
import styles from './Pages.module.scss';
import { CardItem } from 'types/cardItem';



export default function FoodTruckPage() {
  const items: CardItem[] = [
    {
      id:1,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    },
    {
      id:2,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    }
  ]
  return (
    <>
      <main>
        <FoodTruckForm/>
        <section className={styles.foodTruckItems}>
          <FoodTruckCard items={items}/>
        </section>
      </main> 
    </>
  )
}


  