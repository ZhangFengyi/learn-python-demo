# -*- coding: utf-8 -*-
import requests
import json
from pyecharts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token="

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer": "http://music.163.com/song?id=551816010",
    "Origin": "http://music.163.com",
    "Host": "music.163.com"
}

# 加密数据，直接拿过来使用
post_data = {
    "params": "V/rBBeLlO5L9lYqGj9JasgYkv1gRlr+b5zTAMnwI3kXIkAzYQFVKQ6jqZFSuYIz2qQEfaRzuPhVBGSHd9YhoRhgjwuaTggl4qCghEyyO6ki84wROcxrkQAno+g9JuChwBf9ZO8b98NTb5pMU20NoDEzhnknt7Xt/mphJqyL8xGrhA3tMFBaw0czXZ+rzrUdl",
    "encSecKey": "248f8d6b338a16cd543a7b7c5aee60144fc9d8fc196dd82d047a0547bcefcd7b59f11f1a1455fdfb02ef5150fa622589248c3838b5b799d5d36b6e51da9afa77eb15e097567e4b6993f28a3c8b7febad168fe08ff1f1bdedcd61521f3e7cdb4f2a44fee13857cd995daabf8fd6b17d0ed0d3b8fea747c0412a79e87bfa930064"
}

response = requests.post(url, headers=headers, data=post_data)

data = json.loads(response.text)
hot_comment_list = []
for hot_comment in data['hotComments']:
    item = {
        'nickname': hot_comment['user']['nickname'],
        'content': hot_comment['content'],
        'liked_count': hot_comment['likedCount']
    }
    hot_comment_list.append(item)


# 获取内容、用户名以及获赞数列表
nickname_list = [comment['nickname'] for comment in hot_comment_list]
content_list = [comment['content'] for comment in hot_comment_list]
liked_count_list = [comment['liked_count'] for comment in hot_comment_list]

# bar = Bar("热评中点赞数示例图")
# bar.add("点赞数", nickname_list, liked_count_list, is_stack=True, mark_line=['min', 'max'], mark_point=['average'])
# bar.render()

content_text = " ".join(content_list)
word_cloud = WordCloud(font_path="/Library/Fonts/Arial Unicode.ttf", max_words=200).generate(content_text)
plt.figure()
plt.imshow(word_cloud, interpolation='bilinear');
plt.axis('off')
plt.show()
