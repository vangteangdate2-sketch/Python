print ("An e-commerce company stores order codes.")
orders = [ 
    "ORD-2026-001", 
    "ORD-2026-002", 
    "NEW-2025-003", 
    "OLD-2024-004", 
    "ORD-2026-005" 
] 

# extract the order prefix
order_prefixes = [order.split("-")[0] for order in orders]
print(order_prefixes)

# extract the year
order_years = [order.split("-")[1] for order in orders]
print(order_years)

# extract the order number
order_numbers = [order.split("-")[2] for order in orders]
print(order_numbers)

#replace "OLD" with "NEW"
updated_orders = [order.replace("OLD", "NEW") for order in orders]
print(updated_orders)

#Display the order codes that start with "ORD"
ord_orders = [order for order in orders if order.startswith("ORD")]
print(ord_orders)