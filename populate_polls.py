import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'mysite.settings')  # enter your project's name here.

django.setup()

from polls.models import Question, Choice


def populate():
    # First, we will create lists of dictionaries containing the choices
    # we want to add into each question.
    # Then we will create a dictionary of dictionaries for our questions.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    question_1 = 'Which of the following is used as a moderator in nuclear reactor?'
    question_2 = 'Which among the following is a positively charged particle emitted by a radioactive element?'
    question_3 = 'Atoms are composed of'
    question_4 = 'In an atomic explosion, enormous energy is released which is due to'
    question_5 = 'Isotopes are separated by'
    question_6 = 'Which of the following has a least penetrating power?'

    question_1_choices = [
        {"choice_text": "Thorium"},
        {"choice_text": "Graphite"},
        {"choice_text": "Radium"},
        {"choice_text": "Water"}
    ]

    question_2_choices = [
        {"choice_text": "Beta Ray"},
        {"choice_text": "Alpha Ray"},
        {"choice_text": "Cathode Ray"},
        {"choice_text": "Gamma Ray"}
    ]

    question_3_choices = [
        {"choice_text": "Electrons and protons"},
        {"choice_text": "Electrons only"},
        {"choice_text": "Protons only"},
        {"choice_text": "Electrons and nuclei"}
    ]

    question_4_choices = [
        {"choice_text": "Conversion of chemical energy into heat energy"},
        {"choice_text": "Conversion of mechanical energy into nuclear energy"},
        {"choice_text": "Conversion of mass into energy"},
        {"choice_text": "Conversion of neutrons into protons"}
    ]

    question_5_choices = [
        {"choice_text": "Crystallisation"},
        {"choice_text": "Sublimation"},
        {"choice_text": "Distillation"},
        {"choice_text": "Filtration"}
    ]

    question_6_choices = [
        {"choice_text": "All have same penetrating power"},
        {"choice_text": "Beta Particles"},
        {"choice_text": "Alpha particles"},
        {"choice_text": "Gamma rays"}
    ]

    questions = {
        question_1: {"choices": question_1_choices},
        question_2: {"choices": question_2_choices},
        question_3: {"choices": question_3_choices},
        question_4: {"choices": question_4_choices},
        question_5: {"choices": question_5_choices},
        question_6: {"choices": question_6_choices}
    }

    # The code below goes through the questions dict, then adds each question,
    # and then adds all the associated choices for that question.
    # if you are using Python 2.x then use questions.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for question, question_data in questions.items():
        q = add_question(question)
        for c in question_data['choices']:
            add_choice(q, c['choice_text'])

    # Print out the questions we have added.
    for q in Question.objects.all():
        for c in Choice.objects.filter(question=q):
            print("- {0} - {1}".format(str(q), str(c)))


def add_choice(q, c_text, votes=0):
    choice = Choice.objects.get_or_create(question=q, choice_text=c_text)[0]
    choice.votes = votes
    choice.save()
    return choice


def add_question(q_text):
    pub_date = timezone.now()
    question = Question.objects.get_or_create(question_text=q_text, pub_date=pub_date)[0]
    question.save()
    return question

# Start execution here!

if __name__ == '__main__':
    print("Starting Polls population script...")
    populate()
