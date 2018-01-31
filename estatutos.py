#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

stop_words = '''
el la los las por de del que se y que
a ante bajo con contra de desde en entre hacia hasta para por segun
sin sobre tras durante mediante
'''.split()

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'estatutos.md')).read()
for w in stop_words:
    text = text.replace(w, '')

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
