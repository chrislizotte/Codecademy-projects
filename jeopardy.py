import pandas as pd
import re
import numpy as np

pd.set_option('display.max_colwidth', None)

jeopardy = pd.read_csv('jeopardy.csv')

# rename columns to remove whitespace
jeopardy.rename(columns={'Show Number': 'show_number', ' Air Date': 'airdate', ' Round': 'show_round', ' Category': 'category', ' Value': 'value', ' Question': 'question', ' Answer': 'answer'}, inplace=True)

# jeopardy.reset_index()
# print(jeopardy.columns)
# missing_values = jeopardy[jeopardy.value == 'None']
# print(missing_values.show_round.head())
# print(missing_values.value.head())

# create a numeric value column
ignore_none = lambda value:'0' if value == 'None' else value
jeopardy['value_numeric'] = pd.to_numeric(jeopardy.value.apply(ignore_none).replace(r'[\$,]', '', regex=True).replace(r'[\,]', '', regex=True))

# print(jeopardy.value_numeric.head())

# should return 152 rows with filter_questions
sample_list = ['england', 'king']

def filter_questions(string_list):
    filter = lambda question : all(string.lower() in question.lower() for string in string_list)
    return jeopardy[jeopardy.question.apply(filter)]

# this version uses a regex expression to only match whole words, not substrings
def filter_questions_regex(string_list):
    filter = lambda question : all(re.search(r'\b' + string.lower() + r'\b', question.lower()) for string in string_list)
    return jeopardy[jeopardy.question.apply(filter)]

def calculate_average(string_list):
    # select questions containing strings in list
    selection = filter_questions_regex(string_list)
    # exclude Final Jeopardy! questions with a value of 0
    selection = selection[selection.value_numeric > 0]
    return selection.value_numeric.mean()

# find unique answers for questions selected by strings from a list
def unique_answers(string_list):
    selection = filter_questions_regex(string_list)
    return len(selection.answer.unique())

# find most common answer for questions selected by strings from a list
def most_common_answer(string_list):
    selection = filter_questions_regex(string_list)
    answers = selection.groupby('answer').show_number.count().reset_index()
    return answers[answers.show_number == answers.show_number.max()].rename(columns={'show_number': 'frequency'})

def filter_by_decade(string_list):
    selection = filter_questions_regex(string_list)
    selection['year'] = pd.to_numeric(selection.airdate.str[:4])
    # this didn't work for some reason
    # selection['decades'] = np.select(condlist=[selection.year >= 1980 and selection.year < 1990, selection.year >= 1990 and selection.year < 2000, selection.year >= 2000 and selection.year < 2010, selection.year >= 2010 and selection.year < 2020], choicelist=['1980s', '1990s', '2000s', '2010s'], default='1970s')
    # this did work; but I was unwittingly letting years ending in 0 fall in the cracks by only using < and not <=
    selection['decades'] = selection.year.apply(lambda year:(1970 <= year < 1980 and '1970s') or (1980 <= year < 1990 and '1980s') or (1990 <= year < 2000 and '1990s') or (2000 <= year < 2010 and '2000s') or (2010 <= year < 2020 and '2010s'))
    decade_frame = selection.groupby('decades').question.count().reset_index()
    return decade_frame
