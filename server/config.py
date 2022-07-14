
# Logging configuration.
LOGGING = {
'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'console': {
            'format': ('[%(asctime)s][%(levelname)s] %(name)s '
                       '%(filename)s:%(funcName)s:%(lineno)d | %(message)s'),
            'datefmt': '%H:%M:%S',
        }
    },
    'handlers': {
        'simple': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['simple', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
