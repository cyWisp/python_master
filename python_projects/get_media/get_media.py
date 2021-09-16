#!/usr/bin/env python
from sys import argv
from classes import ScriptArgs
from functions import get_command, run_youtube_dl

if __name__ == '__main__':
    script_args = ScriptArgs(argv)
    script_args.validate()

    run_youtube_dl(get_command(script_args))
    
