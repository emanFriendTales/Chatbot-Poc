from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionTellMoreSimonForm(Action):
    def name(self) -> Text:
        return "action_tell_more_simon"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["tell_more_simon"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionWhyHappenedSimonForm(Action):
    def name(self) -> Text:
        return "action_why_happened_simon"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["why_happened_simon"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionMoreDetailsSimonForm(Action):
    def name(self) -> Text:
        return "action_more_details_simon"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["more_details_simon"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionDifferentSimonForm(Action):
    def name(self) -> Text:
        return "action_different_simon"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["different_simon"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionGoingToDoSimonForm(Action):
    def name(self) -> Text:
        return "action_going_to_do_simon"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["going_to_do_simon"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionBestOptionSimonForm(Action):
    def name(self) -> Text:
        return "action_best_option_simon"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["best_option_simon"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_sadness_temporary_simon")

        return[]

class ActionHaveYouTalkedSimonForm(Action):
    def name(self) -> Text:
        return "action_have_you_talked_simon"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["have_you_talked_simon"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(template="utter_talk_to_me_simon")

        return[]