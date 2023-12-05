const filterByCategory = (products, filterBy) => {
  if (filterBy === "all") {
    return products;
  }
  return products.filter((product) => {
    return product.metadata.category === filterBy;
  });
};

export default filterByCategory;
