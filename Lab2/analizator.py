import re


# top-K repeated N-grams in the text (K and N are taken from input if needed; by default K=10, N=4).
def text_analysis(text_list):
    # Amount of sentences in the text.
    amount_of_sentences = len(text_list)

    # Amount of non-declarative sentences in the text.
    amount_non_declarative_sentences = 0
    for sent in text_list:
        if sent[-1] != ".":
            amount_non_declarative_sentences += 1

    # Average length of the word in the text in characters.
    # Average length of the sentence in characters (words count only).
    average_len_of_the_word = 0
    words_list = get_word_list(r"\w*(?<![0-9])", text_list)

    for word in words_list:
        average_len_of_the_word += len(str(word))

    average_len_of_the_sent = average_len_of_the_word
    average_len_of_the_word /= len(words_list)
    average_len_of_the_sent /= len(text_list)

    print(amount_of_sentences)
    print(amount_non_declarative_sentences)
    print(average_len_of_the_word)
    print(average_len_of_the_sent)
    # for item in words_list:
    #     print(item)
    average_len_of_sentences = 0


def get_word_list(regex, text_list):
    words_list = []
    for item in text_list:
        words_list += re.findall(regex, item)
    words_list = list(filter(None, words_list))
    return words_list
