#!/usr/bin/env python
# encoding: utf-8

import re
from requests import get
from os import _exit

"""
假设你会用，不需要对恶意的id进行验证。
"""

def getId():
    """
    简单识别 id号
    """
    id = input("输入ID号或输入链接:\n")
    try:
        int(id)
    except ValueError:
        if(re.search('music',id)):
            id = re.search('[1-9][0-9]{4,}',id).group(0)
            # print(id)
        else:
            print("无法识别")
            _exit(1)
    finally:
        return id

def buffer(id):
    """
    获取 网易云音乐接口的歌词
    """
    url = f"http://music.163.com/api/song/lyric?id={id}&lv=1&kv=1&tv=-1"

    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'referer':f'https://music.163.com/song?id={id}'
    }

    soup_json = get(url,headers=headers).json()

    return soup_json 

def choose(data):
    choose =input("\t输出功能选项\n\t1). 输出歌词\n\t2). 输出翻译歌词(仅当为外语歌曲或存在)\n\t3).输出可能的歌词并分类(擦缝？)\n\t4)输出文件,并退出\n\t任意). 放弃\n")
    if('1' == choose):  # 1). 输出歌词
        print(re.sub('(.\d+){3,}.','',data['lrc']['lyric']))

    elif('2' == choose): # 2). 输出翻译歌词(仅当为外语歌曲或存在)
        """
        返回 zh-hans ,如果有的话
        """
        try:
            print(re.sub('(.\d+){3,}.','',data['tlyric']['lyric']))
        except:
            print("\n>>> !不存在,选项 1) 即可\n\n")
            
        

    elif('3' == choose):
        '''
        输出可能的歌词并分类(擦缝?)
        '''
        try:
            print(data['lrc']['lyric']+data['tlyric']['lyric'])
        except :
            print("\n>>> 没有数据 2, 无法进行\n")

    elif('4' == choose):
        "输出所有的类型文件"
        if(not data['tlyric']['lyric']):
            with open("tmusci_lyric.txt",'w',encoding='utf8') as f:
                ly = re.sub('(.\d+){3,}.','',data['lrc']['lyric'])
                "如果需要时间轴，修改此行"
                
                f.writelines(ly)
            _exit(0)
        else:
            with open('music_lyric.txt','w',encoding='utf8') as f:
                ly = re.sub('(.\d+){3,}.','',data['tlyric']['lyric'])
                "如果需要时间轴，修改此行"
                
                f.writelines(ly)
            _exit(0)

    else:
        _exit(0)

if __name__ == "__main__":
    data = buffer(getId())

    while(True):
        choose(data)



        

    
    



