from flask import Flask, request, jsonify
from ollama import chat
from ollama import ChatResponse


app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username != password:
#             return jsonify({'message': 'Login attempt received', 'username': username})
#     return '''
#         <form method="POST">
#             <input type="text" name="username" placeholder="Username" required><br>
#             <input type="password" name="password" placeholder="Password" required><br>
#             <input type="submit" value="Login">
#         </form>
#     '''

#Waitress
@app.route('/explore', methods=['GET'])
def login():
    mood = request.args.get('mood');
    buttonValue = request.args.get('SubmitButton'); 

    # process your request parameters
    rawUserInput = mood

    promptUsingUserInputText = f'Here is a paragraph(s) inputted by a user: {rawUserInput}. After carefully analyzing the tone and user\'s way of speaking, determine and describe their mood in one word'

    response: ChatResponse = chat(model='llama3.2', messages=[
        {
        'role': 'user', 'content': promptUsingUserInputText}
    ])

    finalOneWordResponse = response['message']['content'].strip()

    return finalOneWordResponse