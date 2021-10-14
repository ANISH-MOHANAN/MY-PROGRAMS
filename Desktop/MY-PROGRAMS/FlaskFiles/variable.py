#to show importance of paasing to declared variable

from flask import Flask
new=Flask(__name__)


# @new.route('/profile/<username>')
# def profile(username):
#     return '<h1> This profile is for %s</h1>' % username
#
# new.run()

#passing id
@new.route('/profile/<int:id>')
def profile(id):
    return '<h1> This profile is for %d</h1>' % id

new.run()