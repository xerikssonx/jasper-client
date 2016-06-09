# -*- coding: utf-8-*-

import re

WORDS = ["ALARM"]

_numbers_ = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
             'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
             'thirty', 'forty', 'fifty']

_time_ = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
          'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
          'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50}


def handle(text, mic, profile):
    mic.say("I am starting to set up alarm clock")
    hour = get_hour(mic)
    minute = get_minute(mic)



def get_hour(mic):
    valid = False
    hour_result = 0
    while not valid:
        mic.say("Please set hours")
        hour = mic.activeListen()
        hour_array = hour.split()
        for item in hour_array:
            if item in _numbers_:
                hour_result += _time_.get(item)
                valid = True
            else:
                mic.say("Error")
                valid = False
                hour_result = 0
                break
    if hour_result > 23:
        valid = False
        hour_result = 0
        mic.say("Error")
        return get_hour(mic)
    return hour_result


def get_minute(mic):
    valid = False
    minute_result = 0
    while not valid:
        mic.say("Please set minutes")
        minute = mic.activeListen()
        minute_array = minute.split()
        for item in minute_array:
            if item in _numbers_:
                minute_result += _time_.get(item)
                valid = True
            else:
                mic.say("Error")
                valid = False
                minute_result = 0
                break

    if minute_result > 23:
        valid = False
        minute_result = 0
        mic.say("Error")
        return get_minute(mic)
    return minute_result


def isValid(text):
    return bool(re.search(r'\balarm\b', text, re.IGNORECASE))