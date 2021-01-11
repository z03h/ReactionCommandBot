import re
from setuptools import setup

requirements = ["discord.py>=1.6.0,<1.7.0"]

version = ''
with open('discord/ext/reactioncommands/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

setup(name='dpy-reactionbot',
      author='z03h',
      url='https://github.com/z03h/ReactionCommandBot',
      version=version,
      packages=['discord.ext.reactioncommands'],
      license='MIT',
      description='discord.py extension that adds reaction commands',
      install_requires=requirements,
      python_requires='>=3.6.4'
)
