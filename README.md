# chatgptmagic

Adds a chatgpt ipython magic command, `%ai`

## Usage

```
pip install --upgrade 'chatgptmagic@git+https://github.com/thingless/chatgptmagic.git'
```

```
OPENAI_API_KEY=YOUR_CHAT_GPT_KEY ipython


In [1]: %load_ext chatgptmagic

In [2]:  %ai "write fizzbuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)                                        
```

Thre are a few magic helpers as well:

* `%aireset` - resets history
* `%aiusage` - shows token usage for last request
* `%aihistory` - shows chat history