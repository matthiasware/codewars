def censor_this(text, words):
    words = {w.lower() for w in words}
    text = ["*"*len(i) if i.lower() in words else i for i in text.split()]
    return " ".join(text)

t, fw = "The cat does not like the therapy", ["the", "like"]
h = censor_this(t, fw)
print(h)