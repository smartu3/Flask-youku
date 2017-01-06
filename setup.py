from setuptools import setup,find_packages

setup(
	name='Flask-Youku',
	version='0.1',
	license='MIT',
	description='Flask extension to allow easy embedding of Youku videos',
	author='ZZJ',
	author_email='zhze93@qq.com',
	platforms='any',
	install_requires=['Flask'],
	packages=find_packages()
	)