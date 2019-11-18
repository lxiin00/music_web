from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.utils.http import urlquote
from index.models import *


def playView(request, song_id):
    # 热搜歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:6]
    # 歌曲信息
    song_info = Song.objects.get(song_id=int(song_id))
    # 播放列表
    play_list = request.session.get('play_list', [])
    song_exist = False
    if play_list:
        for i in play_list:
            if int(song_id) == i['song_id']:
                song_exist = True
    if song_exist == False:
        play_list.append({'song_id': int(song_id), 'song_singer': song_info.song_singer, 'song_name': song_info.song_name, 'song_time': song_info.song_time})
    request.session['play_list'] = play_list

    if song_info.song_lyrics != '暂无歌词':
        f = open('static/songLyric/' + song_info.song_lyrics , 'r', encoding='utf-8')
        song_lyrics = f.read()
        f.close()
        song_type = Song.objects.values('song_type').get(song_id=song_id)['song_type']
        song_relevant = Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by('-dynamic_plays').all()[:6]
        dynamic_info = Dynamic.objects.filter(song_id=int(song_id)).first()
        if dynamic_info:
            dynamic_info.dynamic_plays += 1
            dynamic_info.save()
        else:
            dynamic_info = Dynamic(dynamic_plays=1, dynamic_search=0, dynamic_down=0, song_id=song_id)
            dynamic_info.save()

    return render(request, 'play.html', locals())


def downloadView(request, song_id, song_name):
    song_info = Song.objects.get(song_id=int(song_id))
    dynamic_info = Dynamic.objects.filter(song_id=int(song_id)).first()
    if dynamic_info:
        dynamic_info.dynamic_down += 1
        dynamic_info.save()
    else:
        dynamic_info = Dynamic(dynamic_plays=0, dynamic_down=1, dynamic_search=0, song_id=song_id)
        dynamic_info.save()
    file = 'static/songFile/' + song_info.song_file

    def file_iterator(file, chunk_size=512):
        with open(file, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    filename = song_name + '.mp3'
    response = StreamingHttpResponse(file_iterator(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="%s"' % urlquote(filename)
    return response