import numpy as numpy
import tensorflow as tf
import time
import re

lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
convos = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

id2line = {}

for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

convos_id = []

for convo in convos[:-1]:
    _convo = convo.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
    convos_id.append(_convo.split(','))

questions = []
answers = []

for convo in convos_id:
    for i in range(len(convo) - 1):
        questions.append(id2line[convo[i]])
        answers.append(id2line[convo[i+1]])

def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm","i am", text)
    text = re.sub(r"it's","it is", text)
    text = re.sub(r"he's","he is", text)
    text = re.sub(r"she's","she is", text)
    text = re.sub(r"that's","that is", text)
    text = re.sub(r"what's","what is", text)
    text = re.sub(r"where's","where is", text)
    text = re.sub(r"\'ll"," will", text)
    text = re.sub(r"\'ve"," have", text)
    text = re.sub(r"\'re"," are", text)
    text = re.sub(r"\'d"," would", text)
    text = re.sub(r"won't","will not", text)
    text = re.sub(r"don't","do not", text)
    text = re.sub(r"can't","cannot", text)
    text = re.sub(r"couldn't","could not", text)
    text = re.sub(r"wouldn't","would not", text)
    text = re.sub(r"shouldn't","should not", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?!,]","", text)
    return text

clean_questions = []

for question in questions:
    clean_questions.append(clean_text(question))

clean_answers = []

for answer in answers:
    clean_answers.append(clean_text(answer))

word2count = {}

for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

threshold = 20

questionswords2int = {}
wd_num = 0

for word, count in word2count.items():
    if count >= threshold:
        questionswords2int[word] = wd_num
        wd_num += 1

answerswords2int = {}
wd_num = 0

for word, count in word2count.items():
    if count >= threshold:
        answerswords2int[word] = wd_num
        wd_num += 1

tokens = ['<PAD>','<EOS>','<OUT>','<SOS>']

for token in tokens:
    questionswords2int[token] = len(questionswords2int) + 1

for token in tokens:
    answerswords2int[token] = len(answerswords2int) + 1

answersints2words = {w_i: w for w, w_i in answerswords2int.items()}

for i in range(len(clean_answers)):
    clean_answers[i] += ' <EOS>'

questions_2_int = []

for question in clean_questions:
    ints = []
    for word in question.split():
        if word not in questionswords2int:
            ints.append(questionswords2int['<OUT>'])
        else:
            ints.append(questionswords2int[word])
    
    questions_2_int.append(ints)

answers_2_int = []

for answer in clean_answers:
    ints = []
    for word in answer.split():
        if word not in answerswords2int:
            ints.append(answerswords2int['<OUT>'])
        else:
            ints.append(answerswords2int[word])
    
    answers_2_int.append(ints)

sorted_clean_questions = []
sorted_clean_answers = []

for length in range(1, 25 +1):
    for i in enumerate(questions_2_int):
        if len(i[1]) == length:
            sorted_clean_questions.append(questions_2_int[i[0]])
            sorted_clean_answers.append(answers_2_int[i[0]])

################################### Tensorflow section Below #########################################