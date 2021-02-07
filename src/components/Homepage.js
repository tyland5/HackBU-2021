import React, { useState } from 'react';
import './Homepage.css';
import Gift from './Gift';
import data from '../web-scrape/products.json';

const Homepage = () => {
  const [gift, setGifts] = useState({});

  const handleClick = () => {
    setGifts(data);
  };

  return (
    <div className='homepage-container'>
      <div className='homepage'>
        <h1>Find the perfect gift.</h1>
        <div className='search' onClick={handleClick}>
          <p>Generate new idea {`>>`}</p>
        </div>
      </div>
      <Gift gift={gift} />
    </div>
  );
};

export default Homepage;
