#!usr/bin/env/python
# Program created by Uriel Garcilazo on August 24th 2021. Program consumes two images:
#  - photo for microscopy
#  - scalebar

from PIL import Image
import os
from os.path import join as jn

path = os.getcwd()
print(path)
pathImages = jn(path, "Photos")
pathSB = jn(path, "_SB_")
formats = ['.jpg','.JPG','.PNG','.png','.tiff','.TIFF']
magnsPath = [jn(pathSB, x) for x in os.listdir(pathSB) if x.endswith('.png')]
magns = [x.replace('.png','').split('_')[-1] for x in magnsPath]



# Extract a list with the different photos that will require scalebar
filesPhotos = []

for root, folders, files in os.walk(pathImages):
    # for file in files: print(file)
    [filesPhotos.append(jn(root,x)) for x in files]


# Add a watermark function
def add_SB (sbPath, photoPath):
    # open the image that will get scalebar inserted
    try:
        photo = Image.open(photoPath)
        widthPh, heightPh = photo.size
        # open the scalebar
        sbImg = Image.open(sbPath)
        widthSb, heighSb = sbImg.size
        magnitud = (round((1/5) * heighSb))
        photo.paste(sbImg, (widthPh-(widthSb + magnitud),
        heightPh-(heighSb + magnitud)))
        photo.save(photoPath)
    except:
        print("The image {} couldn't be edited. Please verify the file is not open by other application, or it's a video file".format(photoPath))
for photo in filesPhotos:
    for indx, magn in enumerate(magns):
        if magn in photo:
            add_SB (magnsPath[indx], photo)
input(">>> The program has finished inserting the scalebars. Press Enter to exit the program")