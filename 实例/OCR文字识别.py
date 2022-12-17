import pytesseract
from PIL import Image
im = Image.open('D:/Code/计算机视觉/1.png')
string = pytesseract.image_to_string(im,lang='chi_sim')
print(string)