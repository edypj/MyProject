from textblob import TextBlob
import nltk
nltk.download('movie_reviews')


# Fungsi untuk melakukan analisis sentimen
def analisis_sentimen(teks):
    analisis = TextBlob(teks)
    if analisis.sentiment.polarity > 0:
        return "Sentimen positif"
    elif analisis.sentiment.polarity < 0:
        return "Sentimen negatif"
    else:
        return "Sentimen netral"

# Contoh teks dengan sentimen negatif
teks_negatif = "Produk ini sangat buruk dan saya sangat kecewa!"
hasil_negatif = analisis_sentimen(teks_negatif)
print("Hasil analisis untuk teks negatif:", hasil_negatif)

# Contoh teks dengan sentimen positif
teks_positif = "Saya sangat senang dengan produk ini!"
hasil_positif = analisis_sentimen(teks_positif)
print("Hasil analisis untuk teks positif:", hasil_positif)

# Contoh teks dengan sentimen netral
teks_netral = "Ini adalah produk yang standar."
hasil_netral = analisis_sentimen(teks_netral)
print("Hasil analisis untuk teks netral:", hasil_netral)