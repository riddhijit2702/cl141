from flask import Flask,jsonify,request
import csv

allArticles = []
likedArticles = []
dislikedArticles = []
didnotsee = []
app = Flask(__name__)
with open("article.csv",encoding = "utf-8") as files :
    reader = csv.reader(files)
    data = list(reader)
    allArticles = data[1:]
@app.route('/get-article')


def getMovie():
    return jsonify({
        
        "data " : allArticles[0],
        "status": "Sucess"
        })
        

@app.route('/liked-article',methods =  ["POST"])
def likedArticle():
    movie = allArticles[0]
    allArticles = allArticles[1:]
    likedArticles.append(movie)
    return jsonify({
        "status": "Sucess"
    })

@app.route('/disliked-article',methods =  ["POST"])
def dislikedArticle():
    movie = allArticles[0]
    allArticles = allArticles[1:]
    dislikedArticles.append(movie)
    return jsonify({
        "status": "Sucess"
    })


@app.route('/didnotsee',methods =  ["POST"])
def didnotsee():
    movie = allArticles[0]
    allArticles = allArticles[1:]
    didnotsee.append(movie)
    return jsonify({
        "status": "Sucess"
    })   

if (__name__ == "__main__") :
    app.run()