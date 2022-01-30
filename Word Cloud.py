import wordcloud

import numpy as np

from matplotlib import pyplot as plt

from IPython.display import display

import fileupload

import io

import sys


def _upload():
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents

        decoded = io.StringIO(change['owner'].data.decode('utf-8'))

        filename = change['owner'].filename

        print('Uploaded `{}` ({:.2f} kB)'.format(

            filename, len(decoded.read()) / 2 ** 10))

        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')

    display(_upload_widget)


_upload()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
 \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
 \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
 \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
 \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE

    non_punctuation_text = ""

    for char in file_contents:

        if char not in punctuations:
            non_punctuation_text = non_punctuation_text + char

    words = non_punctuation_text.split()

    clean_words = []

    frequencies = {}

    for word in words:

        if word.isalpha():

            if word not in uninteresting_words:
                clean_words.append(word)

    for alpha_word in clean_words:

        if alpha_word not in frequencies:

            frequencies[alpha_word] = 1

        else:

            frequencies[alpha_word] += 1

    # wordcloud

    cloud = wordcloud.WordCloud()

    cloud.generate_from_frequencies(frequencies)

    return cloud.to_array()


myimage = calculate_frequencies(
    "Python is a language with a simple syntax, and a powerful set of libraries. It is an interpreted language, with a rich programming environment, including a robust debugger and profiler. While it is easy for beginners to learn, it is widely used in many scientific areas for data exploration. This course is an introduction to the Python programming language for students without prior programming experience. We cover data types, control flow, object-oriented programming, and graphical user interface-driven applications. The examples and problems used in this course are drawn from diverse areas such as text processing, simple graphics creation and image manipulation, HTML and web programming, and genomics.")

plt.imshow(myimage, interpolation='nearest')

plt.axis('off')

plt.show()