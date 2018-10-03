from setuptools import find_packages, setup

requirement_list = [r.strip()
                    for r in open('requirements.txt', 'r').readlines() if r]

if __name__ == '__main__':
    setup(
          name='dwc',
          version='0.0.1',
          install_requires=requirement_list,
          description='Change your desktop wallpaper daily!',
          long_description=open('README.md').read(),
          python_requires='>=3.5',
          author='ayan-b',
          author_email='ayanbanerjee7777@gmail.com',
          url='https://github.com/ayan-b/Desktop-Wallpaper-Changer',
          license="MIT",
          packages=find_packages(exclude=('tests',)),
    )
