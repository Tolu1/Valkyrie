# ======================================================================= # 
#                           NLP MODELS AND APIS                           #
# ======================================================================= #

import os
import json
import uuid
from google.cloud import dialogflow_v2 as dflow
from google.api_core.exceptions import InvalidArgument

class Dialogflow():

    def __init__(self, credentials=None, logging=True):
        if credentials == None:
            credentials='./private_key.json'

        if not os.path.exists(credentials):
            raise FileNotFoundError('Missing credentials for Google Dialogflow --> Make sure file path exists')
            
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

        with open(credentials, 'r') as data:
            self.DIALOGFLOW_PROJECT_ID = json.load(data)['project_id']
        self.DIALOGFLOW_LANGUAGE_CODE = 'en'
        self.SESSION_ID = uuid.uuid4()

        self.logging = logging

    def info(self):
        return 'Powered by Google Diagflow!📣'

    def set_session_id(self, session_id):
        self.SESSION_ID = session_id

    def interact(self, text):
        session_client = dflow.SessionsClient()
        session = session_client.session_path(self.DIALOGFLOW_PROJECT_ID, self.SESSION_ID)
        text_input = dflow.types.TextInput(text=text, language_code=self.DIALOGFLOW_LANGUAGE_CODE)
        query_input = dflow.types.QueryInput(text=text_input)

        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
            raise

        if self.logging:
            log = f"""Query text: {response.query_result.query_text}
Detected intent: {response.query_result.intent.display_name}
Detected intent confidence: {response.query_result.intent_detection_confidence}
Fulfillment text: {response.query_result.fulfillment_text}
"""
            print(log)

        return response.query_result.fulfillment_text