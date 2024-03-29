import re


def text_analysis(text_list):
    try:
        amount_of_sent = amount_of_sentences(text_list)
        amount_non_declarative_sent = amount_of_non_decl_sentences(text_list)
        average_len_of_the_word, average_len_of_the_sent = average_word_and_sent_length(text_list)
    except ZeroDivisionError:
        print("Oops. Text length is 0.\n")
    except BaseException:
        print("Exception caught in text_analysis.")

    return amount_of_sent, amount_non_declarative_sent, \
        average_len_of_the_word, average_len_of_the_sent


def amount_of_sentences(text_list):
    # Amount of sentences in the text.
    return len(text_list)


def amount_of_non_decl_sentences(text_list):
    # Amount of non-declarative sentences in the text.
    amount_non_declarative_sentences = 0
    for sent in text_list:
        if sent[-1] != ".":
            amount_non_declarative_sentences += 1
    return amount_non_declarative_sentences


def average_word_and_sent_length(text_list):
    # Average length of the word in the text in characters.
    # Average length of the sentence in characters (words count only).
    average_len_of_the_word = 0
    words_list = get_word_list(r"\w*(?<![0-9])", text_list)

    for word in words_list:
        average_len_of_the_word += len(str(word))

    average_len_of_the_sent = average_len_of_the_word
    average_len_of_the_word /= len(words_list)
    average_len_of_the_sent /= len(text_list)

    return average_len_of_the_word, average_len_of_the_sent


def get_word_list(regex, text_list):
    words_list = []
    for item in text_list:
        words_list += re.findall(regex, item)
    words_list = list(filter(None, words_list))
    return words_list


# Top-K repeated N-grams in the text (K and N are taken from input if needed; by default K=10, N=4).
def generate_ngrams(text, k=10, n=4):
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    words = [word for word in text.split(" ") if word != ""]
    # Zip(*arr) == zip(arr[0], arr[1], ...)

    # [1,2,3]
    # [4,5,6]
    # [7,8,9,10]
    # ->
    ngrams = zip(*[words[i:] for i in range(n)])

    max_len_ngrams = [" ".join(ngram) for ngram in ngrams]
    max_len_ngrams.sort(key=len, reverse=True)
    return max_len_ngrams[:k]
