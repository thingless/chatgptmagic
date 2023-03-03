__version__ = '0.0.1'

from .chatgpt_magic import ChatGptMagic

def load_ipython_extension(ipython):
    ipython.register_magics(ChatGptMagic)