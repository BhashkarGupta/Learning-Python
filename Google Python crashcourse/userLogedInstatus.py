def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date) #sorting event by date
  machines = {}
  for event in events:
    if event.machine not in machines: #adding event machine t othe dict
      machines[event.machine] = set()
    if event.type == "login": # add if the user has logged in 
      machines[event.machine].add(event.user)
    elif event.type == "logout": # remove if user has logged out
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0: # check if the user set is empty, in that case user has logged out ans should not be displayed
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)  