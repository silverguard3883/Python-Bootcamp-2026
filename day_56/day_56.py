from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
# def home():
#     return render_template('index_practice.html')            #Flask only accepts html files from a "templates" folder
#                                                             #Static files (like images) are only accepted from a "static" folder
#
# if __name__ == '__main__':
#     app.run(debug=True)

def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

