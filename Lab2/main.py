from Toolkit.fileservice import open_file
from Toolkit.regexservice import text_analysis_with_regex
from Toolkit.stringgluer import text_gluer_with_constants
from Toolkit.analizator import text_analysis, generate_ngrams
from constants import CONSTANTS_FOR_SWITCHING, CONSTANTS_FOR_CONTINUE


def main():
    # regex = r"[A-Z][^.!?]*((\.{3})|(\.)|(\!?\??\!?))"
    regex = r"\S[^.?!]+[.!?]*"

    text = open_file("TestTxtFiles/text.txt", "r")
    my_list = text_analysis_with_regex(regex, text)

    new_list = text_gluer_with_constants(my_list,
                                         CONSTANTS_FOR_SWITCHING,
                                         CONSTANTS_FOR_CONTINUE)

    am_sent, am_non_sent, av_len_w, av_len_s = text_analysis(new_list)
    top_ngram = generate_ngrams(text, 3)

    print(f"Amount of sentences in the text: {am_sent}")
    print(f"Amount of non-declarative sentences in the text: {am_non_sent}")
    print(f"Average length of the sentence in characters: {av_len_s} char(s)")
    print(f"Average length of the word in the text in characters: {av_len_w} char(s)")
    print(f"Top-K (Max length) repeated N-grams in the text : ")
    for index in range(len(top_ngram)):
        print(f"{index + 1}: {top_ngram[index]}")


if __name__ == '__main__':
    main()
