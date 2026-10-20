
# E-commerce-Product-Sorting

A Python case study demonstrating the Divide and Conquer algorithm design strategy using Merge Sort to sort e-commerce products by price.

# E-commerce Product Sorting Using Divide and Conquer

A Python case study demonstrating how the Divide and Conquer strategy can be used to arrange e-commerce products from lowest to highest price.

## Features

- Sort products from lowest to highest price.
- Display product names and prices before sorting.
- Display the sorted product list after sorting.
- Use Merge Sort to efficiently sort products.
- Demonstrate the Divide and Conquer strategy.

## Algorithm Used

**Merge Sort (Divide and Conquer)**

- **Divide:** Split the product list into two halves.
- **Conquer:** Recursively sort both halves.
- **Combine:** Merge the sorted halves into one sorted list.

## Requirements

- Python 3.7 or newer
- No external packages are required.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python ecommerce_sorting.py
   ```

## Sample Input

```text
Headphones: Rs. 1500
Keyboard: Rs. 800
Mouse: Rs. 400
Monitor: Rs. 7000
Webcam: Rs. 1200
```

## Sample Output

```text
Products After Sorting (Low to High):
Mouse: Rs. 400
Keyboard: Rs. 800
Webcam: Rs. 1200
Headphones: Rs. 1500
Monitor: Rs. 7000
```

## Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Auxiliary Space: O(n)

## Applications

- Sorting products on e-commerce websites.
- Arranging products by price or rating.
- Organizing large product lists.

## Conclusion

This case study demonstrates how Merge Sort applies the Divide and Conquer strategy to sort e-commerce products efficiently. It helps illustrate the practical use of algorithm design techniques in real-world applications.

## Files Included

- `ecommerce_sorting.py` – Python source code.
- `output.txt` – Program output.
- `README.md` – Case study documentation.
