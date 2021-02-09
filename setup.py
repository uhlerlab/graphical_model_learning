import setuptools

setuptools.setup(
    name='graphical_model_learning',
    version='0.1a.005',
    description='',
    long_description='',
    author='',
    author_email='',
    packages=setuptools.find_packages(exclude=['tests']),
    python_requires='>3.5.0',
    zip_safe=False,
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    install_requires=[
        'numpy',
        'conditional_independence',
        'graphical_models',
        'tqdm',
        'scipy',
        'matplotlib'
    ]
)

