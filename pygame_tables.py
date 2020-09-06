"""
Copyright 2020, Rafael Urben, rafaelurben@gmail.com, All rights reserved.

Borrowed from https://github.com/rafaelurben/pygame-tables under the MIT license.
"""

# Imports

import pygame

# Init

pygame.font.init()

# Utility Functions

def to_width(string, length, align=False):
    '''Modify a string to match the given length
    
    :param string: The string to modify
    :param length: The final length
    :param align: Align string left (False) or right (True)
    '''
    string = str(string)
    if len(string) > length:
        return string[:length-2]+".."
    else:
        return string.rjust(length) if align else string.ljust(length)

# Classes

class Table:
    '''Create a table in pygame'''

    def __init__(self, rows, settings, fontsize=12):
        '''
        Create tables in PyGame!

        Example:

        rows = [
            ("Rafael", 16, "Switzerland"),
            ("Someone", 100, "Germany")
        ]

        settings = [
            ("Name",    20, False),
            ("Age",      3, True),
            ("Country", 15, False),
            # (Title, Max length, align (right: True, left: False))
        ]

        table = Table(rows, settings)
        #table.draw(surface, x, y)
        '''

        self.rows = rows
        self.fontsize = fontsize
        self.settings = settings
        self.font = pygame.font.SysFont('Courier', fontsize)

    def draw(self, win, x=10, y=10):
        '''
        Draw the table on a PyGame Surface starting at specified position
        '''

        win.blit(self.font.render(" ".join(to_width(s[0], s[1], s[2]) for s in self.settings), True, (0,0,0)), (x, y))
        y += self.fontsize+3

        for row in self.rows:
            win.blit(self.font.render(" ".join(to_width(row[i], s[1], s[2]) for i, s in enumerate(self.settings)), True, (0,0,0)), (x, y))
            y += self.fontsize+3
