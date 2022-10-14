# mempw

## Description
Memorable password generator in Python

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

[![xkcd "Password Strength" comic](https://imgs.xkcd.com/comics/password_strength.png "https://xkcd.com/936/")](https://xkcd.com/936/)

## Installation
Github:
```bash
git clone https://github.com/mdvthu/mempw
pip3 install ./mempw
```
PyPI:
```bash
pip3 install mempw
```

## Configuration
Edit `mempw/config.py` to customise settings

## Wordlist
Uses system (Linux/Unix) wordlists and [SCOWL](https://sourceforge.net/projects/wordlist/files/speller/2020.12.07/)
online wordlists. More information can be found in `config.py`.

## Usage
Command line interface, `mempw`, generates a new password using the
default configuration settings.
