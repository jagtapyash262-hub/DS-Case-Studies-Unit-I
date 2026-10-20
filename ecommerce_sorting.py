
def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2

    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    sorted_products = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["price"] <= right[j]["price"]:
            sorted_products.append(left[i])
            i += 1
        else:
            sorted_products.append(right[j])
            j += 1

    sorted_products.extend(left[i:])
    sorted_products.extend(right[j:])

    return sorted_products


products = [
    {"name": "Headphones", "price": 1500},
    {"name": "Keyboard", "price": 800},
    {"name": "Mouse", "price": 400},
    {"name": "Monitor", "price": 7000},
    {"name": "Webcam", "price": 1200}
]

print("E-COMMERCE PRODUCT SORTING")
print("\nProducts Before Sorting:")

for product in products:
    print(f'{product["name"]}: Rs. {product["price"]}')

sorted_products = merge_sort(products)

print("\nProducts After Sorting (Low to High):")

for product in sorted_products:
    print(f'{product["name"]}: Rs. {product["price"]}')
