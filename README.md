# Synechron-Summer-Internship-2023

## Aim of the project
* To explored relevant blogs and Deep Learning platforms and perform an expository analysis of various state-of-the-art models for OCR and its downstream tasks, for usage by banks.
* Narrow down to one downstream tasks of OCR that seem most useful for banks in daily work.
* Prepare datasets to evaluate the performance of various open-source fine-tuned models on various aspects such as segmented pages, multiple tables, varying fonts, handwritting, little poor quality scans, etc, to ensure that it is suitable for various documents that banks encounter.
* Create a UI to enable tasks such as natural language queries and to extract key information with limited or no human intervention.

## Tasks completed
* Demonstrated the use of a LayoutLM model fine-tuned on a dataset of invoices, SQuAD2.0 and DocVQA in Document Visual Question Answering to extract key information from invoices.
* Used Tesseract for OCR, to get the words and bounding boxes in an image. Implemented magorshunov/layoutlm-invoices model from huggingface.co using Transformers framework, in a colab notebook.
* Used Gradio to create a UI, including a Chatbot for natural language queries on document images such as Cheques, Invoices, Forms, Identity Documents, etc. to extract key information.
* Explored and tested various page segmentation modes in Tesseract and made a UI to enable controlling certain parameters to get better results.
* Explored the possibility of extending it to beyond natural language queries by connecting to langchain agent and using its Generative AI.

## About the model
LayoutLM (huggingface documentation) is a model for effective pretraining method of text and layout for document image understanding and information extraction tasks, such as form understanding and receipt understanding.
In this notebook, a fine-tuned LayoutLM model is used for the task of Document Question Answering on documents such as invoices, forms, Cheques, ID documents, etc.
It can also perform well on unstructured documents (without clear key-value pairs) like lease agreements, just like nlp question-answering models.

## Helper Functions
1. `up_dpi(image, scale)`: It takes as input 2 parameters- `image`, the image as filepath, `scale`, the factor by which you want to scale the image. \
It returns the resized image `res` as array.
2. `get_word_boxes(image, scale)`: It takes as input 2 parameters- `image`, the image as filepath, `scale`, the factor by which you want to scale the image. It performs OCR using Tesseract. \
Currently, the configuration used is `--psm 6`. The configuration can be played around with, to get the best OCR results. A good read on Tesseract page segmentation modes can be found [here](https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/). \
This functions extracts the word and bounding box coordinates, normalizes it to (1000, 1000) and returns them as a `list[(str)text, ((int)x0, (int)y0, (int)x1, (int)y1)]`. \
The statement `if(d["conf"][i]>60)` sets the minimum confidence score for text to be considered. This helps remove noise caused due to images, few characters of different languages, etc.
3. `get_answers(image, questions, scale)`: It takes 3 parameters as input- `image`, the image as filepath, `questions`, a `list[(str)question]`. \
It iterates through `questions` and passes the `image`, i_th question, the word and bounding box information into the document question answering pipeline created in the imports section. \
It returns a list `answers`.
4. `get_answers(image, questions, scale)`: Same as `get_answers` except that it returns a `list[(str)answer, (float)confidence score]`. It is sometimes useful to know the confidence score because it is an indicator of a possible incorrect answer.

## Demo
Used Gradio for the demo
- Tab 1: Invoices- \
Click on upload an image. It uploads an image and stores it as filepath (because the functions that are called, take an image as filepath). Set a suitable scale. Click on "Get Payment Details" button to extract some key information from the invoice. The "Process Payment" button does not work for now.
- Tab 2: e-KYC- \
This tab has a chatbot for natural language queries. Upload an image, set a suitable scale, type a question and hit enter. Click on "Clear" when you want to clear the chat history.
- Tab 3: Cheques- \
Functionality is similar to Invoices tab. It performs decent on handwritten cheques. It almost always gets the A/C No. correctly. Sometimes messes up with the name and amount. The right question asked in the `cheque_answers()` function can get the required answer. Sometimes, fancy font styles in cheques also affects the results.
- Tab 4: Forms- \
You can ask all possible questions, in newlines, in the "Questions" Textbox. Click the "Get answers" button. All the answers with their confidence scores will appear in the "Answers Textbox. **This tab is good for experimentation.**

## Examples
Some examples are given to check the working of the various tabs in the UI.

## Adjusting parameters
- A gradio demo to show how changing the Tesseract page segmentation mode and scale of the image can change OCR results.
- I have used psm 6 as the default configuration in the above demo because it worked well in most cases.
- If you have a folder full of document images of one type, you can experiment with one image to get the suitable scale and psm for images of that type.

## Langchain agent
Another idea is to use langchain to include Generative AI in the chatbot. You can first use the "Forms" mode to get all possible questions and answers and include it under the "Summary of the conversation". Then, under "Current conversation", you can enter a question that can be answered by Generative AI. The implementation is not completed yet.
