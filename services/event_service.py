from services.database import db_session
from models.event import Event

# Остальной код файла остается без изменений


def create_event(title, date, time, location, description):
    try:
        new_event = Event(title=title, date=date, time=time, location=location, description=description)
        new_event.save()
        return new_event
    except Exception as e:
        print(f"Error creating event: {e}")
        return None

def edit_event(event_id, title, date, time, location, description):
    try:
        event = Event.objects.get(id=event_id)
        event.title = title
        event.date = date
        event.time = time
        event.location = location
        event.description = description
        event.save()
        return event
    except Event.DoesNotExist:
        print(f"Error: Event with ID {event_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error editing event: {e}")
        return None

def delete_event(event_id):
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        return event
    except Event.DoesNotExist:
        print(f"Error: Event with ID {event_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error deleting event: {e}")
        return None
