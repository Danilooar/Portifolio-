<<<<<<< HEAD
from flask import Flask, render_template # type: ignore
=======
from flask import Flask, render_template
>>>>>>> 45cdfe183815a81e50d9a5f17a133544f1cd6453

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()