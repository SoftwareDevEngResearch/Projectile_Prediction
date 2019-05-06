try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='ProP (Projectile Prediction)',
    version='0.1.0',
    description='Predict projectile requirements through machine learning.',
    author='Levi Coey',
    author_email='coeyl@oregonstate.edu',
    url='http://prop.predict',
    classifiers=[
        'License :: MIT',
        'Intended Audience :: Research',
        'Intended Audience :: Ballistic Testing',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    python_requires='>=3',
    zip_safe=False,
    packages=['ProP', 'ProP.Data', 'ProP.MachLearn', 'ProP.Tests'],
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