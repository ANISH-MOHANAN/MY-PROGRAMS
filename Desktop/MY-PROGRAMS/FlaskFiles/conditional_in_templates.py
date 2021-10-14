#how to give conditions
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return render_template('conditional.html',username=username,isActive=True)

app.run(debug=True)