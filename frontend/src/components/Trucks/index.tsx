import { CardItem } from "types/cardItem";
import FoodTruckCard from "./Card";
import styles from './Trucks.module.scss';

export default function Trucks() {
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
    },
    {
      id:3,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    },
    {
      id:4,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    },
    {
      id:5,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    },
    {
      id:6,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    },
    {
      id:7,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    },
    {
      id:8,
      title:'my title',
      description: 'some description',
      image: 'assets/food_truck1.png'
    }
  ]

  return (
    <section className={styles.trucks}>
      <FoodTruckCard  items={items}/>
    </section>
  );
}