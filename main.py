from eventer import Eventer
import pprint
import config

            
        #     if "rosyjski" in event["summary"]:
        #         print(start, event['summary'])
        #         event["colorId"] = self.Color.Tomato
        #         updated_event = service.events().update(calendarId='ot43j3ekgcack0cu6bjf2sbvdo@group.calendar.google.com', eventId=event['id'], body=event).execute()


def main():
    pp = pprint.PrettyPrinter(indent=4)

    calendar_id = config.calendar_id
    max_results = 500
    eventer = Eventer(calendar_id)

    list_of_events = eventer.get_upcoming_events(max_results)

    if not list_of_events:
        print('No upcoming events found.')

    events_num = len(list_of_events)

    for counter, event in enumerate(list_of_events):
        summary = event["summary"]

        if summary.startswith('W '):
            eventer.set_color(event, config.LECTURE_COLOR)
            eventer.update_event(event)


        if summary.startswith('L '):
            eventer.set_color(event, config.LAB_COLOR)
            eventer.update_event(event)


        if summary.startswith('P '):
            eventer.set_color(event, config.PROJECT_COLOR)
            eventer.update_event(event)


        if summary.startswith('C '):
            eventer.set_color(event, config.PRACTICALS_COLOR)
            eventer.update_event(event)

        if summary.startswith('C '):
            eventer.set_color(event, config.SEMINARS_COLOR)
            eventer.update_event(event)


        print(f'Updated [{counter+1}/{events_num}]')
        
        
        
        #eventer.set_color(event, Eventer.Color.Graphite)
        #eventer.update_event(event)

if __name__ == '__main__':
    main()
