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


import smtplib

# class ActionSuicidal(Action):

#     def name(self) -> Text:
#         return "action_suicidal"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         updated_slots = domain_slots.copy()
#         if 
#         dispatcher.utter_message(response="utter_happy")

#         return []



class ActionSearchFacility(Action):

    def name(self) -> Text:
        return "action_search_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.get_latest_entity_values()
        facility = tracker.get_slot("facility_type")
        address = tracker.get_slot("location_info")
        
        if address is None:
            dispatcher.utter_message(response="utter_ask_location")
        address = tracker.get_slot("location_info")
        
        if "lawrence" in address or "Lawrence" in address or "LFK" in address or "lfk" in address:
            dispatcher.utter_message(response="utter_lfk_resouces")
        else:
            dispatcher.utter_message(response="utter_local_resources")
        # dispatcher.utter_message(response="Here is the address of {}:{}".format(facility, address))

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

class Sendmail(Action):

    def name(self) -> Text:
        return "action_send_mail"
         
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Subject = tracker.get_slot('Subject')
        Body = tracker.get_slot('Body')
        Recipient = tracker.get_slot('Recipient')


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #connect to smtp server
        server.login("sender@gmail.com", "sender_pswd")  
        # you can write your mail and or get it from the slots with tracker.get_slot
        # if you are using your email is better that you dont pass it through the code for security u can 
        # set path variables with email and password and use them instead


        msg ="Subject: {} \n\n {} " .format(Subject,Body) #creating the message

        server.sendmail("sender@gmail.com", Recipient, msg)                         
        server.quit()  

        dispatcher.utter_message(" Email sended ! ")
        return [SlotSet("to",Recipient)] #just in my case, u can return ntg

