#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os
import subprocess

def remove_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

def main():
    openadk_dir = os.path.join(
        os.path.dirname(__file__),
        "..", "modules", "openadk",
    )
    assert os.path.exists(openadk_dir), openadk_dir
    config_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..", "config",
        )
    )
    assert os.path.exists(config_dir), config_dir

    task_dir = os.path.join(config_dir, "tasks")
    assert os.path.exists(task_dir), task_dir

    # force re-creation of tasks
    remove_file_if_exists(os.path.join(openadk_dir, ".menu"))
    remove_file_if_exists(os.path.join(openadk_dir, ".config"))

    cmd = [
        "make",
        "ADK_APPLIANCE={}".format("pififorward"),
        "defconfig"
    ]
    env = {}
    env.update(os.environ)
    env["ADK_VERBOSE"] = "1"
    env["ADK_CUSTOM_TASKS_DIR"] = task_dir
    env["ADK_TARGET_ARCH"] = "arm"
    env["ADK_TARGET_ARCH_ARM"] = "y"
    env["ADK_TARGET_LINUX_ARCH_ARM"] = "y"
    env["ADK_TARGET_OS_LINUX"] = "y"
    env["ADK_TARGET_OS"] ="linux"
    env["ADK_TARGET_SYSTEM_RASPBERRY_PI3"] = "y"
    env["ADK_TARGET_SYSTEM"] ="raspberry-pi3"
    subprocess.check_call(cmd, cwd=openadk_dir, env=env)


if __name__ == '__main__':
    main()
