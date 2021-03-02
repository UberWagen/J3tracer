
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="Autonomobile",
    version="0.0.1",
    description="Unhitched J3tracer platform",
    long_description=readme(),
    classifiers=[
            "Development Status :: 5 - Prototype",
            "Programming Language :: Python :: 3",
                ],
    url="https://github.com/UberWagen/J3tracer",
    author="CalvinW",
    author_email="calvinwagner92@gmail.com",
    license="MIT",
    install_requires=[
        "Adafruit-Blinka",
        "adafruit-circuitpython-busdevice",
        "adafruit-circuitpython-register",
        "adafruit-circuitpython-pca9685",
        "adafruit-circuitpython-motor",
	"adafruit-circuitpython-framebuf",
        "adafruit-circuitpython-servokit",
        "adafruit-circuitpython-motorkit",
        "adafruit-circuitpython-motor",
        "adafruit-circuitpython-ssd1306",
        "inputs",
        "numpy",
        "nanocamera",
        "Pillow",
        "matplotlib",
    ],
    include_package_data=True,
    zip_safe=False)
