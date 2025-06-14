from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)

# Read the HTML file
def get_html_content():
    # In production, you'd read from index.html file
    # For now, you'll need to copy the HTML content here or read from file
    with open('index.html', 'r') as file:
        return file.read()

@app.route('/')
def home():
    try:
        html_content = get_html_content()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "index.html not found. Please create the file first.", 404

# Optional: Handle contact form submission
@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Here you would typically save to database or send email
    # For now, just print and return success
    print(f"New contact form submission: {name}, {email}, {message}")
    
    return jsonify({"status": "success", "message": "Message received!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
