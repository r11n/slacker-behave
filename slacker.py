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
        for i in self.scenarios:
            self.slack_data.append(self.slackify(i))
        requests.post(
            self.webhook,
            data=json.dumps(self.slack_data),
            headers={'Content-Type': 'application/json'}
        )
    
    def slackify(self, scenario):
        return {
            'fallback': f'Scenario: {scenario.name}',
            'color': '#36a64f' if scenario.status == 'passed' else '#e01e5a',
            'pretext': scenario.name,
            'author_name': 'Slacker',
            'title': scenario.name,
            'text': f'runtime: {scenario.duration}  status: {scenario.status}',
            'ts': time.time()
        }
