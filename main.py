from eventer import Eventer
import pprint

            
        #     if "rosyjski" in event["summary"]:
        #         print(start, event['summary'])
        #         event["colorId"] = self.Color.Tomato
        #         updated_event = service.events().update(calendarId='ot43j3ekgcack0cu6bjf2sbvdo@group.calendar.google.com', eventId=event['id'], body=event).execute()


def main():
    pp = pprint.PrettyPrinter(indent=4)

    calendar_id = "ot43j3ekgcack0cu6bjf2sbvdo@group.calendar.google.com"
    max_results = 1
    eventer = Eventer(calendar_id)

    list_of_events = eventer.get_upcoming_events(max_results)

    if not list_of_events:
        print('No upcoming events found.')
    for event in list_of_events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # print(event["summary"])
        pp.pprint(event)
        eventer.set_color(event, Eventer.Color.Graphite)
        eventer.update_event(event)

if __name__ == '__main__':
    main()