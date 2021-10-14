#how to give conditions
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/books')
def book():
    books=['book1','book2','book3']
    return render_template('books.html',books=books)

app.run(debug=True)