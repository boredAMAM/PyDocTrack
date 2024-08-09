from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

documents = []

@app.route('/')
def home():
    return render_template('document_list.html', documents=documents)

@app.route('/add', methods=['GET', 'POST'])
def add_document():
    if request.method == 'POST':
        document_title = request.form['title']
        document_content = request.form['content']
        documents.append({'title': document_title, 'content': document_content})
        return redirect(url_for('home'))
    return render_template('add_document.html')

@app.route('/document/<int:doc_id>')
def view_document(doc_id):
    if doc_id >= len(documents) or doc_id < 0:
        return "Document not found.", 404
    return render_template('view_document.html', document=documents[doc_id])

if __name__ == '__main__':
    app.run(debug=True)