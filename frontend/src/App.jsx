import { useEffect, useState } from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import { AnimatePresence } from 'framer-motion';
import axios from 'axios';
import Login from './components/Login';
import AboutUs from './pages/AboutUs';
import NotFound from './pages/404';

const AnimatedRoutes = () => {
  const location = useLocation()
  return (
    <AnimatePresence mode='wait'>
      <Routes location={location} key={location.pathname}>
        <Route path='/login' element={<Login />}/>
        <Route path='/about' element={<AboutUs />}/>
        <Route path='/' element={<Home />}/>
        <Route path='*' element={<NotFound />}/>
      </Routes>
    </AnimatePresence>
  )
};

function Home() {
  const [data, setData] = useState([])
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        setError("Error al conectarse al backend" + error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Cargando...</div>;
    
  }
  if (error) {
    return <div>Error: {error}</div>;
  }
  return (
    <div>
      <h1>Datos de usuarios desde django</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{JSON.stringify(item)}</li>
        ))}
       
      </ul>
    </div>
  )
}


//To do 
//1. Crear el componente 'Home'
function App() {
  return (
    <Router>
      <Navbar />
      <div className='container mt-4'>
        <div className='row'>
          <div className='col'>
            <AnimatedRoutes />
          </div>
        </div>
      </div>
    </Router>
  )
}

export default App