# ScalebarInserter
A script that automatically adds scalebars to images taken with a standard magnification (usually with microscopes)

**************How to use it**************

You need to have a python version equal or above 3.0x and the module Pillow installed in your environment.

1. take photographs of a ruler or micrometer at their different magnifications
2. Create your scalebars using Photoshop or illustrator and save them inside the _SB_ folder. The name of the scalebar is not important, but it's essential that it ends with an underscore followed by the magnification and a capital "X"
3. Take your photographs, remembering to name them with the same protocol as you named your scalebars (e.g. photoname_10X.jpg). The program accepts .png, .tiff and .jpg
4. Deposit your images in the photos folder. You can organize your files in subfolders if you wish, and the program will find them
5. Amaze yourself by looking at your images, now with scalebars.

***Important considerations***
Don't change the folder names! The script is designed to navigate the paths inside the photos folder finding everything that looks like an image.
The program will ignore any file that doesn't look like this: "_10X.jpg" (the file extension can be different as long as it is .jpg, .tiff or .png). The "X" has to be uppercase
The program will return an error if:
A. The file is not an accepted image format (like a video)
B. The file is being used by another program


