from datetime import datetime, timedelta
from quickstart import main
from tracker import dates1, dates2, dates3

def create():
   # creates event
   service = main()

   #d = datetime.now().date()
   tomorrow = datetime(dates1, dates2, dates3, 10)-timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=6)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Book Reminder',
           "description": 'This is a reminder to return checkout material',
           "start": {"dateTime": start, "timeZone": 'America/Chicago'},
           "end": {"dateTime": end, "timeZone": 'America/Chicago'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   create()