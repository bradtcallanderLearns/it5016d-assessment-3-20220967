const Product = ({ image, name, description, price }) => {
  const onClick = () => {
    alert(`Checkout: ${name}`);
  };

  return (
    <li className="product-grid-item">
      <img src={image} alt={name} />
      <h3>{name}</h3>
      <p>{description}</p>
      <button onClick={onClick}>Buy now for NZ{price}</button>
    </li>
  );
};

export default Product;
