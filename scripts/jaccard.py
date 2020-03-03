import sys
import argparse
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


hindi_stopwords = ["अंदर","अत","अदि","अप","अपना","अपनि","अपनी","अपने","अभि","अभी","आदि","आप","इंहिं","इंहें","इंहों","इतयादि","इत्यादि","इन","इनका","इन्हीं","इन्हें","इन्हों","इस","इसका","इसकि","इसकी","इसके","इसमें","इसि","इसी","इसे","उंहिं","उंहें","उंहों","उन","उनका","उनकि","उनकी","उनके","उनको","उन्हीं","उन्हें","उन्हों","उस","उसके","उसि","उसी","उसे","एक","एवं","एस","एसे","ऐसे","ओर","और","कइ","कई","कर","करता","करते","करना","करने","करें","कहते","कहा","का","काफि","काफ़ी","कि","किंहें","किंहों","कितना","किन्हें","किन्हों","किया","किर","किस","किसि","किसी","किसे","की","कुछ","कुल","के","को","कोइ","कोई","कोन","कोनसा","कौन","कौनसा","गया","घर","जब","जहाँ","जहां","जा","जिंहें","जिंहों","जितना","जिधर","जिन","जिन्हें","जिन्हों","जिस","जिसे","जीधर","जेसा","जेसे","जैसा","जैसे","जो","तक","तब","तरह","तिंहें","तिंहों","तिन","तिन्हें","तिन्हों","तिस","तिसे","तो","था","थि","थी","थे","दबारा","दवारा","दिया","दुसरा","दुसरे","दूसरे","दो","द्वारा","न","नहिं","नहीं","ना","निचे","निहायत","नीचे","ने","पर","पहले","पुरा","पूरा","पे","फिर","बनि","बनी","बहि","बही","बहुत","बाद","बाला","बिलकुल","भि","भितर","भी","भीतर","मगर","मानो","मे","में","यदि","यह","यहाँ","यहां","यहि","यही","या","यिह","ये","रखें","रवासा","रहा","रहे","ऱ्वासा","लिए","लिये","लेकिन","व","वगेरह","वरग","वर्ग","वह","वहाँ","वहां","वहिं","वहीं","वाले","वुह","वे","वग़ैरह","संग","सकता","सकते","सबसे","सभि","सभी","साथ","साबुत","साभ","सारा","से","सो","हि","ही","हुअ","हुआ","हुइ","हुई","हुए","हे","हें","है","हैं","हो","होता","होति","होती","होते","होना","होने","मैं","मुझको","मेरा","अपने","आप को","हमने","हमारा","अपना","हम","आप","आपका","तुम्हारा","अपने","आप","स्वयं","वह","इसे","उसके","खुद","को","कि","वह","उसकी","उसका","खुद","ही","यह","इसके","उन्होने","अपने","क्या","जो","किसे","किसको","कि","ये","हूँ","होता","है","रहे","थी","थे","होना","गया","किया","जा रहा है","किया","है","है","पडा","होने","करना","करता","है","किया","रही","एक","लेकिन","अगर","या","क्यूंकि","जैसा","जब","तक","जबकि","की","पर","द्वारा","के","लिए","साथ","के","बारे","में","खिलाफ","बीच","में","के","माध्यम","से","दौरान","से","पहले","के","बाद","ऊपर","नीचे","को","से","तक","से","नीचे","करने","में","निकल","बंद","से","अधिक","तहत","दुबारा","आगे","फिर","एक","बार","यहाँ","वहाँ","कब","कहाँ","क्यों","कैसे","सारे","किसी","दोनो","प्रत्येक","ज्यादा","अधिकांश","अन्य","में","कुछ","ऐसा","में","कोई","मात्र","खुद","समान","इसलिए","बहुत","सकता","जायेंगे","जरा","चाहिए","अभी","और","कर","दिया","रखें","का","हैं","इस","होता","करने","ने","बनी","तो","ही","हो","इसका","था","हुआ","वाले","बाद","लिए","सकते","इसमें","दो","वे","करते","कहा","वर्ग","कई","करें","होती","अपनी","उनके","यदि","हुई","जा","कहते","जब","होते","कोई","हुए","व","जैसे","सभी","करता","उनकी","तरह","उस","आदि","इसकी","उनका","इसी","पे","तथा","भी","परंतु","इन","कम","दूर","पूरे","गये","तुम","मै","यहां","हुये","कभी","अथवा","गयी","प्रति","जाता","इन्हें","गई","अब","जिसमें","लिया","बड़ा","जाती","तब","उसे","जाते","लेकर","बड़े","दूसरे","जाने","बाहर","स्थान","उन्हें","गए","ऐसे","जिससे","समय","दोनों","किए","रहती","इनके","इनका","इनकी","सकती","आज","कल","जिन्हें","जिन्हों","तिन्हें","तिन्हों","किन्हों","किन्हें","इत्यादि","इन्हों","उन्हों","बिलकुल","निहायत","इन्हीं","उन्हीं","जितना","दूसरा","कितना","साबुत","वग़ैरह","कौनसा","लिये","दिया","जिसे","तिसे","काफ़ी","पहले","बाला","मानो","अंदर","भीतर","पूरा","सारा","उनको","वहीं","जहाँ","जीधर","﻿के","एवं","कुछ","कुल","रहा","जिस","जिन","तिस","तिन","कौन","किस","संग","यही","बही","उसी","मगर","कर","मे","एस","उन","सो","अत"]

# def read_qaid_file(qa_id_file):
#     qaids = []
#     with open("qa_id_file", mode='r', encoding='utf-8') as file:
#         for line in file:
#             try:
#                 qaid, _ = line.strip().split("\t")
#             except Exception as e:
#                 qaid = line.strip()
#             qaids.append(qaid)
#     return qaids

# def read_question_file(question_file):
#     questions = []
#     with open(question_file, mode='r', encoding='utf-8') as file:
#         for line in file:
#             try:
#                 _, question = line.strip().split("\t")
#             except Exception as e:
#                 question = line.strip()
                
#             questions.append(question)
    
#     return questions

# def read_answer_file(answer_file):
#     answers = []
#     with open(answer_file, mode='r', encoding='utf-8') as file:
#         for line in file:
#             try:
#                 _, answer = line.strip().split("\t")
#             except Exception as e:
#                 answer = line.strip()
            
#             answers.append(answer)
    
#     return answers

def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def main(args):
    # train_questions = read_question_file(args.answer_file)
    # count = 0 
    with open(args.test_set_file, mode='r', encoding='utf-8') as file:
        for line in file:
            # count+=1
            # print(count)
            # if args.new_format is True:
            num, ques_test, ques_train = line.strip().split("\t")
            word_list1 = nltk.word_tokenize(ques_test)
            word_list2 = nltk.word_tokenize(ques_train)

            sw = hindi_stopwords
            
            word_list1 = {w for w in word_list1 if not w in sw}  
            word_list2 = {w for w in word_list2 if not w in sw}   

            lemmatized_output1 = ' '.join([w for w in word_list1])
            lemmatized_output2 = ' '.join([w for w in word_list2])

            similarity = get_jaccard_sim(lemmatized_output1, lemmatized_output2)

            print("{}\t{}".format(1-similarity, similarity))



            # else:
            #     category, question, gold_answer_id_string = line.strip().split("\t", 2)
            #     gold_answer_ids = gold_answer_id_string.split("\t")

            #     if args.all is False and category == "1" and len(gold_answer_ids) > 1:
            #         continue

            #     for answer in answers:
            #         print("0\t{}\t{}".format(question, answer))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_set_file', dest='test_set_file', type=str, action='store', default=None)
    # parser.add_argument('--answer_file', dest='answer_file', type=str, action='store', default=None)
    # parser.add_argument('--all', dest='all', action='store_true', default=False)
    # parser.add_argument('--new_format', dest='new_format', action='store_true', default=False)
    args = parser.parse_args()
    
    main(args)
