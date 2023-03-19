import fileservice
import regexservice
import constants
import stringgluer
import analizator


def main():
    # regex = r"[A-Z][^.!?]*((\.{3})|(\.)|(\!?\??\!?))"
    regex = r"\S[^.?!]+[.!?]*"

    text = fileservice.open_file("text.txt", "r")
    my_list = regexservice.text_analysis_with_regex(regex, text)

    new_list = stringgluer.text_gluer_with_constants(my_list,
                                                     constants.CONSTANTS_FOR_SWITCHING,
                                                     constants.CONSTANTS_FOR_CONTINUE)

    am_sent, am_non_sent, av_len_w, av_len_s = analizator.text_analysis(new_list)
    top_ngram = analizator.generate_ngrams(text, 3)

    print(f"Amount of sentences in the text: {am_sent}")
    print(f"Amount of non-declarative sentences in the text: {am_non_sent}")
    print(f"Average length of the sentence in characters: {av_len_s} char(s)")
    print(f"Average length of the word in the text in characters: {av_len_w} char(s)")
    print(f"Top-K (Max length) repeated N-grams in the text : ")
    for index in range(len(top_ngram)):
        print(f"{index + 1}: {top_ngram[index]}")


if __name__ == '__main__':
    main()
