from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="Autonomobile",
    version="0.0.1",
    description="Unhitched J3tracer platform",
    long_description=readme(),
    long_description_content_type="text/markdown",
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
        "adafruit-circuitpython-servokit",
        "adafruit-circuitpython-motorkit",
        "adafruit-circuitpython-motor",
        "adafruit-circuitpython-ssd1306",
        "inputs",
        "numpy",
        "libcanberra-gtk-module",
        "nanocamera",
        "Pillow",
        "matplotlib",
        "libtiff5-dev",
        "libjpeg8-dev",
        "zlib1g-dev",
        "libfreetype6-dev",
        "liblcms2-dev",
        "libwebp-dev",
        "libharfbuzz-dev",
        "libfribidi-dev",
        "tcl8.6-dev",
        "tk8.6-dev",
        "python-tk",
    ],
    include_package_data=True,
    zip_safe=False)
