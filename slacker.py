import os
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
        requests.post(
            self.webhook,
            data=json.dumps({
                'text': f'Automation report\n*passed*:{passed}\n*failed*:{failed}\ndetailed Report:',
                'attachments': self.slack_data
            }),
            headers={'Content-Type': 'application/json'}
        )
    
    def slackify(self, scenario):
        return {
            'fallback': f'Scenario: {scenario.name}',
            'color': '#36a64f' if scenario.status == 'passed' else '#e01e5a',
            'pretext': scenario.feature.name,
            'author_name': 'Slacker',
            'title': scenario.name,
            'text': f'runtime: {scenario.duration}  status: {scenario.status}',
            'ts': time.time()
        }
