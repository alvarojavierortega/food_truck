  import styles from './Pages.module.scss';
  import error404 from '../assets/error_404.png'
  import { useNavigate } from 'react-router-dom';
  import Button from 'react-bootstrap/Button';
  
  export default function NotFound() {
      const navigate = useNavigate();
  
      return (
          <>
            <div className={styles.container}>
                <span className={styles.text404}>404</span>

                <h1 className={styles.title}>
                    Ops! Page not found.
                </h1>

                
                <Button 
                  variant="success" 
                  size="lg" 
                  className={styles.backButton}
                  onClick={() => navigate(-1)}
                  >Back
                </Button>{' '}

                <img
                    className={styles.dogImage}
                    src={error404}
                    alt="A dog with glasses"
                />
            </div>
            <div className={styles.blankSpace}></div>
        </>
  
      )
  }