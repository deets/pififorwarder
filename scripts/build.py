#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os
import subprocess
import argparse

import common

def remove_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

def select_tasks(*tasks):
    return "\\|".join(tasks)


def commandline_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    return parser.parse_args()


def check_call(cmd, *args, **kwargs):
    print(" ".join(cmd))
    subprocess.check_call(cmd, *args, **kwargs)


def main():
    args = commandline_arguments()
    config_dir, openadk_dir = common.base_directories()

    task_dir = os.path.join(config_dir, "tasks")
    assert os.path.exists(task_dir), task_dir

    # force re-creation of tasks
    remove_file_if_exists(os.path.join(openadk_dir, ".menu"))
    remove_file_if_exists(os.path.join(openadk_dir, ".config"))

    cmd = [
        "make",
        "ADK_APPLIANCE={}".format(select_tasks("pififorward", "deets")),
        "defconfig"
    ]
    env = {}
    env.update(os.environ)
    env["ADK_CUSTOM_TASKS_DIR"] = task_dir
    env["ADK_TARGET_ARCH"] = "arm"
    env["ADK_TARGET_ARCH_ARM"] = "y"
    env["ADK_TARGET_LINUX_ARCH_ARM"] = "y"
    env["ADK_TARGET_OS_LINUX"] = "y"
    env["ADK_TARGET_OS"] ="linux"
    env["ADK_TARGET_LIBC"] = "glibc"
    env["ADK_TARGET_SYSTEM_RASPBERRY_PI3"] = "y"
    env["ADK_TARGET_SYSTEM"] ="raspberry-pi3"

    if args.verbose:
        cmd.append("ADK_VERBOSE=1")

    check_call(cmd, cwd=openadk_dir, env=env)
    # always clean this to guarantee changes in
    # things like network settings etc
    # are picked up
    check_call(["make", "package=base-files", "clean"], cwd=openadk_dir)
    cmd = ["make"]
    if args.verbose:
        cmd.append("ADK_VERBOSE=1")
    check_call(cmd, cwd=openadk_dir)


if __name__ == '__main__':
    main()
