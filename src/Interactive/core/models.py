# ======================================================================= # 
#                           NLP MODELS AND APIS                           #
# ======================================================================= #

import os
import json
import uuid
from google.cloud import dialogflow_v2 as dflow
from google.api_core.exceptions import InvalidArgument

class Dialogflow():
    
    def connect(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.get_credentials()

        with open(self.credentials, 'r') as data:
            self.project_id = json.load(data)['project_id']
        self.language_code = 'en'
        self.sessions_id = uuid.uuid4()
        self.sessions_client = dflow.SessionsClient()
        self.session = self.sessions_client.session_path(self.project_id, self.sessions_id)


    def info(self):
        return 'Powered by Google Diagflow!📣'

    def set_session_id(self, session_id):
        self.sessions_id = session_id

    def set_credentials(self, credentials):
        self.credentials = credentials
    
    def get_credentials(self):  
        
        # default path
        if hasattr(self, 'credentials') is False:  
            self.set_credentials('./private_key.json')  
        if self.credentials is None:  
            self.set_credentials('./private_key.json')
        if not os.path.exists(self.credentials):
            raise FileNotFoundError('Missing credentials for Google Dialogflow --> Make sure file path exists')
        return self.credentials
        
    def console(self):
        print('===================================Welcome to Dialogflow Console===================================')
        try:
            while True:
                print(self.interact(input()))
        except KeyboardInterrupt:
            print('> You stopped the Console.')
        
    def interact(self, text, logging=False):
        text_input = dflow.types.TextInput(text=text, language_code=self.language_code)
        query_input = dflow.types.QueryInput(text=text_input)

        try:
            response = self.sessions_client.detect_intent(session=self.session, query_input=query_input)
        except InvalidArgument:
            raise

        if logging:
            log = f"""Query text: {response.query_result.query_text}
Detected intent: {response.query_result.intent.display_name}
Detected intent confidence: {response.query_result.intent_detection_confidence}
Fulfillment text: {response.query_result.fulfillment_text}
"""
            print(log)

        return response.query_result.fulfillment_text

    class Rasa():
        
        def info(self):
            return 'Rasa will be coming soon!📣'