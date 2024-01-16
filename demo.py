!pip install gradio

import gradio as gr
import time

with gr.Blocks() as demo:
    gr.Markdown("NOTE: Upload a document image and set a suitable scale factor for accurate OCR")
    with gr.Tab("Invoice"):
        image_1 = gr.Image(type="filepath")
        number_1 = gr.Number(value=2, label="Scale factor")
        button_1 = gr.Button("Get Payment Details")
        with gr.Row():
            name_1 = gr.Textbox(label="Client Name", interactive=True)
            inv_1 = gr.Textbox(label="Invoice Number", interactive=True)
            dt_1 = gr.Textbox(label="Invoice Date", interactive=True)
            tax_1 = gr.Textbox(label="Sales Tax", interactive=True)
            tot_1 = gr.Textbox(label="Total", interactive=True)
        dump_button_3 = gr.Button("Process Payment")
        def invoice_answers(image, scale):
            questions = ["What is the Client Name?", "What is the Invoice Number?", "What is the invoice Date?", "What is the Sales Tax?", "What is the Total?"]
            answers = get_answers(image, questions, scale)
            return answers

    with gr.Tab("e-KYC"):
        with gr.Row():
            image_2 = gr.Image(type="filepath")
            chatbot_2 = gr.Chatbot()
        number_2 = gr.Number(value=2, label="Scale factor")
        question_2 = gr.Textbox(label="Question")
        clear_2 = gr.ClearButton([question_2, chatbot_2])
        def respond_2(image, question, scale, chat_history):
            bot_message = get_answers(image, [question], scale)[0]
            chat_history.append((question, bot_message))
            time.sleep(2)
            return "", chat_history
        question_2.submit(respond_2, [image_2, question_2, number_2, chatbot_2], [question_2, chatbot_2])

    with gr.Tab("Cheque"):
        image_3 = gr.Image(type="filepath")
        number_3 = gr.Number(value=2, label="Scale factor")
        button_3 = gr.Button("Get Info")
        with gr.Row():
            pay_3 = gr.Textbox(label="Pay", interactive=True)
            amt_3 = gr.Textbox(label="Amount", interactive=True)
            ac_3 = gr.Textbox(label="Ac/No.", interactive=True)
            date_3 = gr.Textbox(label="Date", interactive=True)
        dump_button_3 = gr.Button("Process")
        def cheque_answers(image, scale):
            questions = ["What is the Date?", "What is the Pay?", "What is the Ac/No?", "What is the Amount?"]
            answers = get_answers(image, questions, scale)
            return answers

    with gr.Tab("Form"):
        gr.Markdown("Type your questions in the 'Questions' Textbox, each question in a new line")
        with gr.Row():
            image_4 = gr.Image(type="filepath")
            number_4 = gr.Number(label="Scale factor", value=2)
        with gr.Row():
            question_4 = gr.Textbox(label="Questions", lines=12)
            answer_4 = gr.Textbox(label="Answers", lines=12)
        with gr.Row():
            button_4 = gr.Button("Get answers")
            dump_button_4 = gr.Button("Dump")
        def form_answers(image, questions, scale):
            q = questions.strip("\n").split("\n")
            results = get_answers_scores(image, q, scale)
            out = ""
            for i, (ans, sco) in enumerate(results):
                out = out + f"{i+1}. {ans} (score={sco})\n"
            return out

    # with gr.Accordion("Open for More!"):
    #     gr.Markdown("Look at me...")

    button_1.click(invoice_answers, inputs=[image_1, number_1], outputs=[name_1, inv_1, dt_1, tax_1, tot_1])
    button_3.click(cheque_answers, inputs=[image_3, number_3], outputs=[date_3, pay_3, ac_3, amt_3])
    button_4.click(form_answers, inputs=[image_4, question_4, number_4], outputs=answer_4)

demo.launch() # debug=True
