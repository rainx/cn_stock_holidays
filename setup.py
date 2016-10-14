from setuptools import setup, find_packages

setup(
    name = "cn-stock-holidays",
    version = "0.3",
    packages = find_packages(),
    install_requires=[
        'requests'
    ],

    # metadata for upload to PyPI
    author="rainx",
    author_email="i@rainx.cn",
    description="A List of china stock exchange holidays",
    license="MIT",
    keywords="china stock holiday exchange shanghai shenzhen",
    url="https://github.com/zhikuang/cn_stock_holidays.git",  # project home page, if any

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt'],
    },
    entry_points={
        'console_scripts': [
            'cn-stock-holiday-sync=cn_stock_holidays.data:sync_data',
        ]
    }
)
