#Extract Data from the Document including Newline

IQBot doesn't extract the text in a new line. In order to overcome this, this repo is a workaround solution 
to implement it.

This repo shows how to extract the desired text from complete paragraph of text

### Dependencies

* cropImage.py
* ReadTxtFileDate.py

####Step 1:
*Extracting the first page of the pdf as image.
*We use pdf extract command to convert pdf to png, the command takes pdf as an input,
and the filepath to store the png, we need to enter the page no. to capture the desired page.

####Step 2:
*Crop the Name& address data Area from the Extracted Image using co-ordinates with the help  of a python script
*From the captured page, we write a python script to capture the desired area where the text that 
we want to extract is present.(Cropping of image).
*We need to add the arguments in the form of list , arg[0] as captured image path
arg[1] as cropped image path for the python arguments.
*The python code works in a way where it's cropping the image based on the coordinates, you can change the coordinates
based on the location of the desired area.

####Step 3:
*Get the text from the Cropped Image using OCR command.
*OCR can extract the text will be with the newline and whitespaces.

####Step 4:
*Write the extracted Text from the cropped Image to a TXT file. 

####Step5:
*Get the name out of the extracted text using python script
*As per the document Name will be always be on the first line 


