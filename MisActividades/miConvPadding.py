#Ahora con padding

import numpy as np
import cv2
import matplotlib.pyplot as plt


def miConv(img, kernel):
    h_img, w_img = img.shape #Alto y Ancho de la Imágen
    h_ker, w_ker = kernel.shape #Alto y Ancho del Kernel
    
    res = np.ones((h_img-h_ker+1,w_img-w_ker+1)) #Se crea una matriz de salida
    
    #Dentro de la iteración con "i" y "j", se va seleccionado cada elemento de la matriz de salida
    for i in range(h_img - h_ker + 1):
        for j in range(w_img - w_ker + 1):
            sumador = 0
            #Dentro de la iteración "x" y "y" se aplica la operación donde te da la suma del producto de matrices
            for x in range(h_ker):
                for y in range(w_ker):
                    sumador += img[i+x, j+y]*kernel[h_ker-1-x, w_ker-1-y]
            res[i, j] = sumador
            
    plt.imshow(res, cmap='gray')
    plt.title("Output Image Using Kernel")
    plt.show() #Muestra graficada la matriz de salida en escala de grises
    
    #padding en las orillas de acuerdo al tamaño del kernel
    padh= int((h_ker-1)/2)
    padw= int((w_ker-1)/2)
    pad_img=np.ones((h_img + (2*padh),w_img + (2*padw))) #Matriz de salida considerando el tamaño del padding en su alto y ancho
    pad_img[padh:pad_img.shape[0] - padh, padw:pad_img.shape[1] - padw] = img #Se le inserta a la matriz con padding, los valores  matriz de la imagen original 
    plt.imshow(pad_img, cmap='gray')
    plt.title("Padded Image")
    plt.show()#Muestra grafica de la matriz con padding en escala de grises
        
    return res
    
    
    
k = np.array([[-1, -1, -1],
              [-1, 8, -1],
              [-1, -1, -1]])


#Edge detection horizontal
k2 = np.array([[-1, 0, -1],
              [-1, 0, -1],
              [-1, 0, -1]])


ruta = r"C:\Users\arace\Desktop\Araceli Escuela\TEC\SEMESTRE 4\SemanaTEC\Laboratorio\semena-tec-tools-vision\Images\canicas.png"
image = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
output_image = miConv(image, k)

ruta2 = r"C:\Users\arace\Desktop\Araceli Escuela\TEC\SEMESTRE 4\SemanaTEC\Laboratorio\semena-tec-tools-vision\Images\sanCarlos.jpg"
image2 = cv2.imread(ruta2, cv2.IMREAD_GRAYSCALE)
output_image2 = miConv(image2, k2)

