import sys

from setuptools import setup
from setuptools import find_packages


version = '0.23.0.dev0'

# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.
install_requires = [
    'acme>=0.21.1',
    'certbot>=0.21.1',
    # 1.5 is the first version that supports oauth2client>=2.0
    'google-api-python-client>=1.5',
    'mock',
    # for oauth2client.service_account.ServiceAccountCredentials
    'oauth2client>=2.0',
    'setuptools',
    'zope.interface',
    # already a dependency of google-api-python-client, but added for consistency
    'httplib2'
]

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-google',
    version=version,
    description="Google Cloud DNS Authenticator plugin for Certbot",
    url='https://github.com/certbot/certbot',
    author="Certbot Project",
    author_email='client-dev@letsencrypt.org',
    license='Apache License 2.0',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-google = certbot_dns_google.dns_google:Authenticator',
        ],
    },
    test_suite='certbot_dns_google',
)