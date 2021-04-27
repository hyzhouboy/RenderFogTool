import cv2
import torch
import numpy as np 
import os


name = "0001_00003.png"
rgb_name = "./image/" + name
depth_name = "./image/depth/" + name


rgb_image = cv2.imread(rgb_name)
depth_image = cv2.imread(depth_name, cv2.IMREAD_ANYDEPTH)

def gemerate_haze(rgb, depth, k, beta):
    haze_k = k + 0.3
    haze_beta = beta  #0.0001

    transmitmap = np.expand_dims(np.exp(-1 * haze_beta * depth), axis=2)

    tx = np.concatenate([transmitmap, transmitmap, transmitmap], axis=2)
    txcvt = (tx * 255).astype('uint8')
    
    # guided filter smooth the transmit map
    tx_filtered = cv2.ximgproc.guidedFilter(guide=rgb, src=txcvt, radius=50, eps=1e-3, dDepth=-1)

    fog_image = (rgb / 255) * tx_filtered/255 + haze_k * (1 - tx_filtered/255)
    # fog_image = (rgb / 255) + haze_k
    fog_image = np.clip(fog_image, 0, 1)
    # print(fog_image*255)
    fog_image = (fog_image * 255).astype('uint8')
    return fog_image

k = 0.5  #atmospheric
beta = 0.00008   #attenuation factor
fog = gemerate_haze(rgb_image, depth_image, k, beta)
cv2.imshow("rgb", rgb_image)
cv2.imshow("fog", fog)
cv2.waitKey(0)
# cv2.imwrite("fog"+"_" + str(k)+"_"+str(beta) + ".png", fog)