employee={"name":"hari","dept":"r&d","salary":50000,"combo_offer":1000,"extra_working_day":3}

# print all key values

# for k,v in employee.items():
#     print(k,v)
    
#chk extra_working_days present

if("extra_working_day" in employee):
    salary=employee.get("salary")+employee.get("extra_working_day")*employee.get("combo_offer")
    print(f"the salary is {salary}")
    
else:
    salary=employee.get("salary")
    print(salary)