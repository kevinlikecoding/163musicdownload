from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB
from mutagen.easyid3 import EasyID3
import mutagen.id3
import mutagen
import api
import time
import os

try:
    resp,c = api.phone_login()
except api.requests.exceptions.ConnectionError:
    api.start_server()
    time.sleep(2)
    resp,c = api.phone_login()
count = 0
os.system("rm ../tmp/*")
def download_song_flac(id):
    url = api.get_song_url(id, c)
    if str(os.system("pwd")).endswith("Api"):
        os.chdir("..")
    if str(url).endswith(".flac"):
        os.system("aria2c "+url+" -o ./tmp/song_tmp.flac")
        pic_url = api.get_song_pic(id,c)
        os.system("aria2c "+pic_url+" -o ./tmp/cover.jpg")
        picPath = './tmp/cover.jpg'
        
        songFile = ID3()

        with open(picPath, 'rb') as f:
            picData = f.read()
        songFile['APIC'] = APIC(  # 插入封面
            encoding=3,
            mime='./tmp/cover.jpg',
            type=3,
            desc=u'Cover',
            data=picData
        )
        songFile['TIT2'] = TIT2(  # 插入歌名
            encoding=3,
            text=api.get_song_name(id,c)
        )
        songFile['TPE1'] = TPE1(  # 插入第一演奏家、歌手、等
            encoding=3,
            text=api.get_song_artist_name(id,c)
        )
        songFile['TALB'] = TALB(  # 插入专辑名
            encoding=3,
            text=api.get_song_album_name(id,c)
        )
        songFile.save("./tmp/song_tmp.flac")
        if str(os.system("pwd")).endswith("Api"):
            os.chdir("..")
        os.system("cp ./tmp/song_tmp.flac ./Downloads/")
        os.system("mv ./Downloads/song_tmp.flac \"./Downloads/"+api.get_song_name(id,c)+"-"+api.get_song_artist_name(id,c)+".flac\"")
        os.system("rm ./tmp/*")
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
    else:
        os.system("aria2c "+url+" -o ./tmp/song_tmp.mp3")
        pic_url = api.get_song_pic(id,c)
        os.system("aria2c "+pic_url+" -o ./tmp/cover.jpg")
        picPath = './tmp/cover.jpg'
        
        songFile = ID3()

        with open(picPath, 'rb') as f:
            picData = f.read()
        songFile['APIC'] = APIC(  # 插入封面
            encoding=3,
            mime='./tmp/cover.jpg',
            type=3,
            desc=u'Cover',
            data=picData
        )
        songFile['TIT2'] = TIT2(  # 插入歌名
            encoding=3,
            text=api.get_song_name(id,c)
        )
        songFile['TPE1'] = TPE1(  # 插入第一演奏家、歌手、等
            encoding=3,
            text=api.get_song_artist_name(id,c)
        )
        songFile['TALB'] = TALB(  # 插入专辑名
            encoding=3,
            text=api.get_song_album_name(id,c)
        )
        songFile.save("./tmp/song_tmp.mp3")
        if str(os.system("pwd")).endswith("Api"):
            os.chdir("..")
        os.system("cp ./tmp/song_tmp.mp3 ./Downloads/")
        os.system("mv ./Downloads/song_tmp.mp3 \"./Downloads/"+api.get_song_name(id,c)+"-"+api.get_song_artist_name(id,c)+".mp3\"")
        os.system("rm ./tmp/*")
        print(os,os.system("pwd"))
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
        print(os.system("du -h ./Downloads"))
def download_song_mp3(id):
    if str(os.system("pwd")).endswith("Api"):
        os.chdir("..")
    url = api.get_song_url(id, c)
    if str(url).endswith(".flac"):
        os.system("aria2c "+url+" -o ./tmp/song_tmp_flac.flac")
        os.system("ffmpeg -i ./tmp/song_tmp_flac.flac ./tmp/song_tmp.mp3")
    else:
        os.system("aria2c "+url+" -o ./tmp/song_tmp.mp3")
    pic_url = api.get_song_pic(id,c)
    os.system("aria2c "+pic_url+" -o ./tmp/cover.jpg")
    picPath = './tmp/cover.jpg'
    
    songFile = ID3()

    with open(picPath, 'rb') as f:
        picData = f.read()
    songFile['APIC'] = APIC(  # 插入封面
        encoding=3,
        mime='./tmp/cover.jpg',
        type=3,
        desc=u'Cover',
        data=picData
    )
    songFile['TIT2'] = TIT2(  # 插入歌名
        encoding=3,
        text=api.get_song_name(id,c)
    )
    songFile['TPE1'] = TPE1(  # 插入第一演奏家、歌手、等
        encoding=3,
        text=api.get_song_artist_name(id,c)
    )
    songFile['TALB'] = TALB(  # 插入专辑名
        encoding=3,
        text=api.get_song_album_name(id,c)
    )
    songFile.save("./tmp/song_tmp.mp3")
    if str(os.system("pwd")).endswith("Api"):
        os.chdir("..")
    os.system("cp ./tmp/song_tmp.mp3 ./Downloads/")
    os.system("mv ./Downloads/song_tmp.mp3 \"./Downloads/"+api.get_song_name(id,c)+"-"+api.get_song_artist_name(id,c)+".mp3\"")
    os.system("rm ./tmp/*")
    print(os,os.system("pwd"))
    print(os.system("du -h ./Downloads"))
    print(os.system("du -h ./Downloads"))
    print(os.system("du -h ./Downloads"))
    print(os.system("du -h ./Downloads"))
    print(os.system("du -h ./Downloads"))
sel1 = input("欢迎！\n输入1：下载歌单\n输入2：下载专辑\n输入3：下载歌手的全部歌曲\n输入4：下载单曲\n输入5：下载关注的所有歌手的所有歌曲\n你的选择是：")
sel2 = input("不转码FLAC还是将FLAC转码为MP3(y/n): ")

if sel1 == '1':
    if sel2 == 'y':
        tracks = api.get_playlist_track(input('请输入歌单ID：'),c)
        for i in range(len(tracks)):
            download_song_flac(tracks[i])
    if sel2 == 'n':
        tracks = api.get_playlist_track(input('请输入歌单ID：'),c)
        for i in range(len(tracks)):
            download_song_mp3(tracks[i])


if sel1 == '2':
    if sel2 == 'y':
        tracks = api.get_album_track(input('请输入专辑ID：'),c)
        for i in range(len(tracks)):
            download_song_flac(tracks[i])
    if sel2 == 'n':
        tracks = api.get_album_track(input('请输入专辑ID：'),c)
        for i in range(len(tracks)):
            download_song_mp3(tracks[i])


if sel1 == '3':
    if sel2 == 'y':
        tracks = api.get_artist_all_song(input('请输入艺术家ID：'),c)
        for i in range(len(tracks)):
            download_song_flac(tracks[i])
    if sel2 == 'n':
        tracks = api.get_artist_all_song(input('请输入艺术家ID：'),c)
        for i in range(len(tracks)):
            download_song_mp3(tracks[i])


if sel1 == '4':
    if sel2 == 'y':
        tracks = input('请输入歌曲ID：')
        download_song_flac(tracks)
    if sel2 == 'n':
        tracks = input('请输入歌曲ID：')
        download_song_flac(tracks)


if sel1 == '5':
    if sel2 == 'y':
        id_list = input("请输入艺术家ID，以“,”间隔： ").split(",")
        for j in id_list:
            tracks = api.get_artist_all_song(j,c)
            for i in range(len(tracks)):
                download_song_flac(tracks[i])
    if sel2 == 'n':
        tracks = api.get_artist_all_song(input('请输入艺术家ID：'),c)
        for i in range(len(tracks)):
            download_song_mp3(tracks[i])
