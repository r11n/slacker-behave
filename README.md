# Slacker
A hook based reporter for behave

## TODOs
* support for `decorators`
* commandline argument support
## Usage
```python
# -- FILE:features/environment.py
import os
import Slacker
def before_all(context):
    context.slacker = Slacker(os.environ('SLACK_WEBHOOK_URL'))
    # do your actions

def after_scenario(context, scenario):
    context.slacker.store(scenario)

def after_all(context):
    context.slacker.generate()
```