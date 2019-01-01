products = {"풀" : 800, "색종이": 1000}

for product_detail in products.items():
    print("{}의 가격: {}원".format( *product_detail))


for product_detail in products.items():
    print("{}의 가격: {}원".format( product_detail[0], product_detail[1]))
