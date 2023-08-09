from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionPressureHappenningForm(Action):
    def name(self) -> Text:
        return "action_pressure_happening_mia"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["pressure_happening_mia"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:


        return[]


class ActionFeelingThisTimeMiaForm(Action):
    def name(self) -> Text:
        return "action_feeling_this_time_mia"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feeling_this_time_mia"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_change_perspective_mia")

        return[]

class ActionThreeThingsMiaForm(Action):
    def name(self) -> Text:
        return "action_three_things_mia"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["three_things_mia"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_enjoy_advice_mia")

        return[]

class ActionWhatsNextMiaForm(Action):
    def name(self) -> Text:
        return "action_whats_next_mia"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["whats_next_mia"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        return[]

class ActionFeelBetterMiaForm(Action):
    def name(self) -> Text:
        return "action_feel_better_mia"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_better_mia"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_i_get_it_mia")

        return[]

class ActionLeapMiaMiaForm(Action):
    def name(self) -> Text:
        return "action_leap_mia"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["leap_mia"]

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_give_yourself_time_mia")

        return[]