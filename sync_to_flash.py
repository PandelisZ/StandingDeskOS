#!/usr/bin/python3

import os
import shutil
import subprocess
import sys


def ensure_right_os():
    if os.uname().sysname != 'Darwin':
        print('OS not supported yet.')
        sys.exit(1)


def get_mountpoint():
    mounted = False
    mount_result = subprocess.run(['mount'], stdout=subprocess.PIPE, encoding='UTF-8')
    mounts = mount_result.stdout.splitlines()
    for mount in mounts:
        if 'PYBFLASH' in mount:
            mounted = True
            mountpoint = mount.split()[2]

    if not mounted:
        print('PyBoard not mounted')
        sys.exit(2)
    return mountpoint


def get_changed_files():
    changed_files = []
    git_result = subprocess.run(
        ['git', 'status', '--porcelain'],
        stdout=subprocess.PIPE,
        encoding='UTF-8')
    files = git_result.stdout.splitlines()
    for file in files:
        changed_files.append(file.strip().split(maxsplit=1)[1])
    return changed_files


def sync(files, mountpoint):
    for file in files:
        shutil.copy(file, os.path.join(mountpoint, file))


if __name__ == '__main__':
    ensure_right_os()
    mountpoint = get_mountpoint()
    changed_files = get_changed_files()
    sync(changed_files, mountpoint)
