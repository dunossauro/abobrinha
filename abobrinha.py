from json import dumps
from os.path import abspath


def abobrinha(feature, env_description, output_file='file.json'):
    """
    Generate a json file from feature context.

    Args:
        - feature: the feature argument in behave environment
        - env_description: Description to environment
            (archlinux, bsd, windows ...)
    """
    return _generate_json(_end_feature(feature, env_description))


def _end_feature(feature, env_description):
    return {'feature_name': feature.name,
            'duration': feature.duration,
            'status': feature.status,
            'tags': feature.tags,
            'scenarios': _describe_scenarios(feature.scenarios),
            'environment': env_description}


def _describe_scenarios(scenarios):
    return [{'scenario_name': scenario.name,
             'duration': scenario.duration,
             'status': scenario.status,
             'tags': scenario.tags,
             'steps': _describe_steps(scenario.steps)}
            for scenario in scenarios]


def _describe_steps(steps):
    return [{'step_name': step.name,
             'duration': step.duration,
             'status': step.status}
            for step in steps]


def _generate_json(features_json, filename='file.json'):
    with open(filename, 'w', encoding='utf8') as doc:
        doc.write(dumps(features_json, ensure_ascii=False))
        return '{}: ceated!'.format(abspath('filename'))
