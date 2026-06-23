import subprocess


def git_status():
    return subprocess.run(["git", "status"], shell=False, check=False)
