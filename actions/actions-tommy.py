from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionSelfControlTommyForm(Action):
    def name(self) -> Text:
        return "action_self_control_tommy"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["self_control_tommy"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_if_feel_better_tommy")
        return[]

class ActionDoBeforeTommyForm(Action):
    def name(self) -> Text:
        return "action_do_before_tommy"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["do_before_tommy"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:


        return[]

class ActionIfGoingBackTommyForm(Action):
    def name(self) -> Text:
        return "action_if_going_back_tommy"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["if_going_back_tommy"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:


        return[]

class ActionFeelDoingAgainTommyForm(Action):
    def name(self) -> Text:
        return "action_feel_doing_again_tommy"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_doing_again_tommy"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_explore_things_tommy")

        return[]

class ActionJoyTommyForm(Action):
    def name(self) -> Text:
        return "action_joy_tommy"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["joy_tommy"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_temporary_satisfaction_tommy")

        return[]

class ActionMissingOutTommyForm(Action):
    def name(self) -> Text:
        return "action_missing_out_tommy"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["missing_out_tommy"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_I_hear_you_tommy")

        return[]

class ActionOccupyMindTommyForm(Action):
    def name(self) -> Text:
        return "action_occupy_mind_tommy"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["occupy_mind_tommy"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_try_that_tommy")
        return[]