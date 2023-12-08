import { CardItem } from "types/cardItem";
import FoodTruckCard from "./Card";
import styles from './Trucks.module.scss';

type CardItems={
  items: CardItem[]
}

export default function Trucks({items}: CardItems) {

  return (
    <section className={styles.trucks}>
      <FoodTruckCard  items={items}/>
    </section>
  );
}