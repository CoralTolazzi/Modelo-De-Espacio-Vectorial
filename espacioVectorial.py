import matplotlib
matplotlib.use('TkAgg')  # <-- Asegura que se use una GUI para mostrar gráficos

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "El veloz zorro marrón salta sobre el perro perezoso.",
    "Un perro marrón persiguió al zorro.",
    "El perro es perezoso."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(cosine_sim, annot=True, cmap="Blues",
            xticklabels=[f"Doc{i+1}" for i in range(len(documents))],
            yticklabels=[f"Doc{i+1}" for i in range(len(documents))])
plt.title("Matriz de Similitud del Coseno")
plt.show()  # <-- Esto debería abrir una ventana con el gráfico
