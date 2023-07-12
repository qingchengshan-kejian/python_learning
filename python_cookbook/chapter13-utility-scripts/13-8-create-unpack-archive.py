import shutil

shutil.unpack_archive('python.tgz')

shutil.make_archive('py33', 'zip', 'python3.9')

shutil.get_archive_formats()