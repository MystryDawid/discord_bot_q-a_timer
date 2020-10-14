question_and_answers = {
    'question1':
        [
            'answer',
            'answer',
            'answer',
            'answer'
        ],
    'question2':
        [
            'answer',
            'answer',
            'answer',
            'answer'
        ],
    'question3':
        [
            'answer',
            'answer',
            'answer',
            'answer'
        ]

}

nierozumiem = [
    "I don't understand.",
]

help_description = "```" \
                   "add_qanda question [answer;:answer] - adding question \n" \
                   "add_answers_qanda existing_question [answer;:answer] - adding an answer to an existing question \n" \
                   "del_answers_qanda existing_question [answer;:answer] - deleting answers to an existing question \n" \
                   "delete_qanda question - removing the question \n"  \
                   "show_one_qanda question - showing a question \n" \
                   "show_qanda - showing all questions \n" \
                   "add_timer day/month/year hour:minute (11/11/11 11:11) or day of the week (Monday) \n " \
                   "the text that will appear, when you put day of a week it will repeat itself until you deleted it \n" \
                   "show_timer - lists all notifications with their next appearance date \n" \
                   "del_timer index_of_timer - deletes the given reminder \n" \
                   "admin_help - this \n" \
                   "```"