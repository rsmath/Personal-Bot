'''
    This module provides some helpful functionst to parse commands from prompt
'''

def convert_to_command(comm):
    commands = {"t" : 'twitter',
                "twitter" : 'twitter',
                'insta' : 'instagram',
                'instagram' : 'instagram',
                'i' : 'instagram',
                "g" : 'github',
                "git" : 'github',
                "github" : 'github',
                "k" : 'kaggle',
                "kaggle" : 'kaggle',
                "mail" : 'mail',
                "email" : 'mail',
                "m" : 'mail',
                "xkcd" : 'xkcd',
                "x" : 'xkcd',
                "xk" : 'xkcd',
                "s" : 'school',
                "school" : 'school'
               }
    return commands[comm.lower()]