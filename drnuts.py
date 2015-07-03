#!/usr/bin/env python2
import os
import sys
import telebot
import time
from datetime import datetime
from paip import eliza
sys.path.append(os.path.join(os.path.dirname(__file__), 'externals/paip-python/'))


TOKEN = os.environ['TELEGRAM_TOKEN']
LOGFILE = "drnuts-%s.log" % (datetime.date(datetime.now()))


rules = {
    "?*x hello ?*y": [
        "How do you do. Please state your problem."
        ],
    "?*x hi ?*y": [
        "How do you do. Please state your problem."
        ],
    "?*x bye ?*y": [
        "No good bye. See you soon.",
        "Good bye. I hope to see you again.",
        "Very well. See you later."
        ],        
    "?*x computer ?*y": [
        "Do computers worry you?",
        "What do you think about machines?",
        "Why do you mention computers?",
        "What do you think machines have to do with your problem?",
        ],
    "?*x name ?*y": [
        "I am not interested in names",
        ],
    "?*x sorry ?*y": [
        "Please don't apologize",
        "Apologies are not necessary",
        "What feelings do you have when you apologize",
        ],
    "?*x I remember ?*y": [
        "Do you often think of ?y?",
        "Does thinking of ?y bring anything else to mind?",
        "What else do you remember?",
        "Why do you recall ?y right now?",
        "What in the present situation reminds you of ?y?",
        "What is the connection between me and ?y?",
        ],
    "?*x do you remember ?*y": [
        "Did you think I would forget ?y?",
        "Why do you think I should recall ?y now?",
        "What about ?y?",
        "You mentioned ?y",
        ],
    "?*x I want ?*y": [
        "What would it mean if you got ?y?",
        "Why do you want ?y?",
        "Suppose you got ?y soon."
        ],
    "?*x if ?*y": [
        "Do you really think it's likely that ?y?",
        "Do you wish that ?y?",
        "What do you think about ?y?",
        "Really--if ?y?"
        ],
    "?*x I dreamt ?*y": [
        "How do you feel about ?y in reality?",
        ],
    "?*x dream ?*y": [
        "What does this dream suggest to you?",
        "Do you dream often?",
        "What persons appear in your dreams?",
        "Don't you believe that dream has to do with your problem?",
        ],
    "?*x my mother ?*y": [
        "Who else in your family ?y?",
        "Tell me more about your family",
        ],
    "?*x my father ?*y": [
        "Your father?",
        "Does he influence you strongly?",
        "What else comes to mind when you think of your father?",
        ],
    "?*x I am glad ?*y": [
        "How have I helped you to be ?y?",
        "What makes you happy just now?",
        "Can you explain why you are suddenly ?y?",
        ],
    "?*x I am sad ?*y": [
        "I am sorry to hear you are depressed",
        "I'm sure it's not pleasant to be sad",
        ],
    "?*x are like ?*y": [
        "What resemblence do you see between ?x and ?y?",
        ],
    "?*x is like ?*y": [
        "In what way is it that ?x is like ?y?",
        "What resemblence do you see?",
        "Could there really be some connection?",
        "How?",
        ],
    "?*x alike ?*y": [
        "In what way?",
        "What similarities are there?",
        ],
    "?* same ?*y": [
        "What other connections do you see?",
        ],
    "?*x no ?*y": [
        "Why not?",
        "You are being a bit negative.",
        "Are you saying 'No' just to be negative?"
        ],
    "?*x I was ?*y": [
        "Were you really?",
        "Perhaps I already knew you were ?y.",
        "Why do you tell me you were ?y now?"
        ],
    "?*x was I ?*y": [
        "What if you were ?y?",
        "Do you think you were ?y?",
        "What would it mean if you were ?y?",
        ],
    "?*x I am ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        ],
    "?*x am I ?*y": [
        "Do you believe you are ?y?",
        "Would you want to be ?y?",
        "You wish I would tell you you are ?y?",
        "What would it mean if you were ?y?",
        ],
    "?*x am ?*y": [
        "Why do you say 'AM?'",
        "I don't understand that"
        ],
    "?*x are you ?*y": [
        "Why are you interested in whether I am ?y or not?",
        "Would you prefer if I weren't ?y?",
        "Perhaps I am ?y in your fantasies",
        ],
    "?*x you are ?*y": [
        "What makes you think I am ?y?",
        ],
    "?*x because ?*y": [
        "Is that the real reason?",
        "What other reasons might there be?",
        "Does that reason seem to explain anything else?",
        ],
    "?*x were you ?*y": [
        "Perhaps I was ?y?",
        "What do you think?",
        "What if I had been ?y?",
        ],
    "?*x I can't ?*y": [
        "Maybe you could ?y now",
        "What if you could ?y?",
        ],
    "?*x I feel ?*y": [
        "Do you often feel ?y?"
        ],
    "?*x I felt ?*y": [
        "What other feelings do you have?"
        ],
    "?*x I ?*y you ?*z": [
        "Perhaps in your fantasy we ?y each other",
        ],
    "?*x why don't you ?*y": [
        "Should you ?y yourself?",
        "Do you believe I don't ?y?",
        "Perhaps I will ?y in good time",
        ],
    "?*x yes ?*y": [
        "You seem quite positive",
        "You are sure?",
        "I understand",
        ],
    "?*x someone ?*y": [
        "Can you be more specific?",
        ],
    "?*x everyone ?*y": [
        "Surely not everyone",
        "Can you think of anyone in particular?",
        "Who, for example?",
        "You are thinking of a special person",
        ],
    "?*x always ?*y": [
        "Can you think of a specific example?",
        "When?",
        "What incident are you thinking of?",
        "Really--always?",
        ],
    "?*x what ?*y": [
        "Why do you ask?",
        "Does that question interest you?",
        "What is it you really want to know?",
        "What do you think?",
        "What comes to your mind when you ask that?",
        ],
    "?*x perhaps ?*y": [
        "You do not seem quite certain",
        ],
    "?*x are ?*y": [
        "Did you think they might not be ?y?",
        "Possibly they are ?y",
        ],
    }

default_responses = [
    "Very interesting",
    "I am not sure I understand you fully",
    "What does that suggest to you?",
    "Please continue",
    "Go on",
    "Do you feel strongly about discussing such things?",
    ]


def listener(*messages):
    logfile = open(LOGFILE, 'a')
    for m in messages:
        rules_list = []
        for pattern, transforms in rules.items():
            # Remove the punctuation from the pattern to simplify matching.
            pattern = eliza.remove_punct(str(pattern.upper())) # kill unicode
            transforms = [str(t).upper() for t in transforms]
            rules_list.append((pattern, transforms))
        
        # chat
        chatid = m.chat.id
        if m.content_type == 'text':
            username = m.chat.username
            tgtext = m.text.encode("ascii", "replace")
            text = eliza.remove_punct(tgtext).upper()
            eliza_response = eliza.respond(rules_list, text, map(str.upper, default_responses))
            tb.send_message(chatid, eliza_response)
            # logfile, for debuggind purposes only
            logfile.write("%s - %s: \"%s\" - drnuts: \"%s\"\n" % (
                str(datetime.now()), username, tgtext, eliza_response))


def main():
    global tb
    tb = telebot.TeleBot(TOKEN)
    tb.get_update()  # cache exist message
    tb.set_update_listener(listener) #register listener
    tb.polling(5)
    while True:
        time.sleep(20)

if __name__ == "__main__":
    main()
