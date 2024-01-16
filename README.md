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
* Explored the possibility of extending it to beyond natural language queries by connecting to langchain agent.

## About the model
LayoutLM (huggingface documentation) is a model for effective pretraining method of text and layout for document image understanding and information extraction tasks, such as form understanding and receipt understanding.
In this notebook, a fine-tuned LayoutLM model is used for the task of Document Question Answering on documents such as invoices, forms, Cheques, ID documents, etc.
It can also perform well on unstructured documents (without clear key-value pairs) like lease agreements, just like nlp question-answering models.
