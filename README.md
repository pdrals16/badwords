# service-badwords

### Tratamento 
* Stopwords
* Pontuação
* Acentuação
* Letras no minusculo
* Flexões e derivações

### Modelos 
* Bag of words
* TF-IDF
* Ngrams

### Word2Vec
* CBOW
* Skip Gram

## Run Docker 

docker build . -t badwords

docker run -d -i --name badwords --rm --network netbang -p 8000:8000 badwords