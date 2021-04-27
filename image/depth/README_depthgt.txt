Virtual KITTI 1.3.1
===================

http://www.xrce.xerox.com/Research-Development/Computer-Vision/Proxy-Virtual-Worlds

COPYRIGHT
Copyrights in The Virtual KITTI Dataset are owned by Xerox.

PLEASE READ THESE TERMS CAREFULLY BEFORE DOWNLOADING THE VIRTUAL KITTI DATASET. DOWNLOADING OR USING THE DATASET MEANS YOU ACCEPT THESE TERMS.
The Virtual KITTI Dataset is provided by Xerox and may be used for non-commercial purposes only and is subject to the Creative Commons Attribution-NonCommercial-ShareAlike 3.0.

ATTRIBUTION
The Virtual KITTI Dataset is an Adaptation of the KITTI Vision Benchmark Suite. See also the publication by Andreas Geiger and Philip Lenz and Raquel Urtasun, entitled "Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite", in Computer Vision and Pattern Recognition (CVPR), 2012.

CITATION
When using or referring to this dataset in your research, please cite Xerox as the originator of the Virtual KITTI Dataset and cite our CVPR 2016 paper (reference below).

Virtual Worlds as Proxy for Multi-Object Tracking Analysis
Adrien Gaidon, Qiao Wang, Yohann Cabon, Eleonora Vig
In IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016


Depth Ground Truth
-----------------------------------------------------------------

Link: http://download.xrce.xerox.com/virtual-kitti-1.3.1/vkitti_1.3.1_depthgt.tar

The depth ground truth for each video is stored in 16-bit grayscale PNG images as:

    vkitti_<version>_depthgt/<world>/<variation>/%05d.png

Depth values are distances to the camera plane obtained from the z-buffer (https://en.wikipedia.org/wiki/Z-buffering). They correspond to the z coordinate of each pixel in camera coordinate space (not the distance to the camera optical center). We use a fixed far plane of 655.35 meters, i.e. points at infinity like sky pixels are clipped to a depth of 655.3m. This allows us to truncate and normalize the z values to the [0;2^16 - 1] integer range such that a pixel intensity of 1 in our single channel PNG16 depth images corresponds to a distance of 1cm to the camera plane. The depth map in centimeters can be directly loaded in Python with numpy and OpenCV via the one-liner (assuming “import cv2”):

    depth = cv2.imread(depth_png_filename, cv2.IMREAD_ANYDEPTH)
