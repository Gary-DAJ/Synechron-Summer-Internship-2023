# Necessary Installations and Imports

!pip install transformers
!pip install torch
!pip install pillow

from transformers import AutoTokenizer, AutoModelForDocumentQuestionAnswering, AutoProcessor
tokenizer = AutoTokenizer.from_pretrained("magorshunov/layoutlm-invoices")
# processor = AutoProcessor.from_pretrained("magorshunov/layoutlm-invoices")
model = AutoModelForDocumentQuestionAnswering.from_pretrained("magorshunov/layoutlm-invoices")

from transformers import DocumentQuestionAnsweringPipeline
pipe = DocumentQuestionAnsweringPipeline(model=model, framework = "pt", tokenizer=tokenizer) #, processor=processor

!sudo apt install tesseract-ocr
!pip install pytesseract
!which tesseract
tesseract_cmd = (r'/usr/bin/tesseract')

import pytesseract
from pytesseract import Output
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
