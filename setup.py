from setuptools import setup, find_packages

setup(
    name = "cn-stock-holidays",
    version = "0.1",
    author= 'RainX',
    description='ingest zipline databundle source for chinese market',
    packages = find_packages(),
    install_requires=[
        'requests'
    ],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt'],
    },
    entry_points={
        'console_scripts': [
            'cn-stock-holidy-sync=cn_stock_holidays.data:sync_data',
        ]
    }
)