from fabric import task
from datetime import datetime

@task
def do_pack(c):
    """Function to compress files"""
    # Create the versions directory if it doesn't exist
    c.run("mkdir -p versions")

    # Generate the file name with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the tar archive
    result = c.run("tar -cvzf {} web_static".format(archive_path), warn=True)

    # Check if the command was successful
    if result.failed:
        return None
    return archive_path
