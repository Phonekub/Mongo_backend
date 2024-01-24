from flask import request,Flask,jsonify
from pymongo.mongo_client import MongoClient
from flask_basicauth import BasicAuth

app = Flask(__name__) 
uri = "mongodb+srv://mongo:mongo@cluster0.cgejftk.mongodb.net/?retryWrites=true&w=majority"

app.config['BASIC_AUTH_USERNAME']='username'
app.config['BASIC_AUTH_PASSWORD']='password'
basic_auth = BasicAuth(app)

client = MongoClient(uri)
db = client["students"]
collection = db["std_info"]

books=[
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"}
]
stds=[]

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/students",methods=["GET"])
@basic_auth.required
def get_all_books():
    all_students = collection.find()
    for std in all_students:
        stds.append(std)
    return jsonify({"students":stds})
         

@app.route("/students/<int:std_id>",methods=["GET"])
@basic_auth.required
def get_book(std_id):
    all_students = collection.find()
    for s in all_students:
        std_id = str(std_id)
        if std_id == s["_id"]:
            student =s
            break
        else:
            student=None
    if student:
        return jsonify(student)
    else:
        return jsonify({"error":"Student not found"}),404

@app.route("/books",methods=["POST"])
def create_book():
    data = request.get_json()
    new_book={
        "id":len(books)+1,
        "title":data["title"],
        "author":data["author"]
    }
    books.append(new_book)
    return jsonify(new_book),201

@app.route("/books/<int:book_id>",methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"]==book_id),None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}),404




@app.route("/books/<int:book_id>",methods=["DELETE"])
def delete_book(book_id):
    book = next((b for b in books if b["id"]==book_id),None)
    if book:
        books.remove(book)
        return jsonify({"message":"Book deleted successfully"}),200
    else:
        return jsonify({"error":"Book not found"}),404
    




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
