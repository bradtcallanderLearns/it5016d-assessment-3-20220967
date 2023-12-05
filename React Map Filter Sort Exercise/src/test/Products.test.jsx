import { render } from "@testing-library/react";
import Products from "../components/Products";
import products from "../data/products.json";

test("renders an extra Product when added to the array", () => {
  const product = {
    prices: [
      {
        unit_amount: 8500,
      },
    ],
    id: "prod_brand_new_id",
    created: 1606631666,
    description: "How dynamic is your product listing?",
    images: ["https://files.stripe.com/links/fl_test_HG5Y5oY5y2SlpQMclkQ0rjXm"],
    metadata: { category: "sunglasses" },
    name: "A NEW PRODUCT HAS BEEN ADDED",
  };
  const newProducts = [...products, product];
  const { asFragment } = render(<Products products={newProducts} />);
  expect(asFragment()).toMatchSnapshot();
});
