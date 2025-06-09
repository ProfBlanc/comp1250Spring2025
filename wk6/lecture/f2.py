def order_laptop(brand:str, ram:int, hdd:str, storage_capacity:int)->dict:
    config = dict()
    
    if not isinstance(brand, str) or not isinstance(ram, int) or not isinstance(hdd, str) or not isinstance(storage_capacity,int):
            return None
    
    
    if brand.lower() not in "dell,sony,ibm,hp,toshiba,acer,asus".split(","):
        return None  #
    elif ram < 8 or ram > 32:
        return None
    elif hdd not in "ssd,hd".split(","):
        return None
    elif storage_capacity < 256 or storage_capacity > 2048:
        return None

    config["brand"] = brand
    config["storage_capacity"] = storage_capacity
    config["hdd"] = hdd
    config["ram"] = ram

    return config
    
    
# laptop = order_laptop("hp", 16, "ssd", 1000)
laptop = order_laptop(hdd="ssd", storage_capacity=1000, brand="ibm", ram=32)
print(laptop)
