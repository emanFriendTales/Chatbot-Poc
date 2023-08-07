from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionObsessiveReasonOscarForm(Action):
    def name(self) -> Text:
        return "action_obsessive_reason_oscar"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["obsessive_reason_oscar"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionCanChangeOscarForm(Action):
    def name(self) -> Text:
        return "action_can_change_oscar"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["can_change_oscar"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionFeelBetterOscarForm(Action):
    def name(self) -> Text:
        return "action_feel_better_oscar"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_better_oscar"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_distract_yourself_oscar")
        return[]


class ActionDistractOscarForm(Action):
    def name(self) -> Text:
        return "action_distract_oscar"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["distract_oscar"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionFeelIntrusiveThoughtsOscarForm(Action):
    def name(self) -> Text:
        return "action_feel_intrusive_thoughts_oscar"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_intrusive_thoughts_oscar"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionDistractOscarForm2(Action):
    def name(self) -> Text:
        return "action_distract_oscar_2"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["distract_oscar_2"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionFeelOscarForm2(Action):
    def name(self) -> Text:
        return "action_feel_oscar"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_oscar"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionWalkAwayOscarForm(Action):
    def name(self) -> Text:
        return "action_walk_away_oscar"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["walk_away_oscar"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]