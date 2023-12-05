import "./App.css";
import { useEffect, useState } from "react";
import { getProducts } from "./services/getProducts";
import FilterBy from "./components/FilterBy";
import SortBy from "./components/SortBy";
import Products from "./components/Products";

import filterByCategory from "./utils/filterByCategory";
import sortProducts from "./utils/sortProducts";

const App = () => {
  const [products] = useState(getProducts());
  const [filterBy, setFilterBy] = useState("all");
  const [sortBy, setSortBy] = useState("latest");
  const [filteredProducts, setFilteredProducts] = useState(getProducts());

  useEffect(() => {
    const filtered = filterByCategory(products, filterBy);
    const sorted = sortProducts(filtered, sortBy);
    setFilteredProducts([...sorted]);
  }, [filterBy, sortBy, products]);

  return (
    <div className="container">
      <h1>Sunglass Shop</h1>
      <div className="toolbar">
        <FilterBy setFilterBy={setFilterBy} />
        <SortBy setSortBy={setSortBy} />
      </div>
      <Products products={filteredProducts} />
    </div>
  );
};

export default App;
