import json

def json2words(json_path):
    with open(json_path, 'r') as file:
        json_file = json.load(file)

    blocks = json_file['responses'][0]['full_text_annotation']['pages'][0]['blocks']

    words_lists = []
    for i in range(len(blocks)):
        paragraphs = blocks[i]['paragraphs']
        for j in range(len(paragraphs)):
            words_list = paragraphs[j]['words']
            words_lists.append(words_list)

    all_words = []
    bounding_box = []

    for words_data in words_lists:
        for i in range(len(words_data)):            
            word = []
            upper_left_box = words_data[i]['bounding_box']['normalized_vertices'][0]
            lower_right_box = words_data[i]['bounding_box']['normalized_vertices'][2]
            bounding_box.append([upper_left_box['x'], upper_left_box['y'], lower_right_box['x'], lower_right_box['y']])
            symbols = words_data[i]['symbols']
            for j in range(len(symbols)):
                word.append(symbols[j]['text'])
            conbined_word = ''.join(word)
            all_words.append(conbined_word)

    return all_words, bounding_box

def normalize_bbox(bboxes):
     return [
         [int(1000 * bbox[0]),
         int(1000 * bbox[1]),
         int(1000 * bbox[2]),
         int(1000 * bbox[3])]
         for bbox in bboxes
     ]

