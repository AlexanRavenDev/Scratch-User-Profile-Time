import scratchattach as scratch3
import requests
import datetime
session = scratch3.login("username", "password") 
user = session.get_linked_user()

def format_time(raw_time):
    datetime_obj = datetime.datetime.fromisoformat(raw_time)
    
    formatted_time = datetime_obj.strftime("%A, %d %B %Y, %H:%M:%S")
    return formatted_time

def othersleep(seconds): # time.sleep() was broken when I ran it so this it what I am sticking with
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(seconds=seconds)
    
    while datetime.datetime.now() < end_time:
        pass

def get_current_time():
    url = "http://worldtimeapi.org/api/ip"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current_time = data['datetime']
        return current_time
    else:
        return "Failed to retrieve time"


while 1==1:
    time = get_current_time()
    current_time = get_current_time()
    formatted_time = format_time(current_time)
    formatted_time = format_time(time)
    print("Current time:", formatted_time)
    print('Sending to servers')
    # Modify what's below to change what shows up on your wiwo 
    # Add a line below f""" and change that to make it show up there!
    wiwo_text  = f"""
{formatted_time} (localized to my local pos)
    """
    user.set_wiwo(wiwo_text)
    # Swap set_wiwo for set_bio to make it come on your About me
    print('Done')
    othersleep(30)
