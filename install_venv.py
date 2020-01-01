#!/usr/bin/env python3

import os
import subprocess
import argparse
import venv

def create_venv(path):
    venv.EnvBuilder(with_pip=True, symlinks=True).create(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--env-path", help = "Root path for the environment", type=str, required=True)
    args = parser.parse_args()
    env_path = args.env_path
    create_venv(env_path)
    project_root = os.path.dirname(os.path.realpath(__file__))
    proc = subprocess.Popen(["/bin/bash", "-c", f"""
                    source {env_path}/bin/activate;
                    cd {project_root};
                    echo {project_root};
                    python -m pip install wheel;
                    python -m pip install -r requirements.txt;
                    python setup.py install bdist_wheel"""]).communicate()
