import numpy as np
from PIL import Image

#First you need to open images with PIL
first_image = Image.open("C:/images_for_projects/first_dog.jpg")
second_image = Image.open("C:/images_for_projects/second_dog.jpg")
#Then create arrays of above images
first_image_array = np.array(first_image)
second_image_array = np.array(second_image)
#Arrange arrays of two images in single line row
arranged_image = np.hstack([first_image_array, second_image_array])
#Create final image
final_image = Image.fromarray(arranged_image)
#And provide the path with name for final image where you want to save it
final_image.save("C:/images_for_projects/final_proto.jpg")
print("Image saved !")