from json import dumps


class Abobrinha:
    def __init__(self, context):
        self.context = context
        self.features = []
        self.atts = ['Name', 'Duration', 'Status']

    def end_feature(self, feature):
        self.features.append(
            {'Feature_name': feature.name,
             'Duration': feature.duration,
             'Status': feature.status,
             'Tags': feature.tags,
             'Scenarios': self._describe_scenarios(feature.scenarios)})

    def _describe_scenarios(self, scenarios):
        return [{'Scenario_name': scenario.name,
                 'Duration': scenario.duration,
                 'Status': scenario.status,
                 'Tags': scenario.tags,
                 'Steps': self._describe_steps(scenario.steps)}
                for scenario in scenarios]

    def _describe_steps(self, steps):
        return [{'Step_name': step.name,
                 'Duration': step.duration,
                 'Status': step.status}
                for step in steps]

    def generate_json(self):
        with open('file.json', 'w') as doc:
            doc.write(dumps(self.features))
