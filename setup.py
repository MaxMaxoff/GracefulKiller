import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'GracefulKiller',
  version = '0.4.6',
  license = 'MIT',
  author = 'Maxim Toropov',
  author_email = 'maxim.vt@gmail.com',
  description = "module for process SIGTERM, SIGHUP and SIGINT signals gracefully",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/MaxMaxoff/GracefulKiller',
  download_url = 'https://github.com/MaxMaxoff/GracefulKiller/archive/v_04.tar.gz',
  keywords = ['SIGTERM', 'SIGINT', 'SIGHUP', 'GracefulKiller', 'Killer', 'Graceful'],
  install_requires = [
      ],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  package_dir={'': 'src'},
  packages=setuptools.find_packages(where="src"),
  python_requires=">=3.6"
)