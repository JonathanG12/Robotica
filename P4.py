from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array

largo, alto = 250, 250
file = './Pez.png'

img = load_img(file, target_size = (largo ,alto)
               ,color_mode = "grayscale")

print(img.size)
print(img.mode)

imagen_en_array = img_to_array(img)
print(imagen_en_array.shape)

archivo = open("./Pez.csv", "w")
for i in imagen_en_array:
    for j in i:
        archivo.write(str(j[0]) + ",")
    archivo.write("\n")
archivo.flush()
archivo.close()