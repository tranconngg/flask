import json
 
def read_json(path):
    with open(path,'r') as f:
        return json.load(f)
    
def load_categorys():
    return read_json(r"C:\Users\Admin\Desktop\DE\web\saleapp\sale\data\categorys.json")

def load_products():
    return read_json(r"C:\Users\Admin\Desktop\DE\web\saleapp\sale\data\products.json")