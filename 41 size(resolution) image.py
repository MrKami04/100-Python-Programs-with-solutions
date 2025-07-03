# program that find the resoutin of the image.

'''# NOTE: The error ModuleNotFoundError: No module named 'PIL' means 
the Pillow library is not installed.

✅ Install Pillow (modern fork of PIL) using this command 
in your terminal or command prompt:
pip install Pillow
'''
print("😍 ------------------------- 😍")
import PIL
from PIL import Image
img_variable = Image.open("E:/image/ww.jpg")
width ,height = img_variable.size

print(width, "x" , height)