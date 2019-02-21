"""
    My thought process here. I need to do several tasks, I will work through them one by one.
    I will also need to find some external web scrapping libraries to do some of them.
    Web scraping : beautifulsoup4 (import bs4)
    Interacting with website : selenium

    The begin() function will not only sign into websites, but also get the respective data from a url in the terminal.
    Getting data is second priority, to be focused on later, primary focus to open and sign into links.
"""

from authenticate import Websites
from get_data import Data
from helpers import convert_to_command as ctc, command_to_link as ctl
from helpers import input_commands


class Jarvis:
    
    def __init__(self):
        self.website = Websites()
        self.data = Data()
        self.cmd = ''

    def begin(self, cmd):
        # TODO : for any media command passed, sign in, then wait for other commands which refer to other functions
        self.cmd = cmd
        url = ctl(ctc(self.cmd))        # desired link from the prompt
        self.website.sign_in(url)       # open AND sign in
        self.data.get_from(ctc(cmd))


def format_print(cmd = None):
    if cmd is None or cmd not in input_commands.keys():
        print('\nPlease pass in a valid command')
        return
    print(f'Command that was passed: {ctc(cmd)}')


if __name__ == '__main__':
    Bot = Jarvis()
    print('\nYou have initiated Jarvis. Pass in a valid command to sign into a media and open the browser with it.')
    print('\nPass in \'e\' or \'end\' to terminate the program.')
    cmd = input('\nEnter your command here: ')
    while cmd is None or cmd not in input_commands.keys():
        format_print()
        cmd = input('\nEnter your command here: ')
    while cmd.lower() != 'end' and cmd.lower() != 'e':
        format_print(cmd)
        Bot.begin(cmd)
        cmd = input('\nEnter your command here: ')
    print('\nThank you for using Jarvis.\nExecution terminated.')
