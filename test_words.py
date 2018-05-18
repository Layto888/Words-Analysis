
import unittest
from words import Words


class TestWordsAnalyser(unittest.TestCase):
    """class to test the words analyser """

    def setUp(self):
        self.wa = Words('test.txt')
        # input args
        self.inp = [
            ' test this    program ',
            'testthisprogram',
            '@ hello, this is a word list !',
            '_ - # ? ! . * / ^ *',
            'HI, ThIs    IS normalized text !',
            'Hi ! this is. SPARTA. What ?',
            'This is not a regular sentence',
            ' ? ! .',
            'Hi. This is the longest ! Goodbye.',
            'Hi. This is the shortest ! Goodbye.',
            'Short. First sentence. This is the longest one !',
            'TUTU is tutu for life. Test of tutu !',
            ' Total of chars without spaces '
        ]
        # expected args
        self.exp = [
            7,
            0,
            ['hello', 'this', 'is', 'a', 'word', 'list'],
            [],
            'hi, this is normalized text !',
            ['Hi', 'this is', 'SPARTA', 'What'],
            ['This is not a regular sentence'],
            [],
            19,
            2,
            2.666,
            {'tutu', 'is', 'for', 'life', 'test', 'of'},
            25
        ]

    def test_number_spaces(self):
        self.assertEqual(self.wa.number_spaces(self.inp[0]), self.exp[0])
        self.assertEqual(self.wa.number_spaces(self.inp[1]), self.exp[1])

    def test_words_list(self):
        self.assertEqual(self.wa.words_list(self.inp[2]), self.exp[2])
        self.assertEqual(self.wa.words_list(self.inp[3]), self.exp[3])
        self.assertEqual(self.wa.words_list(''), [])

    def test_normalize_text(self):
        self.assertEqual(self.wa.normalize_text(self.inp[4]), self.exp[4])
        self.assertEqual(self.wa.normalize_text(''), '')

    def test_sentence_split(self):
        self.assertEqual(self.wa.sentence_split(self.inp[5]), self.exp[5])
        self.assertEqual(self.wa.sentence_split(self.inp[6]), self.exp[6])
        self.assertEqual(self.wa.sentence_split(self.inp[7]), self.exp[7])

    def test_max_sentence_length(self):
        self.assertEqual(self.wa.max_sentence_length(self.inp[8]), self.exp[8])
        self.assertEqual(self.wa.max_sentence_length(''), 0)
        with self.assertRaises(Exception):
            self.wa.max_sentence_length([])

    def test_min_sentence_length(self):
        self.assertEqual(self.wa.min_sentence_length(self.inp[9]), self.exp[9])
        self.assertEqual(self.wa.min_sentence_length(''), 0)
        with self.assertRaises(Exception):
            self.wa.min_sentence_length([])

    def test_average_sentence_length(self):
        self.assertEqual(self.wa.average_sentence_length(''), 0)
        self.assertAlmostEqual(self.wa.average_sentence_length
                               (
                                   self.inp[10]), self.exp[10], delta=0.01
                               )

    def test_differents_words_list(self):
        self.assertEqual(self.wa.differents_words_list
                         (
                             self.inp[11].lower()), self.exp[11]
                         )
        self.assertEqual(self.wa.differents_words_list(''), set())

    def test_all_characters_without_spaces(self):
        self.assertEqual(self.wa.all_characters_without_spaces(''), 0)
        self.assertEqual(self.wa.all_characters_without_spaces
                         (
                             self.inp[12].lower()), self.exp[12]
                         )

    def test_deduce_language(self):
        pass


if __name__ == '__main__':
    unittest.main()
