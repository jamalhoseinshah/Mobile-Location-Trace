"""
write the below code for Metadata in pycharm software and save the photo as whatever you named which i have putted name "kamal" and run code and you will find details related 
to image. as far stored location of image is very import sotherefore, you will correct folder of pycharm project folder. Moreover, i have attached snap of pycharm for your overlook.

Installation are required so therefore we are given below commands for run before this is Proceeded.

pip3. 4 install pillow.
conda install -c conda-forge exiftool

Regards
Jamal Hussain Shah

"""

from PIL import Image
from PIL.ExifTags import TAGS

# open the image
image = Image.open("kamal.jpg")

# extracting the exif metadata
exifdata = image.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)

    # passing the tagid to get its respective value
    value = exifdata.get(tagid)

    # printing the final result
    print(f"{tagname:25}: {value}")
