from flask import Flask, render_template, request
from markupsafe import Markup
import openai
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
import pymysql
import time
import json
import os

# SET PATH
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
os.chdir(dir_path)

# READ CONFIG
with open("db_config.json", "r") as json_file:
    db_config = json.load(json_file)

def sql_action(user_ip, formatted_time, user_input, ai_response):
    #sql connection
    connection = pymysql.connect(
        host=db_config["host"],
        port=db_config["port"],
        user=db_config["user"],
        password=db_config["password"],
        db=db_config["db"]
    )
    cursor = connection.cursor()

    # ADD DATA INTO SQL
    insert_query = "INSERT INTO user_info (ip, user_time, user_input, gpt_output) VALUES (%s, %s, %s, %s)"
    values = (user_ip, formatted_time, user_input, ai_response)
    cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()


openai.api_key = db_config["api_key"]
app = Flask(__name__)
messages = []


@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    # get user ip
    user_ip = request.remote_addr
    # print(f'==={user_ip}')

    # get user iput time
    timestamp = time.time()
    localtime = time.localtime(timestamp)
    formatted_time = time.strftime("%Y-%m-%d %H:%M", localtime)
    # print(f'==={formatted_time}')

    # print(user_input)
    messages.append({'role': 'user', 'content': user_input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ai_response = completion.choices[0].message['content']

    # print(ai_response)
    messages.append({'role': 'assistant', 'content': ai_response})
    print(messages)

    #SQL ADD
    sql_action(user_ip, formatted_time, user_input, ai_response)

    return  Markup(markdown.markdown(ai_response, extensions=['fenced_code', 'codehilite']))

@app.route('/reset')
def reset():
    global messages
    messages = []
    return "Conversation history has been reset."

@app.route('/history', methods = ["GET"])
def history():
    user_ip = request.remote_addr

    cursor = connection.cursor()
    search_query = "SELECT * FROM user_info WHERE ip = %s"
    cursor.execute(search_query, user_ip)
    result = cursor.fetchall()

    cursor.close()
    return render_template('history.html', result_tuple = result)


if __name__ == '__main__':
    app.run(debug=True)

