import os
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

#Setting up a data augmentation configuration via ImagedataGenerator
datagen = ImageDataGenerator(
rotation_range=40,
width_shift_range=0.2,
height_shift_range=0.2,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
fill_mode='nearest')

base_dir = 'C:/Users/ravi_shukla/Desktop/dogs-vs-cats_small/'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')
train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')
validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')
test_cats_dir = os.path.join(test_dir, 'cats')
test_dogs_dir = os.path.join(test_dir, 'dogs')

#list of all cat training image paths
fnames = [os.path.join(train_cats_dir, fname) for fname in os.listdir(train_cats_dir)]

#Select an image to augment/modify
img_path = fnames[25]

#reads the image and resizes it
img = image.load_img(img_path, target_size=(150, 150))

#Converts to Numpy array with shape (150,150,3)
x = image.img_to_array(img)

#Reshapes it to (1, 150, 150, 3)
x = x.reshape((1,) + x.shape)

import matplotlib.pyplot as plt
#Generates batches of randomly transformed images. Loops indefinitely,so you need to break the loop at some point!
i = 0
for batch in datagen.flow(x, batch_size=1):
    plt.figure(i)
    imgplot = plt.imshow(image.array_to_img(batch[0]))
    i += 1
    if i % 4 == 0:
        break
    
    plt.show()
    
