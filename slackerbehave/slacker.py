import requests
import json
import time
class Slacker:
    def __init__(self, webhook):
        self.scenarios = []
        self.webhook = webhook
        self.slack_data = []



    def store(self, scenario):
            self.scenarios.append(scenario)



    def generate(self):
            passed = 0
            failed = 0
            for i in self.scenarios:
                if i.status == 'passed':
                    passed += 1
                else:
                    failed += 1
                self.slack_data.append(self.slackify(i))
            summary = f'\n*total*:{len(self.scenarios)}\n*passed*:{passed}\n*failed*:{failed}\n'
            requests.post(
                self.webhook,
                data=json.dumps({
                    'text': f'Automation report{summary}detailed Report:',
                    'attachments': self.slack_data
                }),
                headers={'Content-Type': 'application/json'}
            )


    def slackify(self, scenario):
            return {
                'fallback': f'Scenario: {scenario.name}',
                'color': '#36a64f' if scenario.status.name == 'passed' else '#e01e5a',
                'pretext': scenario.feature.name,
                'author_name': scenario.name,
                'title': f'runtime: {round(scenario.duration)} Sec  status: {scenario.status.name}\nSteps:',
                'text': self.step_describe(scenario.steps),
                'ts': time.time()
            }


    def step_describe(self, steps):
            return ''.join(list(
                map(
                    lambda x: f'*`{x.status.name}`* - *_{x.name}_*\n',
                    steps
                )
            ))
