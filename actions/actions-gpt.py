from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai

class ActionChatGPT(Action):
    def name(self) -> Text:
        return "action_chat_gpt"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get user input from the latest message
        user_input = tracker.latest_message['text']

        # Make an API call to ChatGPT
        openai.api_key = "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"
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine
            prompt=user_input,
            max_tokens=50  # Adjust the response length as needed
        )

        # Extract the generated response from the API response
        chatgpt_response = response.choices[0].text.strip()

        # Send the response back to the user
        dispatcher.utter_message(text=chatgpt_response)

        return []