from google.colab.patches import cv2_imshow
def get_word_boxes_psm(image, scale, psm=3):
    if scale<=0:
        scale = 2
    image_as_array = up_dpi(image, scale)
    H, W = image_as_array.shape[:2]
    if psm not in [1,3,4,5,6,7,8,9,10,11,12,13]:
        psm = 3
    d = pytesseract.image_to_data(image_as_array, config=f"--psm {psm}", output_type=Output.DICT)
    n_boxes = len(d['level'])
    word_boxes = []
    for i in range(n_boxes):
        if(d["conf"][i] > 60): # Setting minimum confidence to consider
            text = d["text"][i]
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            bbox = (int(x/W*1000), int(y/H*1000), int((x+w)/W*1000), int((y+h)/H*1000))
            word_boxes.append((text, bbox))
            cv2.rectangle(image_as_array, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image_as_array, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    # cv2_imshow(image_as_array)
    # cv2.waitKey(0)
    return image_as_array
