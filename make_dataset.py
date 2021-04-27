import cv2
import torch
import numpy as np 
import os
import shutil

# name = "00000.png"
# rgb_name = "./image/" + name
# depth_name = "./image/depth/" + name


# rgb_image = cv2.imread(rgb_name)
# depth_image = cv2.imread(depth_name, cv2.IMREAD_ANYDEPTH)

def file2dir(src_file, dst_file):
    shutil.copyfile(src_file,dst_file)

def movefiles(parent_dir, child_dir):
    dir_ = parent_dir + "/" + child_dir +"/"
    new_dir = parent_dir + "/" + "image/"
    image_list = os.listdir(dir_)
    for i in range(len(image_list)):
        src_file = dir_ + image_list[i]
        dst_file = new_dir + child_dir + "_" + image_list[i]
        file2dir(src_file, dst_file)
        print(dst_file)
    print("done!")

# parent_dir = "F:/Research/Motion_Estimate/DataSet/VKITTI/flowgt"
# child_dir = "0020"
# movefiles(parent_dir, child_dir)

def gemerate_haze(rgb, depth, k, beta):
    # haze_k = k + 0.3 * np.random.rand() # 0.3
    haze_k = k + 0.3 # 0.3
    haze_beta = beta  #0.0001

    transmitmap = np.expand_dims(np.exp(-1 * haze_beta * depth), axis=2)

    tx = np.concatenate([transmitmap, transmitmap, transmitmap], axis=2)
    txcvt = (tx * 255).astype('uint8')
    
    # guided filter smooth the transmit map
    tx_filtered = cv2.ximgproc.guidedFilter(guide=rgb, src=txcvt, radius=0, eps=1e-3, dDepth=-1)

    fog_image = (rgb / 255) * tx_filtered/255 + haze_k * (1 - tx_filtered/255)
    # fog_image = (rgb / 255) + haze_k
    fog_image = np.clip(fog_image, 0, 1)
    # print(fog_image*255)
    fog_image = (fog_image * 255).astype('uint8')
    return fog_image



rgb_dir = "F:/Research/Motion_Estimate/DataSet/VKITTI/rgb/image"
depth_dir = "F:/Research/Motion_Estimate/DataSet/VKITTI/depth/image"
fog_dir = "F:/Research/Motion_Estimate/DataSet/VKITTI/fog/image"
k = 0.5  #atmospheric
beta = 0.0002   #attenuation factor

image_list = os.listdir(rgb_dir)
for i in range(len(image_list)):
    rgb_name = rgb_dir + "/" + image_list[i]
    depth_name = depth_dir +  "/" + image_list[i]

    rgb_image = cv2.imread(rgb_name)
    depth_image = cv2.imread(depth_name, cv2.IMREAD_ANYDEPTH)

    fog = gemerate_haze(rgb_image, depth_image, k, beta)
    cv2.waitKey(10)
    cv2.imwrite(fog_dir + "/" + image_list[i], fog)
    
    print(image_list[i])
print("done!")



# cv2.imshow("rgb", rgb_image)
# cv2.imshow("fog", fog)
# cv2.waitKey(0)
# cv2.imwrite("fog"+"_" + str(k)+"_"+str(beta) + ".png", fog)