from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator

def split_word(word):
    if 70 <= len(word) < 140:
        return [word[:70], word[70:]]
    elif 140 <= len(word) < 210:
        return [word[:70], word[70:140], word[140:]]
    elif 210 <= len(word):
        return [word[:70], word[70:140], word[140:210], word[210:]]


def count_elements(word_list):
    count = 0
    for word in word_list:
        if type(word) == list:
            for _word in word:
                count += 1
        else:
            count += 1
    return count


class TextImage:
    def __init__(self, word_list):
        for index, word in enumerate(word_list):
            if not len(word) < 70:
                word_list[index] = split_word(word)
        print(word_list)
        print(count_elements(word_list))

        if count_elements(word_list) == len(word_list):
            img = Image.new('RGB', (25 + len(max(word_list, key=len)) * 85, len(word_list) * 200),
                            color=(255, 255, 255))
        else:
            img = Image.new('RGB', (8192, count_elements(word_list) * 200),
                            color=(255, 255, 255))

        font = ImageFont.truetype(r'fonts/Hannari.otf', 115)

        draw = ImageDraw.Draw(img)

        # index in enumerate can't be modified, thus a counter variable is used
        count = 0
        color_count = 0

        for word in word_list:
            # count colour_count only when language switches
            color_count += 1

            if type(word) == list:
                for _word in word:
                    if len(_word) != 0:

                        if color_count % 2 == 0:
                            draw.text((100, 25 + count * 150), _word, font=font, fill=(224, 101, 56))
                            count += 1
                        else:
                            draw.text((100, 25 + count * 150), _word, font=font, fill=(0, 0, 0))
                            count += 1

            else:
                if color_count % 2 == 0:
                    draw.text((100, 25 + count * 150), word, font=font, fill=(224, 101, 56))
                    count += 1
                else:
                    draw.text((100, 25 + count * 150), word, font=font, fill=(0, 0, 0))
                    count += 1

        self.file_name = str(word_list[0]) + '.png'
        self.file_location = 'images/' + self.file_name
        img2 = img.resize(img.width*0.8, img.height*0.8)
        img2.save(self.file_location)


