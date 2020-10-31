# -*- coding: utf-8 -*-

import random
from QuestionAndAnswers import question_and_answers, nierozumiem, help_description
from timer import add_timer, timer_while, show_timer, del_timer

import discord.ext
from discord.ext.commands import has_permissions
client = discord.Client()


TOKEN = "bot token"

adminid = "id of the admin user"

startwith = "how message to bot should start np &bot"


@has_permissions(administrator=True)
def if_admin(autor=None):
    if autor.id == adminid:
        return True

    return False


def get_question(content=None):
    return content.lower()[:-1].translate({ord(i): None for i in '.?!'}).rstrip()


def to_file(question, answers):
    try:

        f = open("added_questions.txt", 'a+')
        f.write("\'" + question + "\':\n[")
        for index, a in enumerate(answers):
            if index:
                f.write(",\n")
            f.write("\'" + a + "\'")
        f.write("]\n")
        f.close()
    finally:
        pass


def text(content=None):
    return content.split(" ", 1)[1]


def show(_=None):
    index = 1
    user_help_description = "```Possible questions :\n"
    for key in question_and_answers.keys():
        user_help_description = str(index) + ":" + user_help_description + key + " \n"
        index += 1
    user_help_description = user_help_description + "```"
    return user_help_description


def show_one(content=None):
    content = get_question(content)
    if question_and_answers.get(content) is not None:
        return "```" + content + " : " + str(question_and_answers.get(content)) + "```"
    return "```No question like that.```"


def add(content=None):
    question_part, answers_part = content.split("[", 1)
    question = get_question(question_part)
    answers = answers_part.split("]", 1)[0].split(";:")
    question_and_answers[question] = answers

    to_file(question, answers)

    return "```Question added.```"


def delete(content=None):
    try:
        del question_and_answers[content.lower()]
        return "```Question removed.```"
    except KeyError:
        return "```No question like that.```"


def help_user(_):
    user_help_description = "```Possible question :\n"
    for key in question_and_answers.keys():
        user_help_description = user_help_description + key + ", "
    user_help_description = user_help_description + "```"
    return user_help_description


def help_admin(_=None):
    return help_description


def add_answers(content=None):
    question_part, answers_part = content.split("[", 1)
    question = get_question(question_part)
    answers = answers_part.split("]", 1)[0].split(";:")

    if question in question_and_answers.keys():
        for answer in answers:
            question_and_answers[question].append(answer)
        to_file(question, answers)
    else:
        return "```No question like that.```"

    return "```Question added.```"


def del_answers(content=None):
    question_part, answers_part = content.split("[", 1)
    question = get_question(question_part)
    answers = answers_part.split("]", 1)[0].split(";:")

    if question in question_and_answers.keys():
        tmp_answer = question_and_answers[question]
        f = False
        del question_and_answers[question]
        for index, tmp_answer in enumerate(tmp_answer):
            for answer in answers:
                if tmp_answer == answer:
                    del tmp_answer[index]
                    f = True

        question_and_answers[question] = tmp_answer

        if f:
            return "```Answer removed.```"
        else:
            return "```No answers like that.```"
    else:
        return "```No question like that.```"


commends = {
            # admins
            'add_qanda': add,
            'show_qanda': show,
            'show_one_qanda': show_one,
            'delete_qanda': delete,
            'admin_help': help_admin,
            'add_answers_qanda': add_answers,
            'del_answers_qanda': del_answers,

            'show_timer': show_timer,
            'del_timer': del_timer,

            # users
            'help': help_user,
}


@client.event
async def on_message(message):

    if message.content.startswith(startwith):

        channel = message.channel

        return_message = ""

        question = message.content.split(" ", 1)[1].lower().translate({ord(i): None for i in '.?!'})

        if question in question_and_answers.keys():
            return_message = random.choice(question_and_answers.get(question))

        if if_admin(message.author):

            if message.content.split(" ", 2)[1].lower() == "add_timer":
                await client.wait_until_ready()
                rozmowy = client.get_channel(694503436133335042)
                content = message.content.split(" ", 2)[2]
                return_message = await add_timer(content, rozmowy)

            else:

                comm = message.content.split(" ", 2)[1].lower()     # commend

                if comm in commends.keys():
                    func = commends.get(comm)
                    if len(message.content.split(" ")) > 2:
                        content = message.content.split(" ", 2)[2]
                        return_message = func(content)
                    else:
                        return_message = func()

        if return_message == "":
            return_message = random.choice(nierozumiem)

        await channel.send(return_message)

client.loop.create_task(timer_while())

client.run(TOKEN)
