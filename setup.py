from setuptools import setup, find_packages

setup(
    name='morning_greetings',                    # Name of the package
    version='1.0.0',                             # Version of your package
    description='A package to send personalized morning greetings',  # Short description
    author='Hamid Hamrah',                         
    author_email='s362052@oslomet.no',    
    packages=find_packages(),                    # Automatically find and include all packages
    entry_points={                               # Optional: Define command-line scripts
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main'
        ]
    },
    classifiers=[                                # Additional metadata (optional but recommended)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                     # Minimum Python version required
)


