
from PIL import Image

import pytesseract

# img_cv = cv2.imread(r'one_slide.png')

img = r"input_sample/pdf_slide/one_slide.png"

pytesseract.pytesseract.tesseract_cmd = (r'/usr/local/bin/tesseract')

# print(pytesseract.image_to_string(img))
print(pytesseract.image_to_string(Image.open(img)))
