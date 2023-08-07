from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker

class ActionCountdownDoneAnaForm(Action):
    def name(self) -> Text:
        return "action_countdown_done_anna"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["countdown_done_anna"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionFeelReasonAnaForm(Action):
    def name(self) -> Text:
        return "action_feel_reason_ana"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_reason_ana"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionHappenedBeforeAnaForm(Action):
    def name(self) -> Text:
        return "action_happened_before_ana"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["happened_before_ana"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionGoodAtAnaForm(Action):
    def name(self) -> Text:
        return "action_good_at_ana"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["good_at_ana"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionIfApplyAnaForm(Action):
    def name(self) -> Text:
        return "action_if_apply_ana"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["if_apply_ana"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]