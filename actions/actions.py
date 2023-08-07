# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet, FollowupAction
# from rasa_sdk.executor import CollectingDispatcher

# class ActionSubmitProudForm(Action):
#     def name(self) -> Text:
#         return "action_proud_lucky"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#
#         return ["time_proud"]
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#
#
#         dispatcher.utter_message(template="utter_plans_next_lucky")
#
#
#         return[]
#
# class ActionNextPlanForm(Action):
#     def name(self) -> Text:
#         return "action_next_plans_lucky"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#
#         return ["next_plans"]
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#
#         latest_intent = tracker.latest_message['intent'].get('name')
#         ## if negative say
#         if latest_intent == "deny":
#             dispatcher.utter_message(template="utter_no_worries_lucky")
#       ## check if positive say then
#         else:
#             dispatcher.utter_message(template="utter_sounds_plan_lucky")
#         return[]
#
# class ActionNotExcitedForm(Action):
#     def name(self) -> Text:
#         return "action_not_excited_lucky"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#
#         return ["not_excited_lucky"]
#
#     def run(
#             self,
#             dispatcher,
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#
#
#         return[]
