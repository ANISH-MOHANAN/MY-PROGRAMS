#how to give conditions
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/books')
def book():
    books=[{'name':'book1','author':'abc1','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},{'name':'book2','author':'abc2','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},{'name':'book3','author':'abc3','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'}]
    return render_template('object_rendering.html',books=books)

app.run(debug=True)