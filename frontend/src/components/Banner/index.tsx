// import { ReactComponent as Logo } from '../../assets/logo.svg';


// export default function Footer() {
//   return (
//     <footer >
//       <Logo />
//     </footer>
//   );
// }

import styles from './Banner.module.scss';


export default function Footer() {
  return (
    <div className={styles.banner} >
      <img src="assets/banner4.png" alt="" />
      <img src="assets/banner1.png" alt="" />
      <img src="assets/banner2.png" alt="" />
    </div>
  );
}