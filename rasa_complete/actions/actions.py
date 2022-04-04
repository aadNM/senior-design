# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, EventType, UserUtteranceReverted
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
# from rasa_sdk.events import UserUtter

class ActionSearchFacility(Action):

    def name(self) -> Text:
        return "action_search_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        facility = tracker.get_slot("facility_type")
        address = "300 Hyde St, San Fransisco"
        dispatcher.utter_message(response="Here is the address of {}:{}".format(facility, address))

        return [SlotSet("address", address)]


class ActionReflect(Action):

    def name(self) -> Text:
        return "action_reflect"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # next(tracker.get_latest_entity_values(mood_type), None)

        dispatcher.utter_message(response="utter_happy")

        return []


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_custom_fallback")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]