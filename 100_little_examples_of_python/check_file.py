# Description      : Check statment added to ensure correct file closure

from __future__ import print_function  #__future__ 把下一个版本的特性导入到当前版本
import sys
import os

# Prints usage if not appropriate length of arguments are provide


def usage():
    print('[-]Usage: python check_file.py [filename1] [filename2] ... [filenameN]')
    
# Read Functions which open the file that is passed to the script

def readfile(filename):
    with open(filename, 'r') as f:   # with ... as 语句，自带打开和关闭功能，应该是常用语文件的打开的。
        file = f.read()
    print(file)
    print()
    print('#'*80)
    print()


def main():
    # Check the arguments passed to the script
    if len(sys.argv) >= 2:  # python2 和 python3 中应该有所区别，程序的参数从argv改成sys.argv
        filenames = sys.argv[1:]  # 第0个参数是程序本身，从1开始的参数是实际输入的运行参数
        filteredfilenames_1 = list(filenames) #To counter changing in the same list which you are iterating  #list()方法，将元组转换成列表
        filteredfilenames_2 = list(filenames)
        # Iterate for each filename passed in command line argument
        for filename in filteredfilenames_1:
            if not os.path.isfile(filename):  # os.path.isfile os模块中的方法，用来判定文件是否存在
                print('[-] ' + filename + ' does not exist.')
                filteredfilenames_2.remove(filename) #remove non existing files from fileNames list  #remove方法，从列表中删除元素
                continue
            # Check you can read the file
            if not os.access(filename, os.R_OK): # os.access 判断文件权限
                print('[-] ' + filename + ' access denied')
                #remove non readable fileNames
                filteredfilenames_2.remove(filename)
                continue
        # Read the content of each file that both exists and is readable
        for filename in filteredfilenames_2:
            # Display Message and read the file contents
            print('[+] Reading from : ' + filename)
            readfile(filename)  #调用已定义的函数
    else:
        usage() #Print usage if not all paraments passd/Checked


if __name__ == '__main__':
    main()  #调用已定义的函数
