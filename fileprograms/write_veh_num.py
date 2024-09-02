vehicle_numbers=[
    "kl1",
    "kl2",
    "kl13",
    "kl14",
    "kl15",
    "kl5",
]

f=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\veh_num.txt","w")
for num in vehicle_numbers:
    f.write(num+"\n")