from flask import Flask, jsonify, render_template, request
import json
import os
import importlib
import uuid
import requests
import time
app = Flask(__name__, template_folder='html')


LOG_DIR = "chat_logs"
os.makedirs(LOG_DIR, exist_ok=True)

API_KEY = "OpenAI API Key"
# Load the JSON data for cartoon URLs
with open("cartoon url.json") as json_file:
    cartoon_data = json.load(json_file)

voice_id_mapping = {
    "alexander": "en-US-AndrewNeural",
    "anderson": "en-US-BrianNeural",
    "essayah": "en-US-AvaNeural",
    "halla": "en-US-DavisNeural",
    "harry": "en-US-JasonNeural",
    "jutta": "en-US-EmmaNeural",
    "mika": "en-US-TonyNeural",
    "olli": "en-US-EricNeural",
    "pekka": "en-US-SteffanNeural",
}

males = [
    "alexander",
    "halla",
    "harry",
    "mika",
    "olli",
    "pekka",
    "jussi"
]
class Main:
    def __init__(self, agent_name):
        # Load agent specific data here, you might want to use agent_name
        # to load different configurations or models
        pass

    def run(self, data):
        # Process the data here and return a response
        # This method should include the logic you previously had in your script
        return "Response based on data"

@app.route('/')
@app.route('/video_generation')
def index():
    return render_template('index.html')

def is_valid_agent_name(agent_name):
    # Implement validation logic here
    # For example, only allow alphanumeric characters
    return agent_name.isalnum()


def get_video(image_url, voice_id, text, ):
    video_url = None
    talk_url = "https://api.d-id.com/talks"
    headers = {
        "accept": "application/json",
        "Authorization": f"Basic {API_KEY}"
    }
    data = {
        "source_url": image_url,
        "script":{
            "type":"text",
            "input": text,
            "provider":{
                "type":"microsoft",
                "voice_id": voice_id
            }
        }
    }

    response = requests.post(talk_url, headers=headers, json=data)
    talk_id = response.json()['id']

    while not video_url:
        output = requests.get(talk_url+"/"+talk_id, headers=headers).json()
        video_url = output.get('result_url')
        if video_url:
            break
        time.sleep(2)

    return video_url
def log_interaction(session_id, message, sender):
    session_file = os.path.join(LOG_DIR, f"{session_id}.txt")
    with open(session_file, 'a') as file:
        file.write(f"{sender}: {message}\n")

@app.route('/start_session', methods=['POST'])
def start_session():
    # Generate a unique session ID
    session_id = str(uuid.uuid4())
    session_file = os.path.join(LOG_DIR, f"{session_id}.txt")

    # Create a new file for the session
    with open(session_file, 'w') as file:
        file.write(f"Session started: {session_id}\n")

    return session_id

@app.route('/text/<agent_name>', methods=['POST'])
def text(agent_name):
    data = request.json
    session_id = data['sessionId']
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400
    
    agent_script_name = "Audio_" + agent_name.lower().split()[0]  # Assuming the script name is the agent's name in lowercase
    script_path = os.path.join(os.getcwd(), 'text_generation', f'{agent_script_name}.py')
    print(script_path)
    log_interaction(session_id, message=data['message'], sender='User')

    if not os.path.exists(script_path):
        return jsonify({"error": "Agent script not found"}), 404
    
    try:
        spec = importlib.util.spec_from_file_location(agent_script_name, script_path)
        agent_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(agent_module)

        agent_bot = agent_module.Main( data['message'])
        if agent_name.lower().split()[0] in males:
            response = agent_bot.run()
        else:
            response = agent_bot.run()
        response = response.replace("Bot 1:","")
        log_interaction(session_id=session_id, message=response, sender='Agent')
        return jsonify({"agent_response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/text_generation')
def text_generation():
    return render_template('text_generation.html')

@app.route('/get_agent/<agent_name>')
def get_agent(agent_name):
    image_url = cartoon_data.get(agent_name)
    if image_url:
        return jsonify({"imageLink": image_url})
    else:
        return jsonify({"error": "Agent not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
