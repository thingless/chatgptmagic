__version__ = '0.0.1'

import os
import sys
from .chatgpt_magic import ChatGptMagic

def load_ipython_extension(ipython):
    if not os.getenv('OPENAI_API_KEY'):
        print('you must specify "OPENAI_API_KEY" enviroment variable to make ai magic work', file=sys.stderr)
    ipython.register_magics(ChatGptMagic)