from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "meu pedido está atrasado",
    "minha entrega não chegou",
    "quero cancelar minha compra",
    "preciso cancelar meu pedido",
    "não consigo fazer pagamento",
    "meu boleto não funciona",
    "não consigo acessar minha conta",
    "erro ao fazer login",
    "produto veio quebrado",
    "quero fazer uma reclamação"
]

labels = [
    "logistica",
    "logistica",
    "cancelamento",
    "cancelamento",
    "financeiro",
    "financeiro",
    "suporte_tecnico",
    "suporte_tecnico",
    "reclamacao",
    "reclamacao"
]

vectorizer =  CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def classify_message(message: str):
    X_new = vectorizer.transform([message])
    prediction = model.predict(X_new)[0]
    return prediction

