#!/usr/bin/python3 -u
import sys
import os
import os.path
import subprocess
import urllib.parse

_BASE_DIR = "/srv/ctf/gctf/"
_REPO_DIR = os.path.join("/srv/ctf/gctf/", "qwe")


def encode_repo_url(repo_url):
  return urllib.parse.quote(repo_url, safe='').replace('.', '%2e')


def build_repo_dir(repo_url):
  return os.path.join(_BASE_DIR, encode_repo_url(repo_url))

filepath = sys.argv[1]

real_filepath = os.path.realpath(os.path.join(_REPO_DIR, filepath))
print(real_filepath)
print(os.path.commonpath((_REPO_DIR, real_filepath)))
print(_REPO_DIR)
print(_REPO_DIR != os.path.commonpath((_REPO_DIR, real_filepath)))
print(subprocess.run(["cat", real_filepath], capture_output=True))
