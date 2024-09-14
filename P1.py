from tensorflow.keras.utils import load_img

largo, alto = 200, 200
file = '../Pez.png'

img = load_img(file, target_size = (largo ,alto)
               ,color_mode = "grayscale")

print(img.size)
print(img.mode)

img.show()