import setuptools

setuptools.setup(
        name = "my_fancy_app",
        version="0.0.1",
        author="Dmitrii Bundin",
        author_email="dbundin@griddynamics.com",
        description="Airflow dataflow",
        long_description="Some long description",
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [ 'hlpth = my_fancy_app.__main__:main' ]
        },
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.7'
)
