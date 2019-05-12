#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
sdr_set = []
# 先把所有以.sdr结尾的文件夹找到,放到set中
for root, dirs, files in os.walk("/Volumes/Kindle/", topdown=False):
    for dir in dirs:
        if str(dir).endswith(".sdr"):
            #print(os.path.join(root,dir))
            # 如果文件夹以sdr结尾，就保存到列表中
            sdr_set.append(os.path.join(root,dir[:-3]))
# 再次遍历，如果一个文件以set中文件夹的全路径名为开始,并且不以sdr文件夹为开始，则在set中删除这个文件夹
# 原因是，sdr文件夹对应的电子书文件存在，则不需要删除这个sdr缓存文件夹
for root, dirs, files in os.walk("/Volumes/Kindle/", topdown=False):
    for name in files:
        for sdr_dir in sdr_set:
            # 如果对应文件存在，就从列表中删除对应SDR
            full_file_name = str(os.path.join(root,name))
            if full_file_name.startswith(sdr_dir) and not full_file_name.startswith(sdr_dir+"sdr"):
                print("exist: "+os.path.join(root,name))
                #print("exist: "+name)
                sdr_set.remove(sdr_dir)
                break
                
for sdr_dir in sdr_set:
    print("removed "+sdr_dir+"sdr")

    shutil.rmtree(sdr_dir+"sdr")
    pass

