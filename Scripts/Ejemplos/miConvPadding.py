#Ahora con padding

import numpy as np
import cv2
import matplotlib.pyplot as plt


def miConv(img, kernel):
    h_img, w_img = img.shape
    h_ker, w_ker = kernel.shape
    
    res = np.ones((h_img-h_ker+1,w_img-w_ker+1))
    
    for i in range(h_img - h_ker + 1):
        for j in range(w_img - w_ker + 1):
            sumador = 0
            for x in range(h_ker):
                for y in range(w_ker):
                    sumador += img[i+x, j+y]*kernel[h_ker-1-x, w_ker-1-y]
            res[i, j] = sumador
            
    plt.imshow(res, cmap='gray')
    plt.title("Output Image Using Kernel")
    plt.show()
    
    padh= int((h_ker-1)/2)
    padw= int((w_ker-1)/2)
    pad_img=np.ones((h_img + (2*padh),w_img + (2*padw)))
    pad_img[padh:pad_img.shape[0] - padh, padw:pad_img.shape[1] - padw] = img
    plt.imshow(pad_img, cmap='gray')
    plt.title("Padded Image")
    plt.show()
        
    return res
    
"""    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)
 
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
 
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image
 
    if verbose:
        plt.imshow(padded_image, cmap='gray')
        plt.title("Padded Image")
        plt.show()"""
#output_size = ((input_size — kernel_size + 2 * padding) / stride) + 1
    
    
k = np.array([[-1, -1, -1],
              [-1, 8, -1],
              [-1, -1, -1]])



ruta = r"C:\Users\arace\Desktop\Araceli Escuela\TEC\SEMESTRE 4\SemanaTEC\Laboratorio\semena-tec-tools-vision\Images\canicas.png"
image = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
output_image = miConv(image, k)

#miConv(image,k)
