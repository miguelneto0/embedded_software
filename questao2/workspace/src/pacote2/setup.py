from setuptools import setup

package_name = 'pacote2'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Miguel Neto',
    maintainer_email='miguelneto0019@gmail.com',
    description='Pacote para simulação de sensor com filtro de média móvel.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_simulator = pacote2.sensor_simulator:main',
        ],
    },
)
