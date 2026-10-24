#An ECommerce website reecords the product ID's purchased by two customers.Find the products purchased by exactly one of the two customers without
#  using symmetric difference ?

customer1=set()
n=int(input("ENTER THE NO OF PRODUCT PARCHASED BY CUST1 :"))
for i in range(n):
    customer1.add(input("ENTER THE NAME OF PRODUCTS :"))
print("SET OF NAMES :",customer1)

customer2=set()
m=int(input("ENTER THE NO OF PRODUCT PARCHASED BY CUST2 :"))
for i in range(m):
    customer2.add(input("ENTER THE NAME OF PRODUCT :"))
print("SET OF NAMES :",customer2)

twocus=(customer1|customer2) - (customer1&customer2)
print("PRODUCT PURCHASED BY EXACTLY ONE OF TWO CUST :",twocus)