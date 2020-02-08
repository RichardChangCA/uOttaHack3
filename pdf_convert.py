
from PIL import Image

try:
    import pytesseract
    # import the tesseract exeuctable for the package
    pytesseract.pytesseract.tesseract_cmd = (r'/usr/local/bin/tesseract')
except:
    print("Please installed tesseract before running this file")
    exit(-1)

def convert_image_to_string(file_path="input_sample/pdf_slide/one_slide.png"):
    return pytesseract.image_to_string(Image.open(file_path))



# print(pytesseract.image_to_string(img))

def test_convert_to_string():
    result =convert_image_to_string()
    assert result is not None , exit(-1)
    assert isinstance(result,str), exit(-1)

if __name__ == "__main__":
    test_convert_to_string()