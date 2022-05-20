from time import localtime
from json import load
from webbrowser import open as openweb


mon, mday, wday, hour, minute = str(localtime().tm_mon), str(localtime().tm_mday), localtime().tm_wday, str(localtime().tm_hour), str(localtime().tm_min)

if len(minute) == 1:
    minute = '0'+minute

if len(hour) == 1:
    hour = '0'+hour

if len(mday) == 1:
    mday = '0'+mday

if len(mon) == 1:
    mon = '0'+mon


with open("schedule.json", 'r') as f:
    schedule = load(f)

with open("Links.json", 'r') as f:
    links = load(f)

today = schedule[wday]

classtime = list(today.keys())
decide = False
for i in classtime:
    if (int(hour+minute) <= (int(i)+10)) and (decide == False):
        upcoming = i
        decide = True

if decide:
    info = links[today[upcoming]]
    openweb(info[1])
    
    with open('log.txt', 'a') as f:
        f.write(f"[{mon}/{mday} {hour}:{minute}] Joined {info[0]} with the link {info[1]}\n")