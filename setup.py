from distutils.core import setup
setup(
    name = 'slackerbehave',
    packages = ['slackerbehave'],
    version = '0.0.6',
    license = 'MIT',
    description = 'A slack report generator for behave using the behave hooks',
    author = 'raghavendranekkanti',
    author_email = 'raghavendra.nekkanti@inmar.com',
    url = 'https://github.com/raghavendranekkanti/slacker-behave',
    download_url = 'https://github.com/raghavendranekkanti/slacker-behave/archive/0.0.6.tar.gz',
    keywords = ['slack-webhook', 'behave-reports', 'reports', 'behave', 'slack'],
    install_requires = [
        'requests'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
