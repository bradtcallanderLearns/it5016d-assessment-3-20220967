# 01 Exercise - Sunglass Shop: Map and Filter

## Brief

The Sunglass eCommerce site is starting to come together. There are a few features that should be complete to make the store more robust and complete some of the user features.

The first problem is that each of the products is displayed by manually reading an index from an array. What happens if you add a new product? This problem needs to be fixed by writing more flexible JavaScript, that can handle a product array of any length.

Also, the _Filter By_ dropdown and the _Sort by_ dropdown is not working.

![exercise](docs/exercise.png)

## Rationale

- Using `filter` and `map` are powerful and handy functions to use with arrays.
- Learning how to sort an array can be used for many different interactive purposes.

## Getting Started

1. Open the project in VS Code, and open your terminal
2. Type: `npm install` and then `npm start`. The React Application should open in your browser
3. Open `src/App.jsx` in VS Code.

## Instructions Part A - Use `map` to display the list of products

1. Watch the following video to understand how to use `map` with React Components: [Using Map in react (6 mins)](https://www.loom.com/share/d1da8d90491347fbab400113327160c9)
2. Open `src/components/Products.jsx` in VS Code
3. Replace the big list of `<Product />` components with a single `.map` function.
4. Don't forget to add a `key` property to the `<Product />` component. You can use the `product.id` as its value:

   ```jsx
   <Product key={product.id} ... />
   ```

### Acceptance criteria

- The map function is used to display the product list
- If a new product is added to the `products` array, it will automatically display on the webpage

## Instructions Part B - Implement the `filterBy` dropdown

The Sunglass Shop has all the event handlers, and React state preconfigured.

You need to update the function in `./src/utils/filterByCategory.js`. Return an array that only contains the products whose category matches the `filterBy` parameter.

For example, if `filterBy` is `"sunglasses"`, only products whose `meta.category` is equal to `"sunglasses"` should be included in the array.

To accomplish this task, use the [`.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) method, to return an array that only contains products with a category that is equal to the `filterBy` parameter.

1.  In the `filterByCategory.js` file, replace `return []` with `return products.filter()`
2.  Complete your filter function, by adding a callback as the first parameter.
3.  Ensure the callback returns `true` or `false`. It should check if the `filterBy` parameter is equal to the category of the product. Find the product category at `product.metadata.category`.
4.  Lastly, if `filterBy` is set to `"all"`, then `filterByCategory` should return an array that contains all of the products.

Watch the following code along video to see the answer:

### Acceptance criteria

- If the `filterBy` parameter is `"all"`, it should return an array with all of the products
- If the `filterBy` parameter is `"sunglasses"`, it should return an array that only contains products from the sunglasses category
- If the `filterBy` parameter is `"accessories"`, it should return an array that only contains products from the sunglasses category

## Instructions Part C - Sort Products

For this part, feel free to start with the code-along video at the bottom of this file.

Update the function in `./src/utils/sortProducts.js` so it returns an array with products in the correct order.

Find the price at the following location on the product object: `.prices[0].unit_amount`

### Acceptance criteria

- If `sortBy` is equal to `"high"`, the highest-priced item must be the first in the array, followed by the second highest-priced item etc
- If `sortBy` is equal to `"low"`, the lowest priced item must be the first in the array
- If `sortBy` is equal to `"latest"`, the product with the highest `created` value must be the first item in the array
