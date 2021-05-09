#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import apachelogs
import csv


# In[5]:


def parse_log(file):
    data = set()
    parser = apachelogs.parser.LogParser(apachelogs.COMBINED)
    with open(file) as fp:
        for entry in parser.parse_lines(fp):
            data.add((entry.remote_host, entry.request_line.split(' ')[1], entry.headers_in["User-Agent"]))
    return data


# In[15]:


def main():
    data = set()
    for root, folders, files in os.walk('.'):
        for file in files:
            if 'access_log' in file:
                data.update(parse_log(os.path.join(root, file)))
                print(f'added file {os.path.join(root, file)}')
    # write to csv file
    with open('result.csv', mode='w', newline='') as fout:
        writer = csv.writer(fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Host_IP', 'Path', 'UserAgent'])
        writer.writerows(data)


# In[16]:


main()


# In[ ]:




