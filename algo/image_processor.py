from PIL import Image
import pytesseract
from algo.openai_model import generate_english_test_answer


# Set up Tesseract OCR
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text


def process_images(images):
    concatenated_text = ""

    for image in images:
        text = extract_text_from_image(image)
        concatenated_text += text + " "

    return generate_english_test_answer(concatenated_text)


# image_paths = ['D:\\Projects\\TestHelperServer\\static\\test.jpg']
#
# print(process_images(image_paths))
