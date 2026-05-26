import csv
import datetime
import collections
import os

script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, 'sales_data.csv')


def total_revenue():
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        total = 0
        for row in reader:
            total += int(row["amount"]) * int(row["quantity"])
    return total

def sales_by_category():
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        category_sales = collections.defaultdict(int)
        for row in reader:
            category_sales[row["category"]] += int(row["quantity"])
    return category_sales  

def top_products(n):
    with open(csv_path, newline = '', encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        product_sales = collections.Counter()
        for row in reader:
            product_sales[row["product"]] += int(row["quantity"])
        return product_sales.most_common(n)
    
def sales_by_month():
    with open(csv_path, newline = '', encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        month_sales = collections.defaultdict(int)
        for row in reader:
            date = datetime.datetime.strptime(row["date"], "%Y-%m-%d")
            month = date.strftime("%Y-%m")
            month_sales[month] += int(row["quantity"])
    return month_sales

def max_sale_date():
    with open(csv_path, newline = '', encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        max_date = None
        max_quantity = 0
        for row in reader:
            date = datetime.datetime.strptime(row["date"], "%Y-%m-%d")
            quantity = int(row["quantity"])
            if quantity > max_quantity:
                max_quantity = quantity
                max_date = date
    return max_date.strftime("%d.%m.%Y")

def lowest_selling_category():
    with open(csv_path, newline = '', encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        category_sales = collections.defaultdict(int)
        for row in reader:
            category_sales[row["category"]] += int(row["quantity"])
    return min(category_sales, key=category_sales.get)

def save_report():
    lines = []
    lines.append("============================")
    lines.append("ОТЧЁТ ПО ПРОДАЖАМ")
    lines.append("============================")
    lines.append(f"Всего выручки: {total_revenue()} руб.")
    lines.append("Продажи по категориям:")
    for category, quantity in sales_by_category().items():
        lines.append(f"  {category}: {quantity} шт.")
    lines.append("Топ самых продаваемых товаров:")
    n = int(input("Введите количество самых продаваемых товаров для записи в отчёт: "))
    for product, quantity in top_products(n):
        lines.append(f"  {product}: {quantity} шт.")
    lines.append("Продажи по месяцам:")
    for month, quantity in sales_by_month().items():
        lines.append(f"  {month} : {quantity} шт.")
    lines.append(f"Дата самой большой продажи: {max_sale_date()}")
    lines.append(f"Категория с самыми низкими продажами: {lowest_selling_category()}")
    with open("sales_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    print("Всего выручки: ", total_revenue())
    for category, quantity in sales_by_category().items():
        print(f"  {category}: {quantity} шт.")
    n = int(input("Введите количество самых продаваемых товаров для отображения: "))
    print(f"Топ {n} самых продаваемых товаров:")
    for product, quantity in top_products(n):
        print(f" {product}: {quantity} шт.")
    print("Продажи по месяцам:")
    for month, quantity in sales_by_month().items():
        print(f" {month} : {quantity} шт.")
    print("Дата самой большой продажи:")
    print(max_sale_date())
    print("Категория с самыми низкими продажами:")
    print(lowest_selling_category())
    save_report()