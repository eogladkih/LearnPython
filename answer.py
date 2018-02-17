conversation = input("что-нибудь:")


def get_answer(question):
    vocab = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return vocab[question]


#get_answer(conversation)
print (get_answer(conversation))
