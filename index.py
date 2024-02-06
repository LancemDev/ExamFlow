import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base URL for the website
base_url = 'https://ir.mksu.ac.ke/'

# Sample input names for the form fields
input_names = {
    'title': 'dc_title',
    'author': 'dv_contributor_author_last',
    'year': 'dc_date_issued',
    'month': 'dc_date_issued',
    'publisher': 'dv_publisher',
    'type': 'dc_type',
    'license': 'dv_license',
}

# Function to fill and submit the form for a single document
# def submit_document(doc):
#     return jsonify({'message': 'Document submitted!', 'status': 'success'})
    # Form data for the document
    # form_data = {
    #     # 'dc_title': 'Sample Title',
    #     'dv_contributor_author_last': 'Machakos University',
    #     'dc_date_issued_year': '2022',
    #     'dc_date_issued_month': 'December',  # Assuming the date format is YYYY-MM
    #     'dv_publisher': 'Machakos University Press',
    #     'dc_type': 'Learning Object',
    #     'decision': 'on',
    # }

    # form_data['additional_field'] = 'additional_value'
    # get title of the doc from the uploaded file
    # form_data['dc_title'] = doc.split('.')[0]

    # Submit the form
    # response = requests.post(base_url + 'submit_form', data=form_data)

    # Check if the submission was successful
    # if response.status_code == 200:
    #     print(f"Document '{doc}' submitted successfully!")
    # else:
    #     print(f"Failed to submit document '{doc}'. Status code: {response.status_code}")

# Route for testing
@app.route('/test')
def index():
    return "Urls should be working!"

@app.route('/test-uploads', methods=['GET'])
def test_uploads():
    return render_template('home/index.html')

# Route to trigger document submission
# @app.route('/submit_documents', methods=['POST'])
# def submit_documents():
    # Assuming you have a list of document names
    # document_names = request.form.getlist('documents')

    # for doc in document_names:
    #     submit_document(doc)

    # return "Documents submitted!"


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_documents', methods=['POST'])
def submit_documents():
    uploaded_files = request.files.getlist('documents')

    # Process the uploaded files as needed
    for file in uploaded_files:
        # Handle each file, for example, save it to a folder
        file.save(f'uploads/{file.filename}')

    return 'Files submitted successfully'


@app.route('/login')
def login():
    # Manually login to the website
    email = 'x@gmail.com'
    password = '12345678'

    login_url = base_url + 'login'


    # Create a session
    session = requests.Session()

    # Send a post request to the login url
    response = session.post(login_url, data={'email': email, 'password': password})

if __name__ == "__main__":
    app.run(debug=True)
