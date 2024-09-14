from keras.utils import load_img, img_to_array

largo, alto = 500, 500
#file = './FIT V.jpg'
file = './Pez.png'

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

print(img.size)
print(img.mode)


imagen_en_array = img_to_array(img)  #filas, columnas, canales de colores
print(imagen_en_array.shape)

#print(imagen_en_array)

for i in imagen_en_array:
    for j in i:
        print(str(j[0]) + ",", end="")
    print()