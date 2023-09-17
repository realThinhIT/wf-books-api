import os
import importlib

# Retrieve current environment, if one is not specified, fallback to 'development'
env = os.getenv('ENVIRONMENT', 'dev')

# Try to import the configurations of that environment
try:
    config = importlib.import_module('app.config.' + env).Config
except ImportError as e:
    raise Exception('Could not find config for the environment: "{}". '
                    'Please correct environment name and try again.'.format(env))
