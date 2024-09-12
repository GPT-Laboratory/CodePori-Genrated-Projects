import requests
import json
class main:
    def __init__(self,):
        self.open_ai_api_key = "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"
        self.bot_1 = open("agent_001.txt", "r").read()
        self.bot_2 = open("agent_002.txt", "r").read()
        self.bot_3 = open("agent_003.txt", "r").read()
        self.project_descrption = "Identify issues and their solution from https://github.com/tailwindlabs/tailwindcss/discussions" # WRITE ANY PROJECT DESCRIPTION HERE
        self.bot_1 = self.bot_1.replace("PROJECT_DESCRIPTION", self.project_descrption)
        self.bot_2 = self.bot_2.replace("PROJECT_DESCRIPTION", self.project_descrption)
        self.bot_3 = self.bot_3.replace("PROJECT_DESCRIPTION", self.project_descrption)
        self.conversation_history_bot_1 = []
        self.conversation_history_bot_1.append({'role': 'system', 'content': self.bot_1})
        self.conversation_history_bot_2 = []
        self.conversation_history_bot_2.append({'role': 'system', 'content': self.bot_2})
        self.conversation_history_bot_3 = []
        self.conversation_history_bot_3.append({'role': 'system', 'content': self.bot_2})
    
    def call_chat_gpt_api(self, conversation_history, openai_api_key):
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Authorization': 'Bearer ' + openai_api_key,
            'Content-Type': 'application/json',
        }

        payload = {
            'model': 'gpt-3.5-turbo-16k',
            'messages': conversation_history,
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=50)

        return response.json()


    def process_response(self, response):
        if isinstance(response, str) and response.startswith("FALLBACK"):
            assistant_response = response
            previousResponse = assistant_response
        elif response['choices'][0]['message']['content']:
            assistant_response = response['choices'][0]['message']['content']
            previousResponse = assistant_response
        elif response['choices'][0]['message']['function_call']:
            assistant_response = response['choices'][0]['message']['function_call']
            previousResponse = assistant_response

        return assistant_response, previousResponse
    
    def run(self,):

        total_rounds = 0
        while total_rounds != 3:
            
            response = self.call_chat_gpt_api(self.conversation_history_bot_1, self.open_ai_api_key)
            assistant_response, self.previous_response = self.process_response(response)
            print(assistant_response)
            
            self.conversation_history_bot_1.append({'role': 'user', 'content': assistant_response})
            self.conversation_history_bot_2.append({'role': 'user', 'content': assistant_response})
            self.conversation_history_bot_3.append({'role': 'user', 'content': assistant_response})
            
            response = self.call_chat_gpt_api(self.conversation_history_bot_2, self.open_ai_api_key)
            assistant_response, self.previous_response = self.process_response(response)
            print(assistant_response)
            
            self.conversation_history_bot_1.append({'role': 'user', 'content': assistant_response})
            self.conversation_history_bot_2.append({'role': 'user', 'content': assistant_response})
            self.conversation_history_bot_3.append({'role': 'user', 'content': assistant_response})
            
            response = self.call_chat_gpt_api(self.conversation_history_bot_3, self.open_ai_api_key)
            assistant_response, self.previous_response = self.process_response(response)
            print(assistant_response)
            
            self.conversation_history_bot_1.append({'role': 'user', 'content': assistant_response})
            self.conversation_history_bot_2.append({'role': 'user', 'content': assistant_response})
            self.conversation_history_bot_3.append({'role': 'user', 'content': assistant_response})

            total_rounds += 1
    
if __name__ == "__main__":
    main().run()