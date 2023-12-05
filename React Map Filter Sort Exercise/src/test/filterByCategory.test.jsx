import filterByCategory from "../utils/filterByCategory";

const products = [
  {
    id: 1,
    metadata: {
      category: "sunglasses",
    },
  },
  {
    id: 2,
    metadata: {
      category: "sunglasses",
    },
  },
  {
    id: 3,
    metadata: {
      category: "accessories",
    },
  },
  {
    id: 4,
    metadata: {
      category: "accessories",
    },
  },
];

describe("filterByCategory", () => {
  it('should return all the products if filterBy is "all"', () => {
    const filterBy = "all";
    const result = filterByCategory(products, filterBy);
    expect(result).toEqual(products);
  });

  it('should ONLY return sunglasses filterBy is "sunglasses"', () => {
    const filterBy = "sunglasses";
    const result = filterByCategory(products, filterBy);
    expect(result).toEqual([products[0], products[1]]);
  });

  it('should ONLY return accessories filterBy is "accessories"', () => {
    const filterBy = "accessories";
    const result = filterByCategory(products, filterBy);
    expect(result).toEqual([products[2], products[3]]);
  });
});
