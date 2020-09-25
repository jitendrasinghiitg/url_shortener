from flask import Flask, request, render_template, jsonify, redirect, url_for
from short_url import add_link, get_link

app = Flask(__name__)


@app.route("/link", methods=['POST'])
def to_tiny_url():
    full_url = request.form["original_url"]
    print(full_url)
    tiny_url = add_link(full_url)
    return render_template('shorturl.html', data={"full": full_url,
                                                  "tiny": tiny_url})


@app.route("/get_url/<tiny_id>", methods=['GET'])
def get_tiny_url(tiny_id):
    full_url = get_link(tiny_id)
    return redirect(full_url, code=302)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
