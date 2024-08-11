from flask import Flask, request, render_template, redirect, url_for
import os
import json

app = Flask(__name__)

DOCUMENT_FILE = 'documents.json'

def load_documents():
    if os.path.exists(DOCUMENT_FILE):
        with open(DOCUMENT_FILE, 'r') as file:
            return json.load(file)
    return []

def save_documents(documents):
    with open(DOCUMENT_FILE, 'w') as file:
        json.dump(documents, file)

documents = load_documents()

@app.route('/')
def home():
    keyword = request.args.get('search', '')
    filtered_documents = [doc for doc in documents if keyword.lower() in doc['title'].lower()] if keyword else documents
    return render_template('document_list.html', documents=filtered_documents, search=keyword)

@app.route('/add', methods=['GET', 'POST'])
def add_document():
    if request.method == 'POST':
        document_title = request.form['title']
        document_content = request.form['content']
        documents.append({'title': document_title, 'content': document_content})
        save_documents(documents)
        return redirect(url_for('home'))
    return render_template('add_document.html')

@app.route('/document/<int:doc_id>')
def view_document(doc_id):
    if doc_id >= len(documents) or doc_id < 0:
        return "Document not found.", 404
    return render_template('view_document.html', document=documents[doc_id], doc_id=doc_id)

@app.route('/edit/<int:doc_id>', methods=['GET', 'POST'])
def edit_document(doc_id):
    if doc_id >= len(documents) or doc_id < 0:
        return "Document not found.", 404
    if request.method == 'POST':
        documents[doc_id]['title'] = request.form['title']
        documents[doc_id]['content'] = request.form['content']
        save_documents(documents)
        return redirect(url_for('view_document', doc_id=doc_id))
    return render_template('edit_document.html', document=documents[doc_id])

if __name__ == '__main__':
    app.run(debug=True)