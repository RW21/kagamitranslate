from googletrans import Translator


def chained_translations(phrase, target_language, source_language):
    translator = Translator()

    while True:
        phrase = translator.translate(phrase, src=source_language, dest=target_language).text
        yield phrase
        source_language, target_language = target_language, source_language


def generate_chained_list(target_list, generator):
    """Since listcomp isn't a good idea with generators, a list is created by this function"""
    for i in range(10):
        next_word = next(generator)
        if next_word not in target_list:
            target_list.append(next_word)

    return target_list


class Translate:
    def __init__(self, phrase, target_language=None, source_language=None):
        translator = Translator()

        source_language = source_language or translator.detect(phrase).lang

        if target_language is None:
            if source_language == 'en':
                target_language = 'ja'
            elif source_language == 'ja':
                target_language = 'en'
            else:
                raise TargetLanguageException

        self.word_list = [phrase]

        self.word_list = generate_chained_list(self.word_list,
                                               chained_translations(phrase, target_language,
                                                                    source_language))

    def __getitem__(self, item):
        return self.word_list[item]

    def __len__(self):
        return len(self.word_list)


class TargetLanguageException(Exception):
    """Raise error for when there is no clear target language"""
