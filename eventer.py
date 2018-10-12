"""Wrapper class for Google calendar API."""
from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from enum import Enum


class Eventer:

    # If modifying these scopes, delete the file token.json. !!!
    SCOPES = 'https://www.googleapis.com/auth/calendar.events'


    class Color:
        """Every possible color in Google Calendar.
        
        String value is proper string value requested to the API."""
        Default = "0"
        Tomato = "11"
        Tangerine = "6"
        Banana = "5"
        Basil = "10"
        Sage = "2"
        Peacock = "7"
        Blueberry = "9"
        Lavender = "1"
        Grape = "3"
        Flamingo = "6"
        Graphite = "8"

    def __init__(self, calendar_id="primary"):
        """Inits Eventer class.
        
        When using this class for the first time, go to https://developers.google.com/calendar/quickstart/python and click
        Enable the Google Calendar API. Download credentials.json and put it to your working folder.
        Before this delete token.json if it's in the folder. Class should generate this."""
        self.calendar_id = calendar_id

        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', self.SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))

    def get_upcoming_events(self, max_results=None):
        """Returns [max_result] upcoming events starting from now.
        
        If [max_results] is None, returns every events starting from now.
        Time is taken from computer clock."""
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        

        if max_results:
            events_result = self.service.events().list(calendarId=self.calendar_id, timeMin=now, # TODO primary
                                                singleEvents=True, maxResults=max_results,
                                                orderBy='startTime').execute()
        else:
            events_result = self.service.events().list(calendarId=self.calendar_id, timeMin=now, # TODO primary
                                                singleEvents=True, orderBy='startTime').execute()

        events = events_result.get('items', [])

        return events

    def set_color(self, event, color):
        """Changes colorId on event query."""
        event["colorId"] = str(color)

    def update_event(self, event):
        """Updates event on Google Calendar.
        
        Call this if you change anything in event."""
        updated_event = self.service.events().update(calendarId=self.calendar_id, eventId=event['id'], body=event).execute()
