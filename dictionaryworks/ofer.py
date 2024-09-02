
mobile={"name":"motoedge","brand":"moto","price":22000,"is_available":True,"offer":500}

if "offer" in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")
    
    print(f"the offer price is {selling_price}")
else:
    selling_price=mobile.get("price")
    
    print(selling_price)