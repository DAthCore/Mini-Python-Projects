#pip install python_barcode
import barcode
from barcode.writer import ImageWriter

text = "BarCode Generator in Python"
text1 = str(text)
code = barcode.get_barcode_class("code128")
image = code(text,writer=ImageWriter())
save_img = image.save('Final Barcode')
