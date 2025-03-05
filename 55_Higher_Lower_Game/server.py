from flask import Flask
from random import randint
app = Flask(__name__)

random_num = randint(0, 9)
print(random_num)


@app.route("/")
def home():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<div style="text-align: center;">'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="width:40%">'
            '</div>')


@app.route("/<int:number>")
def number(number):
    if number == random_num:
        return ('<h1 style="color:green; text-align: center">You found me!</h1>'
                '<div style="text-align: center;">'
                    '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdm9sYW4zdzg2NzR2YWR4dj'
                    'RkYzh2ODQ5aXF6ejlydGwyZXNndzcxdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o6UB3VhArvomJHtdK/giphy.gif">'
                '</div>')
    elif number > random_num:
        return ('<h1 style="color:blue; text-align: center">Too high, try again!</h1>'
                '<div style="text-align: center;">'
                    '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnlkcjV6ZzE5Y3RlbmF'
                        'tcGE1aWcwczh4c3hvdnVmNTUzaDM1Y3VnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/'
                        'fy0gLJtIkZj8I/giphy.gif" style="width:40%">'
                '</div>')
    else:
        return ('<h1 style="color:red; text-align: center">Too low, try again!</h1>'
                '<div style="text-align: center;">'
                    '<img src="https://media.giphy.com/media/eKrgVyZ7zLvJrgZNZn/giphy.gif?cid=790b7611'
                    'gqi8amwlvbgxgs9uolpzkxfg9p0acj1ihrrq9sts&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
                '</div>')


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
