from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
for product in products:
    product['tags'] = set(product['tags'])



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommend_products=[]
    for product in products:
        matches = count_matches(product['tags'], customer_tags)
        recommend_products.append({'name': product['name'], 'matches': matches})
    recommend_products.sort(key=lambda x: x['matches'], reverse=True)
    return recommend_products



# TODO: Step 7 - Call your function and print the results

results = recommend_products(products, customer_preferences)

print("Recommended Products:")
for result in results:
    print(f"{result['name']}: {result['matches']} matches")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#I used loops to get an input, either to get the preference or to know if the user wants to put another preference. I also used loops to change the product tags from a list to a set. I used intersection to match the product tag with the customer preferences. I used loops to append the product name and the number of matches into a new dictionary. If loops were not used it would probably be a code way more lines that it is right now.
# 2. How might this code change if you had 1000+ products?
# I believe that this work would also work if I had more than 1000 products, maybe use other data structures, but I think this code would only take longer to run. Maybe with another data structure it would be more optmized and better to run a 1000+ products
