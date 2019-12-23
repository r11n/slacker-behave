# Slacker
A hook based reporter for behave

## TODOs
* support for `decorators`
* commandline argument support
## Usage
```python
# -- FILE:features/environment.py
import os
import slackerbehave import Slacker
def before_all(context):
    context.slacker = Slacker(os.environ('SLACK_WEBHOOK_URL'))
    # do your actions

def after_scenario(context, scenario):
    context.slacker.store(scenario)

def after_all(context):
    context.slacker.generate()
```
## Testing without Behave
Make sure you import `Scenario` and `Feature` from the `scenario.py`
```python
# -- FILE:test.py
import os
from slackerbehave import Slacker
from slackerbehave import SFeature, SStatus, SScenario

slacker = Slacker(os.environ['SLACK_WEBHOOK_URL'])
slacker.store(SScenario('scene1', 'passed', 'feature1', 10))
slacker.store(SScenario('scene2', 'passed', 'feature1', 10))
slacker.store(SScenario('scene3', 'failed', 'feature1', 10))
slacker.store(SScenario('scene1', 'passed', 'feature2', 10))
slacker.generate()
# should generate a report and send to it corresponding channel or chat in webhook url
# report will look similar to following comments

# total:1
# passed:1
# failed:0
# detailed Report:
# feature1
# || scene1
# || passed
# || runtime: 10  status: passed
# || Today at 3:02 PM
```