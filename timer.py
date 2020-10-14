import aioschedule as schedule
from datetime import datetime
import asyncio
import re

tester = ["powiadomienie_pojedyncze", "[never]"]


async def make_jobe_once():
    for index, job in enumerate(schedule.jobs, start=0):
        if all(x in str(job) for x in tester):
            schedule.jobs.pop(index)


async def powiadomienie_powtarzane(text="", rozmowy=None):
    await rozmowy.send(text)


async def powiadomienie_pojedyncze(text="", rozmowy=None):
    await rozmowy.send(text)
    await make_jobe_once()
    return schedule.CancelJob


days = {
            'monday': "schedule.every().monday",
            'tuesday': "schedule.every().tuesday",
            'wednesday': "schedule.every().wednesday",
            'thursday': "schedule.every().thursday",
            'friday': "schedule.every().friday",
            'saturday': "schedule.every().saturday",
            'sunday': "schedule.every().sunday"
}


async def add_timer(content=None, rozmowy=None):

    if content.split(" ")[0][0].isdigit():  # pojedyncze powiadomienie
        day, hour, text = content.split(" ", 2)
        data = " ".join([day, hour])
        data = datetime.strptime(data, '%d/%m/%y %H:%M')
        seconds = (data - datetime.today()).total_seconds()

        schedule.every(seconds).seconds.do(powiadomienie_pojedyncze, text=text, rozmowy=rozmowy)
        data = "```One-time notification added : {}, {}, \nTreść: {}```".format(day, hour, text)

    else:   # powiadomienie powtarzane
        day, hour, text = content.split(" ", 2)

        eval(days.get(day)).at(hour).do(powiadomienie_powtarzane, text=text, rozmowy=rozmowy)
        data = "```Repeat notification added : {}, {}, \nTreść: {}```".format(day, hour, text)

    return data


def show_timer(content=None):
    return_message = "Notifications : \n"
    for index, job in enumerate(schedule.jobs, start=0):
        job_str = str(job)
        return_message += "```" + \
            str(index + 1) + " := \n" + \
            "Text :" + re.search(r"text=\'(.*?)\'", job_str).group(1) + "\n" +\
            "Date :" + job_str.split("next run: ", 1)[1][:-1] + "\n```"

    return return_message


def del_timer(content=None):
    schedule.jobs.pop(content)
    return_message = "```The notification has been removed.```"
    return return_message


async def timer_while():
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)
