# discord_bot_q-a_timer

**add_qanda question [answer;:answer]** - adding question <br>
**add_answers_qanda existing_question [answer;:answer]** - adding an answer to an existing question  <br>
**del_answers_qanda existing_question [answer;:answer]** - deleting answers to an existing question   <br>
**delete_qanda question - removing the question show_one_qanda question** - showing a question   <br>
**show_qanda** - showing all questions  <br>
  <br>  <br>
**add_timer day/month/year hour:minute (11/11/11 11:11) or day of the week (Monday)** the text that will appear,
              when you put day of a week it will repeat itself until you deleted it   <br>
**show_timer** - lists all notifications with their next appearance date   <br>
**del_timer index_of_timer** - deletes the given reminder admin_help - this  <br>
  <br>  <br>
The bot does not consider punctuation marks, to change that, change line 28 in bot to 
```python 
return content.lower()
```
