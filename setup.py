from setuptools import setup, find_packages

setup(
    name='mkdocs-git-show-history-log-plugin',
    version='0.0.1',
    description='MkDocs plugin for showing a history log for a specified markdown file',
    keywords='mkdocs git meta yaml frontmatter',
    url='https://github.com/pawelsikora/mkdocs-git-show-history-log-plugin/',
    author='Pawel Sikora',
    author_email='sikor6@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.1',
        'GitPython',
        'jinja2'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'git-show-history-log = mkdocs_git_show_history_log_plugin.plugin:GitShowHistoryLogPlugin'
        ]
    }
)
