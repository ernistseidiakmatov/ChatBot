from train import *
import window
import random


def bag_of_words(s, wordss):
    bagg = [0 for _ in range(len(wordss))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, ww in enumerate(wordss):
            if ww == se:
                bagg[i] = 1
    return numpy.array(bagg)


def chat(inp):
    global responses
    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data['intents']:
        if tg['tag'] == tag:
            responses = tg['responses']

    return random.choice(responses)


def botreply():
    que = window.question.get()
    if not que:
        window.textArea.config(state=window.NORMAL)
        window.textArea.insert(window.END, "Bot: Please, text something\n", 'b')
        window.textArea.yview_moveto(1)
        window.textArea.config(state=window.DISABLED)

    else:
        answer = chat(que)
        window.textArea.config(state=window.NORMAL)
        window.textArea.insert(window.END, " You: " + que + "\n", "u")
        window.textArea.insert(window.END, " Bot: " + answer + "\n", "b")
        window.textArea.yview_moveto(1)
        window.textArea.config(state=window.DISABLED)
        window.question.delete(0, window.END)


def enter(event):
    botreply()


def close():
    window.root.quit()
