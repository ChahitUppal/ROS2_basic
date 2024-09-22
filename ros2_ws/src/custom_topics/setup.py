from setuptools import setup

package_name = 'custom_topics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Python-based ROS 2 package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'target_publisher = custom_topics.target_publisher:main',
            'solution_publisher = custom_topics.solution_publisher:main',
            'data_publisher = custom_topics.data_publisher:main',
        ],
    },
)