import datetime


def read_master_date():
    product_list = []
    with open("../master_data/product_master.csv", "r") as f:
        products = f.readlines()[1:]
        for product in products:
            product_list.append(product.split(",")[0])
    return product_list


def get_product_price(product_id):
    product_price = 0
    with open("../master_data/product_master.csv", "r") as f:
        products = f.readlines()[1:]
        for proudct in products:
            product_list = proudct.split(",")
            if product_id in product_list:
                product_price = product_list[2]
                break
    return product_price



def validate_product_id(order_id, products):
    if order_id in products:
         return True
    return False


def validate_order_date(date):
    order_date = datetime.datetime.strptime(date,"%Y-%m-%d").date()
    today_date = datetime.date.today()
    diff = (today_date - order_date).days
    if diff >= 0:
        return True    
    return False


def validate_city(city):
    if city in ['Mumbai', 'Bangalore']:
        return True
    return False


def validate_emptiness(orders):
    empty_cols = []
    for k, v in orders.items():
        if not orders[k] or orders[k] == '':
            empty_cols.append(k)
    return empty_cols


def validate_sales(orders):
    order_quatity = int(orders["quatity"])
    order_sales = int(orders["sales"])
    product_price = int(get_product_price(orders["product_id"]))
    return (order_quatity * product_price) == order_sales


# with open("../master_data/product_master.csv", "r") as f:
#         print("hello")
#         products = f.readlines()[1:]
#         print(products)
#         for product in products:
#            print(product.split(","))