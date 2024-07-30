import requests

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.status = 'Pending'

    def process_order(self):
        # Code to process the order (e.g., update status, deduct inventory)
        self.status = 'Processed'
        Inventory.deduct_inventory(self.product, self.quantity)

class Inventory:
    inventory = {
        'Product A': 100,
        'Product B': 150,
        'Product C': 200
    }

    @classmethod
    def deduct_inventory(cls, product, quantity):
        if product in cls.inventory and cls.inventory[product] >= quantity:
            cls.inventory[product] -= quantity
            print(f'Deducted {quantity} units of {product} from inventory.')
        else:
            print(f'Insufficient inventory for {product}. Order cannot be processed.')

    @classmethod
    def add_inventory(cls, product, quantity):
        if product in cls.inventory:
            cls.inventory[product] += quantity
        else:
            cls.inventory[product] = quantity
        print(f'Added {quantity} units of {product} to inventory.')

def login_to_admin():
    url = "https://gx.189.cn/admin/login.html"
    user="admin"
    passwd="admin@123"
    try:
        # 这里可以模拟登录或访问页面的GET请求
        response = requests.get(url)
        
        if response.status_code == 200:
            print("Successfully accessed the admin login page.")
        else:
            print(f"Failed to access the admin login page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while trying to access the URL: {e}")

# 示例用法
if __name__ == "__main__":
    login_to_admin()  # 调用登录函数
    order1 = Order('ORD001', 'Product A', 20)
    order1.process_order()

    Inventory.add_inventory('Product B', 50)
