#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os
import sys
import subprocess

import common

FIRMWARE = "firmware/raspberry-pi3_glibc_cortex_a53_hard_eabihf/raspberry-pi3-glibc-archive+kernel.tar.xz"

def main():
    disk = sys.argv[1]
    _, openadk_dir = common.base_directories()
    firmware = os.path.join(openadk_dir, FIRMWARE)
    assert os.path.exists(firmware), firmware

    cmd = [
        "sudo", "scripts/install.sh",
        "-q", # no asking for permission
        "-d",  "500",
        "raspberry-pi3",
        disk,
        firmware,
    ]
    subprocess.check_call(cmd, cwd=openadk_dir)


if __name__ == '__main__':
    main()
