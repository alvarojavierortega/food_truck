import Banner from './components/Banner';
import FoodTruckPage from './pages/FoodTruckPage';
import NotFound from './pages/NotFound';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


export default function AppRouter() {
  return (
   
      <Router>
        <Banner />
        <main className='container'>
        <Routes>
           <Route path='/' element={<FoodTruckPage />} />
          <Route path='*' element={<NotFound />} />
        </Routes>      
        </main>  
      </Router>
   
  );
}