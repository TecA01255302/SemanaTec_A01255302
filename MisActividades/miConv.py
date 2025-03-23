"""Mi Convulación por Araceli Ruiz Sánchez (A01255302)
Basándote en el ejemplo mostrado en clase, implementa tu propia versión de una convolución.
Tu función debe recibir 2 matrices: la imagen a modificar y el filtro, y debe devolver la matriz resultante de la operación.
Cuando tu programa esté funcionando, súbelo a tu repositorio de git (commit y push)
y pega el link de tu repo en canvas en la actividad de implementación de convolución individual.
Recuerda que tu código y commits deben de cumplir con todos lo estándares.
"""

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
            
    plt.imshow(res, cmap='gray') #Grafica la matriz de salida en escala de grises
    plt.title("Output Image Using Kernel")
    plt.show()#Muestra la gráfica
    return res


#Edge detection    
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
