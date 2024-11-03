from setuptools import setup

package_name = 'pacote3'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Miguel Neto',
    maintainer_email='miguelneto0019@gmail.com',
    description='Pacote para busca do décimo número primo usando uma ação.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'primo_action_server = pacote3.primo_action_server:main',
        ],
    },
)