# email_id=[
#           "sam@gamil.com",
#           "jhon@gamil.com",
#           "smith@gamil.com",
#           "james@gamil.com",
#           "stuart@gamil.com",
#           ]

# f=open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\emails.txt","w")
# for emial in email_id:
#     f.write(emial+"\n")

email_id = [
    "sam@gamil.com",
    "jhon@gamil.com",
    "smith@gamil.com",
    "james@gamil.com",
    "uart@gamil.com"
]
email_str = "\n".join(email_id)
with open("C:\\Users\\Ashok\\OneDrive\\Desktop\\PythonJuneWorks\\fileprograms\\emails.txt", "w") as f:
    f.write(email_str)
