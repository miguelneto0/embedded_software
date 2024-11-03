from setuptools import setup

package_name = 'pacote1'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Miguel Neto',
    maintainer_email='miguelneto0019@gmail.com',
    description='Pacote ROS 2 em Python para publicação de informações de memória.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mem_publisher = pacote1.mem_publisher:main',  # Executável para o nó mem_publisher
        ],
    },
)
