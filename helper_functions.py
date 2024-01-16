def up_dpi(image, scale):
    res = cv2.resize(cv2.imread(image), None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC) # scale=2 (default)
    return res


def get_word_boxes(image, scale):
    # image_as_array = cv2.imread(image)
    image_as_array = up_dpi(image, scale)
    H, W = image_as_array.shape[:2]
    # options = "tesseract sample_images/image2.jpg stdout -l eng --psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789/-"
    d = pytesseract.image_to_data(image_as_array, config="--psm 6", output_type=Output.DICT) # Image.open(image) if image is a filepath  config=options,
    n_boxes = len(d['level'])
    word_boxes = []
    for i in range(n_boxes):
        if(d["conf"][i] > 60): # Setting minimum confidence to consider
            text = d["text"][i]
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            bbox = (int(x/W*1000), int(y/H*1000), int((x+w)/W*1000), int((y+h)/H*1000))
            word_boxes.append((text, bbox))
            cv2.rectangle(image_as_array, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2_imshow(image_as_array)
    # cv2.waitKey(0)
    return word_boxes


def get_answers(image, questions, scale):
    # image->filepath, questions->List
    word_boxes = get_word_boxes(image, scale)
    n_q = len(questions)
    answers = []
    for i in range(n_q):
        result = pipe([{"image": image, "question": questions[i], "word_boxes":word_boxes}])
        ans = result[0][0]["answer"]
        # score = result[0][0]["score"]
        answers.append(ans)
    return answers

def get_answers_scores(image, questions, scale):
    # image->filepath, questions->List
    word_boxes = get_word_boxes(image, scale)
    n_q = len(questions)
    answers = []
    scores = []
    for i in range(n_q):
        result = pipe([{"image": image, "question": questions[i], "word_boxes":word_boxes}])
        ans = result[0][0]["answer"]
        score = result[0][0]["score"]
        answers.append(ans)
        scores.append(score)
    return list(zip(answers, scores))
