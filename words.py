"""
Words analyses by Amardjia Amine.

Free software utility which allows you to find the most frequent phrases
and frequencies of words. French and English language texts are supported.
It also counts number of words, characters, the lexical density,
sentences...etc.

Usage in command line: python words.py -f [filename.txt] -w [True/False]
-h : for help.

Usage example: python words.py -f test.txt -w True
"""
import argparse
import re
import sys
import operator
from collections import Counter
from contextlib import redirect_stdout

MAX_DIPLAY = 10


class Words:

    def __init__(self, filename):
        """
        Input : text file name
        Do some operations to a text and return results.
        """
        with open(filename, "r") as fp:
            self.normal_text = fp.read().strip()
        self.normalized_text = self.normalize_text(self.normal_text)

    def all_characters_without_spaces(self, text):
        """ count the total of characters without any space char """
        return len(text) - self.number_spaces(text)

    def differents_words_list(self, text):
        """ select only the total of different words,
        it's a set, return the set.
        """
        return set(self.words_list(text))

    def average_sentence_length(self, text):
        """ count the average length of sentences
        avg = words / sentences
        """
        if len(self.words_list(text)) == 0:
            return 0
        else:
            return len(self.words_list(text)) / len(self.sentence_split(text))

    def max_sentence_length(self, text):
        """ count and return the maximum length
        of sentences list """
        all_senteces = self.sentence_split(text)
        try:
            return (max(list(map(len, all_senteces))))
        except Exception as e:
            print(e)
            return 0

    def min_sentence_length(self, text):
        """ count and return the minimum length
        of sentences list """
        all_senteces = self.sentence_split(text)
        try:
            return (min(list(map(len, all_senteces))))
        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def normalize_text(normal_text):
        """ remove extra spaces if any in the text
         and put it in lowercase, to normalize the input text.
        """
        normalized_text = re.sub(' +', ' ', normal_text)
        normalized_text = normalized_text.lower()
        return normalized_text

    @staticmethod
    def number_spaces(text):
        """ count the number of spaces in the text """
        return text.count(' ')

    @staticmethod
    def words_list(text):
        """ get all words in a list
        return the list of words [a-zA-Z_].
        """
        return re.findall("[a-zA-Z]+", text)

    @staticmethod
    def sentence_split(text):
        """ split sentences into list of sentences.
        return len(sentence_split(text)) to get the number of sentences.
        """
        sentences = re.split('[.!?]', text)
        # strip space from the sides.
        sentences = [sentence.strip()
                     for sentence in sentences if len(sentence) > 1]
        return sentences


# run the program
def run(filename, write_it):
    wa = Words(filename)
    # display text basic infos
    if write_it:
        with open("Output.txt", "w") as fp:
            """ if argument value -w is equal to True redirect the output to
            a text file if argument value -w is equal to False or not specified
            the output will be redirected to the console """
            with redirect_stdout(fp):
                display(wa)
                # display the top 'X' occurrences words
                display_top_words(wa, MAX_DIPLAY)
    else:
        display(wa)
        display_top_words(wa, MAX_DIPLAY)


def display(wa):
    """Display all the stuffs on the screen"""
    print('Total word count: ', len(wa.words_list(wa.normalized_text)))

    print('Number of different words: ',
          len(wa.differents_words_list(wa.normalized_text)))

    print('Total number of characters: ', len(wa.normal_text))
    print('Number of characters without spaces: ',
          wa.all_characters_without_spaces(wa.normal_text))

    print('Number of spaces: ', wa.number_spaces(wa.normal_text))

    print('Sentence count: ', len(wa.sentence_split(wa.normalized_text)))
    print('Average sentence length (Words): ',
          wa.average_sentence_length(wa.normalized_text))

    print('Max sentence length (Characters): ',
          wa.max_sentence_length(wa.normalized_text))

    print('Min sentence length (Characters): ',
          wa.min_sentence_length(wa.normalized_text))

    print('Lexical density: ',
          lexical_density(wa.words_list(wa.normalized_text)), ' %')
    print('\n')


def display_top_words(wa, max_display):
    cp = 0
    counts = Counter(wa.words_list(wa.normalized_text))
    sorted_occurences = sorted(
        counts.items(), key=operator.itemgetter(1), reverse=True)

    print('{0:<30}{1:<30}{2:<30}\n'.format('#Ref', 'Occurrence', 'Perc %'))

    for occurence in sorted_occurences:
        cp += 1
        if cp <= max_display:

            print('{0:<30}{1:<30}{2:<30}'.format
                  (
                      occurence[0],
                      occurence[1],
                      (occurence[1] * 100) / len(wa.words_list(wa.normalized_text)))
                  )
        else:
            break


def lexical_density(words_list):
    """ calculates the lexical density.
    L_d = (N_lex / N) * 100
    Where:

    L_d = the analyzed text's lexical density

    N_lex = the number of lexical word tokens (nouns,adjectives,verbs,adverbs)
    in the analyzed text.

    N = the number of all tokens (total number of words) in the analyzed text.
    """
    l_d = 0
    n_lex = 0
    n = 0
    with open('lexi.wd', "r") as fp:
        lexical_words = fp.read()
    lexical_words = lexical_words.split(',')

    for word in lexical_words:
        counter = words_list.count(word)
        n_lex += counter
        counter = 0

    n = len(words_list)
    l_d = (n_lex / n) * 100
    return l_d


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', default='test.txt', required=True,
                        help='The text file to analyze.', type=str)

    parser.add_argument('-w', '--write_it', default=False,
                        help='Write the output into a file text'
                        ' use True/False to specify', type=bool)

    args = parser.parse_args()
    run(args.file_name, args.write_it)
    return 0


# main
if __name__ == '__main__':
    sys.exit(main())
