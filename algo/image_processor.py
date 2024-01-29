# from PIL import Image
# import pytesseract
from algo.openai_model import generate_english_test_answer


# # Set up Tesseract OCR
# def extract_text_from_image(image_path):
#     img = Image.open(image_path)
#     text = pytesseract.image_to_string(img)
#     return text


def process_images(client, images):

    return generate_english_test_answer(images, client)


