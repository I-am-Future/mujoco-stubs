from setuptools import setup

setup(
    name='mujoco-stubs',
    author="Lai Wei",
    author_email="law016@ucsd.edu",
    description="PEP 561 type stubs for mujoco-stubs",
    version='1.0',
    packages=['mujoco-stubs'],
    package_data={"mujoco-stubs": ['mujoco.pyi', '__init__.pyi']},
)