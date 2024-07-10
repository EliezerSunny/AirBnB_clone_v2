from fabric.api import env, run, local
from os import listdir
from os.path import isfile, join

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """Delete out-of-date archives.
    
    Args:
        number (int): The number of archives, including the most recent, to keep.
    """
    number = int(number)
    if number < 1:
        number = 1

    # Local cleanup
    archives = sorted([f for f in listdir("versions") if isfile(join("versions", f))])
    archives_to_delete = archives[:-number]
    with lcd("versions"):
        for archive in archives_to_delete:
            local("rm ./{}".format(archive))

    # Remote cleanup
    releases_path = "/data/web_static/releases"
    run("ls -1t {}/ | grep web_static_".format(releases_path))
    archives = run("ls -1t {}/ | grep web_static_".format(releases_path)).split()
    archives_to_delete = archives[:-number]
    for archive in archives_to_delete:
        run("rm -rf {}/{}".format(releases_path, archive))
