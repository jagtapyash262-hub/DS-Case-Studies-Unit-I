
# Case Study: E-commerce Product Sorting Using Divide and Conquer Strategy

## 1. Introduction

E-commerce websites contain a large number of products with different prices, ratings, and features. Customers often want to sort products according to price to find affordable products easily.

This case study explains how the Divide and Conquer strategy can be used to sort e-commerce products using the Merge Sort algorithm.

## 2. Problem Statement

To arrange a list of e-commerce products in ascending order of price using the Divide and Conquer approach.

## 3. Objectives

- To understand the Divide and Conquer strategy.
- To implement the Merge Sort algorithm using Python.
- To sort products according to their prices.
- To analyze the time and space complexity of the algorithm.

## 4. Strategy Used: Divide and Conquer

Divide and Conquer is an algorithm design technique that divides a large problem into smaller subproblems, solves them, and combines their results.

It involves three steps:

1. **Divide:** Split the product list into two halves.
2. **Conquer:** Sort each half recursively.
3. **Combine:** Merge both sorted halves into one sorted list.

## 5. Algorithm Used: Merge Sort

Merge Sort is a sorting algorithm based on the Divide and Conquer strategy.

In this case study, the products are divided into smaller lists, sorted by price, and merged to produce the final sorted list.

## 6. Example

### Input

| Product | Price |
|---|---:|
| Headphones | Rs. 1500 |
| Keyboard | Rs. 800 |
| Mouse | Rs. 400 |
| Monitor | Rs. 7000 |
| Webcam | Rs. 1200 |

### Output

| Product | Price |
|---|---:|
| Mouse | Rs. 400 |
| Keyboard | Rs. 800 |
| Webcam | Rs. 1200 |
| Headphones | Rs. 1500 |
| Monitor | Rs. 7000 |

The products are arranged from lowest to highest price.

## 7. Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Auxiliary Space Complexity: O(n)

Here, n represents the number of products.

## 8. Advantages

- Efficient for sorting large product lists.
- Provides predictable time complexity.
- Can be adapted to sort products by different attributes.
- Maintains the relative order of products having equal prices.

## 9. Limitations

- Requires additional memory during merging.
- May have more overhead than simpler sorting algorithms for very small lists.
- A real e-commerce system may need additional filtering and pagination features.

## 10. Applications

- Sorting products by price on shopping websites.
- Sorting products by ratings or popularity.
- Organizing large product catalogues.
- Arranging records in ascending or descending order.

## 11. Conclusion

This case study demonstrates how the Divide and Conquer strategy solves the product sorting problem using Merge Sort.

The algorithm divides the product list into smaller parts, sorts them, and combines them into a final ordered list. It provides an efficient way to sort products and helps demonstrate an important concept in Data Structures and Algorithms.

## 12. Technologies Used

- Python
- Merge Sort
- Divide and Conquer Strategy

## 13. Files Included

- `ecommerce_sorting.py` – Python implementation of the algorithm.
- `output.txt` – Sample output of the program.
- `README.md` – Case study documentation.
