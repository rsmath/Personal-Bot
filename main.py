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

    def begin(self, passed_cmd, choice='website'):
        # TODO : for any media command passed, sign in, then wait for other commands which refer to other functions
        self.cmd = passed_cmd
        url = ctl(ctc(self.cmd))  # desired link from the prompt
        # choosing between signing in or getting the data
        if choice is None or choice.lower() == 'website':
            self.website.sign_in(url)  # open AND sign in

        elif choice.lower() == 'data':
            self.data.get_from(ctc(passed_cmd))


def format_print(command=None):
    if command is None or command not in input_commands.keys():
        print('\nPlease pass in a valid command. Read the instructions again.')
        return

    print(f'Command that was passed: {ctc(command)}')


if __name__ == '__main__':
    '''
    This place so that user would be able to chose between opening or getting data
    '''
    Bot = Jarvis()
    print('\nYou have initiated Jarvis. Pass in a valid command to sign into a media and open the browser with it.')
    print('Pass in \'sign in\' or \'open\' or nothing at all to sign into the websites.\nPass in \'get data\' or '
          '\'data\' to obtain the data from the forums.')

    cmd = input('\nEnter your choice here: ')
    flag = None  # holds whether the param is to sign in or get the data
    while cmd is not None and cmd != '':  # not empty and not None, meaning a typo
        if cmd.lower().replace(' ', '') == 'signin' or cmd.lower().replace(' ', '') == 'open':  # removing the spaces
            flag = 'website'
            break
        elif cmd.lower().replace(' ', '') == 'getdata' or cmd.lower().replace(' ', '') == 'data':  # removing spaces
            flag = 'data'
            break
        else:
            print(f'\nSorry, the choice: \'{cmd.lower()}\' was not recognized. Please try again.')
            cmd = input('\nEnter your choice here: ')
            continue

    if cmd is not None and flag == 'website':
        print('\nYou have chosen to sign into websites by passing None into the choice above. To change that choice,'
              'please terminate and restart the program')

    cmd = input('Would you like to see the available commands: ')
    print('\nYou can now pass in your commands.\nPass in \'e\' or \'end\' to terminate the program.')
    cmd = input('\nEnter your command here: ')
    while cmd is None or cmd not in input_commands.keys():
        format_print()
        cmd = input('\nEnter your command here: ')

    while cmd.lower() != 'end' and cmd.lower() != 'e':
        format_print(cmd)
        Bot.begin(cmd, choice=flag)
        cmd = input('\nEnter your command here: ')

    print('\nThank you for using Jarvis.\nExecution terminated.')
