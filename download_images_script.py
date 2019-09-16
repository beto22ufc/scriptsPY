from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"heineken garrafa","limit":100,"print_urls":False}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths) 