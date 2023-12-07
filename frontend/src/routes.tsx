import Footer from './components/Footer';
import FoodTruckPage from './pages/FoodTruckPage';
import NotFound from './pages/NotFound';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


export default function AppRouter() {
  return (
    <main className='container'>
      <Router>
        <Routes>
           <Route path='/' element={<FoodTruckPage />} />
          <Route path='*' element={<NotFound />} />
        </Routes>
        <Footer />
      </Router>
    </main>
  );
}