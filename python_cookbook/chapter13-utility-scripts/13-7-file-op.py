import shutil

shutil.copy(src, dst) # cp
shutil.copy2(src, dst) # cp -p preserve metadata
shutil.copytree(src, dst) # cp -R
shutil.move(src, dst) # mv
