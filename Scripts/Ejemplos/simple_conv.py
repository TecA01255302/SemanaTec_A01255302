"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/

Modified by Benjamin Valdes
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
 
def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def convolution(image, kernel):
    """Aplica una convolucion sin padding (valida) de una dimesion 
    y devuelve la matriz resultante de la operación
    """

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = kernel.shape #asigna alto y ancho del filtro
   
    output = np.zeros(image.shape) #matriz donde guardo el resultado
   
    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)
             
    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    plt.show()
 
    return output

"""
k = np.array([[-1, -2, -1],
              [0, 0, 0],
              [1, 2, 1]])

img = np.array([ [10,20,30,40,50],
                 [15,25,35,45,55],
                 [20,30,40,50,60],
                 [25,35,45,55,65],
                 [30,40,50,60,70]
    ])"""

k = np.array([[1, 1, 1],
              [0, 1, 4],
              [3, 1, 2]])

img = np.array([ [0,0,0,0,0,0,0],
                 [0,2,4,1,5,4,0],
                 [0,5,1,3,3,6,0],
                 [0,6,4,4,7,3,0],
                 [0,8,7,3,7,0,0],
                 [0,6,8,6,8,4,0],
                 [0,0,0,0,0,0,0]
    ])

convolution(img,k)
