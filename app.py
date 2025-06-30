from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return 'Bienvenue sur ma première application Flask !'

if __name__ == '__main__':
    app.run(debug=True)

