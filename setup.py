try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='ProP',
    version='1.0.2',
    description='Predict projectile requirements through machine learning.',
    author='Levi Coey',
    author_email='coeyl@oregonstate.edu',
    url='https://github.com/coeyl/Projectile_Prediction',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        #'Intended Audience :: Research',
        #'Intended Audience :: Ballistic Testing',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3',
    zip_safe=False,
    packages=['ProP', 'ProP.Data', 'ProP.Tests'],
    # or find automatically:
#    package=find_packages(),
#    package_dir={
#        'ProP': 'ProP',
#        'ProP.Data': 'ProP/Data',
#        'ProP.MachLearn': 'ProP/MachLearn',
#        'ProP.Tests': 'ProP/Tests',
#        },
    include_package_data=True,
)
