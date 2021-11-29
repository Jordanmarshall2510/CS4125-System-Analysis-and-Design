from setuptools import find_packages
from distutils.core import setup

setup(  name='Smart City Simulation',
        version='1.0',
        description='A smart city simulation for CS4125 System Analysis and Design.',
        author='Jordan Marshall, Marcin Sek, Jakub Pazej, Eoin McDonough, Aleksandr Jakusev',
        url='https://github.com/Jordanmarshall2510/CS4125---System-Analysis-and-Design',
        packages= find_packages('.'),
        include_package_data=True,
        package_data= {'Server': ['config.json']},
        install_requires=[
            'dash',
            'plotly',
            'numpy',
            'pandas',
            'dash-bootstrap-components',
        ],

    )
