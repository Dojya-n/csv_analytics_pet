import csv
import datetime
import collections
import os

script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, 'sales_data.csv')

csvfile = open(csv_path, newline='', encoding='utf-8')
reader = csv.DictReader(csvfile)

def total_sales():
    sum = 0
    for row in reader:
        quantity = int(row["quantity"])
        sum += quantity
    return sum

def sales_by_category():
    category_sales = collections.defaultdict(int)
    for row in reader:
        category = row["category"]
        quantity = int(row["quantity"])
        category_sales[category] += quantity
    return category_sales

# def top_products():
# def sales_by_month():
# def max_sale_date():
# def lowest_selling_category():
if __name__ == "__main__":
    print("Количество проданных товаров: ", total_sales())
    print("Продажи по категориям: ", sales_by_category())