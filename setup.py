from setuptools import setup, find_packages

setup(
    name='mock_queryset',
    version='0.0.1',
    description='fake a Django queryset with Mock',
    author='Alex Dreyer, Greg Meno, Alfredo Deza',
    author_email='opensource@coxinc.com',
    license='MIT',
    url='https://github.com/adreyer/mock-queryset',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'mock',
        'pytest'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

