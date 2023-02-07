import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Cargamos los datasets 'coursera_courses', 'edx' y 'udemy' en DataFrames

coursera_df = pd.read_csv("coursera_courses.csv")
edx_df = pd.read_csv("edx.csv")
udemy_df = pd.read_csv("udemy.csv")

# combinamos los títulos de los cursos en una sola lista
titles = coursera_df["name"].tolist() + edx_df["title"].tolist() + udemy_df["course_title"].tolist()

# unimos los títulos de los cursos en una sola cadena de texto
text = " ".join(titles)

# creamos la nube de palabras
wordcloud = WordCloud().generate(text)

# mostramos la nube de palabras
plt.imshow(wordcloud, interpolation='mitchell')
plt.axis("off")
plt.show()
