import requests
from PIL import Image

url = input("Enter the url of the image here : ")
file_name = input("Name of the image file (with extenstion): ")

try:
    data = requests.get(url).content

    f = open(file_name, "wb")
    f.write(data)
    f.close()

    img = Image.open(file_name)
    img.show()

except:
    print("Something went wrong, Please Try Again Later !")
