import openai
import re
import traceback
import sys
from IPython.core.magic import (Magics, magics_class, line_cell_magic, line_magic, cell_magic, needs_local_scope)

from rich.console import Console
from rich.markdown import Markdown

console = Console()

@magics_class
class ChatGptMagic(Magics):

    def __init__(self, shell):
        # You must call the parent constructor
        super(ChatGptMagic, self).__init__(shell)
        self.system_message = "You are a helpful assistant. Do not provide an explanation. Unless specified otherwise, assume the user is talking about the python programming language."
        self.aireset()
        self.last_usage = None

    @line_magic
    def aireset(self, line=None):
        self.history = [
            {"role": "system", "content": self.system_message},
        ]

    @line_magic
    def aisystem(self, line=None):
        if line:
            self.system_message = line.strip()
        else:
            console.print(self.system_message)

    @line_magic
    def aiusage(self, line):
        return self.last_usage

    @line_magic
    def aihistory(self, line):
        return self.history

    @line_magic
    def aifix(self, line=None):
        if not getattr(sys, 'last_type', None):
            return
        txt = traceback.format_exception(sys.last_type, sys.last_value, sys.last_traceback)
        self.ai("""Fix the exception:
```
{}
```""".format(txt))

    @line_magic
    def aifixexec(self, line=None):
        if not getattr(sys, 'last_type', None):
            return
        self.aifix()
        self.aiexec()

    def _get_last_code_block(self):
        try:
            txt = self.history[-1]['content']
            blocks = list(re.finditer(r'(?mis)```(.*?)```', txt))
            return blocks[-1].group(1).strip()
        except Exception:
            #raise
            return None

    @line_cell_magic
    def aiexec(self, line=None, cell=None):
        if line or cell:
            self.ai(line, cell)
        cb = self._get_last_code_block()
        if cb:
            exec(cb, self.shell.user_ns)

    @line_cell_magic
    def ai(self, line, cell=None):
        "Magic that works both as %cg and as %%cg"
        if cell is None:
            user_msg = line
        else:
            user_msg = cell
        self.history.append({"role":"user", "content":user_msg})
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history
        )
        ass_msg = res['choices'][0]['message']['content']
        self.history.append({"role":"assistant", "content":ass_msg})
        self.last_usage = res['usage']
        console.print(Markdown(ass_msg))
