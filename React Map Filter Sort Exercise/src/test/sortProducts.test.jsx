import sortProducts from "../utils/sortProducts";

const products = [
  {
    id: 1,
    created: 1,
    prices: [
      {
        unit_amount: 100,
      },
    ],
  },
  {
    id: 2,
    created: 2,
    prices: [
      {
        unit_amount: 90,
      },
    ],
  },
  {
    id: 3,
    created: 3,
    prices: [
      {
        unit_amount: 120,
      },
    ],
  },
  {
    id: 4,
    created: 4,
    prices: [
      {
        unit_amount: 50,
      },
    ],
  },
];

describe("sortProducts", () => {
  it("should sort products from highest to lowest", () => {
    const sortBy = "high";
    const result = sortProducts([...products], sortBy);
    expect(result).toEqual([
      products[2],
      products[0],
      products[1],
      products[3],
    ]);
  });

  it("should sort products from lowest to highest ", () => {
    const sortBy = "low";
    const result = sortProducts([...products], sortBy);
    expect(result).toEqual([
      products[3],
      products[1],
      products[0],
      products[2],
    ]);
  });

  it("should sort products from latest created date", () => {
    const sortBy = "latest";
    const result = sortProducts([...products], sortBy);
    expect(result).toEqual([
      products[3],
      products[2],
      products[1],
      products[0],
    ]);
  });
});
