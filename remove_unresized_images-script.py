import os
import cv2
from PIL import Image

#add the complete path of images
img_dir = r"/home/beto/Downloads/crops(coca-garrafa)/"
for filename in os.listdir(img_dir):
    #img = cv2.imread(filename)
    img = Image.open(img_dir + "/" + filename)
    height = img.height
    width = img.width

    if (height != 100 and width != 100):
        os.remove(img_dir + "/" + filename)
    else:
        print('ok')
    '''
    try :
        with Image.open(img_dir + "/" + filename) as im:
             print('ok')
    except :
        print(img_dir + "/" + filename)
        os.remove(img_dir + "/" + filename)
    '''