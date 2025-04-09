from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form.get("nama")
    buku = request.form.get("buku")
    if not nama or not buku:
        return "Error 500: Data tidak lengkap", 500
    return f"Nama: {nama}, Buku: {buku}"

if __name__ == '__main__':
    app.run(debug=True)
