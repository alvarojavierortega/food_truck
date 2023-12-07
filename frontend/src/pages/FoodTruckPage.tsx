import FoodTruckForm from '../components/Form';
import Trucks from '../components/Trucks';
import styles from './Pages.module.scss'

export default function FoodTruckPage() {

  return (
    <>
      <h1 className={styles.title}> Find your amazing food banner </h1>
      <FoodTruckForm/>
      <Trucks/>
    </>
  )
}


  