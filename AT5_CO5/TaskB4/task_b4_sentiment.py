"""AT5 B4: lexicon sentiment scorer and extractive summary."""
import collections, re
POSITIVE={"good","clean","fast","helpful","improved"}
NEGATIVE={"bad","dirty","slow","rude","smoke","broken"}
NEGATORS={"not","never","no"}
def score(text):
    words = re.findall(r"[a-z']+", text.lower()); total = 0
    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if i > 0 and words[i-1] in NEGATORS: value = -value
        total += value
    return total
def label(text):
    value = score(text)
    return "positive" if value > 0 else "negative" if value < 0 else "neutral"
def summarise(text, k=2):
    sentences = re.split(r"(?<=[.!?])\\s+", text.strip())
    stop = {"the","is","are","a","an","and","of","to","was"}
    freq = collections.Counter(w for w in re.findall(r"[a-z]+", text.lower()) if w not in stop)
    ranked = sorted(enumerate(sentences), key=lambda item: sum(freq[w] for w in re.findall(r"[a-z]+", item[1].lower())), reverse=True)
    chosen = {i for i,_ in ranked[:k]}
    return " ".join(s for i,s in enumerate(sentences) if i in chosen)
def main():
    complaints = ["Roads are clean and the bus was fast.","Smoke from the factory, air is bad.","The staff were not helpful.","Not bad, service improved."]
    for complaint in complaints: print(f"{label(complaint):8} | {complaint}")
    print("Summary:", summarise("Roads are clean. Smoke is bad. Buses are fast. Staff are helpful."))
if __name__ == "__main__": main()
