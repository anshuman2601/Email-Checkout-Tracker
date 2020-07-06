from datetime import datetime, timedelta
from quickstart import main
from tracker import dates

def create():
   # creates one hour event tomorrow 10 
   service = main()

   #d = datetime.now().date()
   tomorrow = datetime(dates[5:9], dates[0:2], dates[2:4], 10)-timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Book Reminder',
           "description": 'This is a reminder to return checkout material',
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   create()