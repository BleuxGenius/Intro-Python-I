# class Products: 
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#         def __str__(self):
#             return f"{self.name} costs ${self.price}"





# class Department: 
#     def __init__(self,name, products):
#         self.name = name
#         self.products = []

#     def __str__(self):
#         return f"No products available in the {self.name} department yet."




# class Store:
#     def __init__(self, name, lat, lon, departments):
#         self.name = name
#         self.location = LatLon(lat,lon)
#         self.departments = [Departments(d) for d in departments]
#         self.departments = departments # strings


#     def __str__(self):
#         return f"Store {self.name}, {self.location}, {self.departments}"  

# store = Store("LambdaStore", 44.13455, -121.123124, ["Clothing, Cookware, Books"])

# # print store


# # we want to add departments 
# # lets

# while True:
#     selection = input("Select the number of a department type 'exit' to leave ")

# if selection == "exit":
#     print("Thanks for shopping with us!")
#     break


# # add error handleing so that when a user inpits a department for a non-existent 
# # department, we'll notify them that department doesn't exist 
# try: 
#     # casting might cause an error
#     selection = int(selection)
#     if (selection >= len(store.departments):
#         print("thats not a valid department)
#     elif selection >: 0 and selection < len(store.departments):
#         print("The user selectted" + store.departments[selection])
#     else: 
#         print("Department numbers are to positive")
#         # the user didn't give us a value tht could be cast to a number 
#         # lets let 
#     except ValueError:
#         print("Please enter your choice ")