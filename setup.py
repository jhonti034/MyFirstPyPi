from distutils.core import setup
setup(
  name = 'MyFirstPyPi',         # How you named your package folder (MyLib)
  packages = ['MyFirstPyPi'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GPU',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Method takes text file location and returns number of lines',   # Give a short description about your library
  author = 'Shubham Chauhan',                   # Type in your name
  author_email = 'shubham.09.06.90@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/jhonti034/MyFirstPyPi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/jhonti034/MyFirstPyPi/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Python3', 'File_Operation'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'python3',
          ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPL License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
