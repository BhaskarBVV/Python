import util
import csv
class Products:
    def get_all_products():
        products=util.utility.readfromweb("https://www.watchguard.com/wgrd-products/all-products-list",".prod-list a")


        all_products=[]
        for i in products:
            product_name=i.get_text()
            all_products.append(product_name)
        
        util.utility.write_in_file("products.csv",["Name of product"], all_products)
