from setuptools import setup, find_packages
setup(
    name='unifetch',
    version='0.1.0',
    packages=find_packages(include=["unifetch", "unifetch.*"]),
    package_data={'unifetch': ['crests/*', "universities.json", "ASCII_generator/fonts/*"]},

    install_requires=[
        "numpy==1.22.1",
        "opencv-python==4.5.5.62",
        "Pillow==9.0.1",
    ]
)