import os
from PIL import Image

img_dir = r"/home/beto/Downloads/crops (fanta-laranja-lata) (copia)"
for filename in os.listdir(img_dir):
    try :
        with Image.open(img_dir + "/" + filename) as im:
             print('ok')
    except :
        print(img_dir + "/" + filename)
        os.remove(img_dir + "/" + filename)