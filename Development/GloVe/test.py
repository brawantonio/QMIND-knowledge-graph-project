from GloVe import GloVe

glove = GloVe("prebuilds/glove.6B.50d.txt")

print(glove.find_closest_embeddings("king")[1:6])
print("king -> pancake", + glove.compute_word_distance("king", "pancake"))
print("king -> queen", + glove.compute_word_distance("king", "queen"))
print("king -> prince", + glove.compute_word_distance("king", "prince"))
glove.plot_word_neighbors("king", 10)