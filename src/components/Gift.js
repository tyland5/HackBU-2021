import React from 'react';

const Gift = ({ gift }) => {
  return (
    <div className='gift'>
      <img src={gift.image} />
      <h2>{gift.name}</h2>
      <p>{gift.price}</p>
    </div>
  );
};

export default Gift;
