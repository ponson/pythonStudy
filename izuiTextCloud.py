import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import numpy as np
from PIL import Image


text = open("./data/IndianHistoryWiki.txt", encoding='utf8').read()
text = text.replace('\n', "").replace("\u3000", "")

text_cut = jieba.lcut(text)
# print(text_cut)
text_cut = ' '.join(text_cut)
# print(text_cut)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
# word_cloud = WordCloud(background_color='white', stopwords=stop_words)
# mask_color = np.array(Image.open("data/chiefwahoo872x924Black.png"))
mask_color = np.array(Image.open("data/blockCblack.png"))
mask_color = mask_color[::3, ::3]
mask_image = mask_color.copy()
mask_image[mask_image.sum(axis=2) == 0] = 255
word_cloud = WordCloud(background_color='white', mask=mask_image, stopwords=stop_words)
word_cloud.generate(text_cut)
image_colors = ImageColorGenerator(mask_color)
word_cloud.recolor(color_func=image_colors)
word_cloud.to_file("output/indians.png")
# print(stop_words)

# plt.subplots(figsize=(12, 8))
# plt.imshow(word_cloud)
# plt.axis("off")
# plt.show()