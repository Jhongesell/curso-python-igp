#!/usr/bin/env python
# -*- coding: utf8 -*-

import re

MINIMAL_PASSWORD_LENGTH = 8

REGEX_UPPERCASE = r'[A-Z]'
REGEX_LOWERCASE = r'[a-z]'
REGEX_DIGIT = r'[0-9]'
REGEX_SYMBOL = r'[^\w]'

SCORING_CRITERIA = (
    ('HAS_UPPERCASE', 0.1),
    ('HAS_LOWERCASE', 0.1),
    ('HAS_DIGIT', 0.1),
    ('HAS_SYMBOL', 0.1),
    ('HAS_MINIMAL_LENGTH', 0.1),
    ('ADDITIONAL_CHARACTER', 0.01),
    ('ADDITIONAL_UPPERCASE', 0.02),
    ('ADDITIONAL_LOWERCASE', 0.0),
    ('ADDITIONAL_DIGIT', 0.02),
    ('ADDITIONAL_SYMBOL', 0.03),
)

SCORE_RANGES = (
    (0.00, u'Insuficiente'),
    (0.50, u'Buena'),
    (0.60, u'Muy buena'),
    (0.70, u'Excelente'),
    (0.80, u'Experto')
)

class PasswordAnalyzerError(Exception):
    pass

class PasswordAnalyzer(object):

    def __init__(self, password=None):
        self.set_password(password)

    def set_password(self, password):
        self.password = password

    def has_password(self):
        return self.password is not None

    def raise_if_no_password(self):
        if not self.has_password():
            raise PasswordAnalyzerError('No password to analyze!')

    def get_password_length(self):
        return len(self.password) if self.password is not None else 0

    def has_minimal_password_length(self):
        return self.get_password_length > MINIMAL_PASSWORD_LENGTH

    def get_additional_character_count(self, after=None):
        if after is None:
            after = MINIMAL_PASSWORD_LENGTH
        count = self.get_password_length() - after
        return count if count > 0 else 0

    def get_chars(self, regexp):
        return re.findall(regexp, self.password)

    def get_char_count(self, regexp, after=0):
        return len(self.get_chars(regexp)) - after

    def get_uppercase_letters(self):
        return self.get_chars(REGEX_UPPERCASE)

    def get_uppercase_count(self, after=0):
        return self.get_char_count(REGEX_UPPERCASE, after)

    def has_uppercase(self):
        return self.get_uppercase_count() > 0

    def get_lowercase_letters(self):
        return self.get_chars(REGEX_LOWERCASE)

    def get_lowercase_count(self, after=0):
        return self.get_char_count(REGEX_LOWERCASE, after)

    def has_lowercase(self):
        return self.get_uppercase_count() > 0

    def get_digits(self):
        return self.get_chars(REGEX_DIGIT)

    def get_digit_count(self, after=0):
        return self.get_char_count(REGEX_DIGIT, after)

    def has_digit(self):
        return self.get_digit_count() > 0

    def get_symbols(self):
        return self.get_chars(REGEX_SYMBOL)

    def get_symbol_count(self, after=0):
        return self.get_char_count(REGEX_SYMBOL, after)

    def has_symbol(self):
        return self.get_uppercase_count() > 0

    def get_initial_score(self):
        return 0.0

    def truncate_score(self, score):
        return score if score <= 1.0 else 1.0

    def get_score(self):
        self.raise_if_no_password()
        scoring_criteria = dict(SCORING_CRITERIA)
        score = self.get_initial_score()
        if self.has_minimal_password_length():
            score += scoring_criteria['HAS_MINIMAL_LENGTH']
        if self.has_uppercase():
            score += scoring_criteria['HAS_UPPERCASE']
        if self.has_lowercase():
            score += scoring_criteria['HAS_LOWERCASE']
        if self.has_digit():
            score += scoring_criteria['HAS_DIGIT']
        if self.has_symbol():
            score += scoring_criteria['HAS_SYMBOL']
        count = self.get_additional_character_count(after=1)
        score += count * scoring_criteria['ADDITIONAL_CHARACTER']
        count = self.get_uppercase_count(after=1)
        score += count * scoring_criteria['ADDITIONAL_UPPERCASE']
        count = self.get_lowercase_count(after=1)
        score += count * scoring_criteria['ADDITIONAL_LOWERCASE']
        count = self.get_digit_count(after=1)
        score += count * scoring_criteria['ADDITIONAL_DIGIT']
        count = self.get_symbol_count(after=1)
        score += count * scoring_criteria['ADDITIONAL_SYMBOL']
        return score

    def get_score_description(self, score=None):
        if score is None:
            score = self.get_score()
        candidate = SCORE_RANGES[0][0]
        for minimum, description in SCORE_RANGES:
            if score >= minimum:
                candidate = description
            else:
                break
        return candidate


if __name__ == '__main__':
    password = ''
    while len(password) == 0:
        password = raw_input('Ingrese una contraseña: ').strip()
    analyzer = PasswordAnalyzer(password)
    print "Score obtenido: %.2f (%s)" % (
        analyzer.get_score(),
        analyzer.get_score_description()
    )
