# Notebook to Streamlit

Use the analysis logic from the Jupyter Notebook to build the Rosa's Pizza Streamlit app.

## Notebook Logic

- Reuse the functions and calculation logic developed in the notebook.
- Import `ZONES`, `TIME_BLOCKS`, `COSTS`, and `delivery_times` from `starter`.
- Do not recreate or modify the provided starter code.
- The cost per late order is:
  `refund + churn_orders * margin`.
- For each candidate promise:
  - simulate delivery times;
  - count the number of orders;
  - count orders with delivery time greater than the promise;
  - calculate profit from orders;
  - calculate total late-order cost;
  - calculate net profit as profit from orders minus late-order cost.
- Recommend the promise with the highest net profit.
- Use `seed=1` when calling `delivery_times` so results are reproducible.

## App Requirements

The Streamlit app should allow the user to:

- select a zone from a dropdown;
- select a time block from a dropdown;
- set the range of promised delivery times to try;
- adjust the profit margin per order;
- adjust estimated churn per late order;
- adjust refund cost per late order;
- click a button to display the recommended promised delivery time.

## Constraints

- Reuse the notebook logic rather than duplicating or replacing it with a different calculation method.
- Keep the app code simple and readable.
- Preserve the meaning of the calculations used in the notebook.
- Use the user-adjusted cost values when calculating the recommendation.