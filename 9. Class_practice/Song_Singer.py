# 클래스 상속연습3 - 노래제목과 장르를 상속받아 가수와 매칭하기

class Song:
    def set_song(self, title, genre):
        self.title = title
        self.genre = genre

    def print_song(self):
        print(f"노래제목 : {self.title}({self.genre})")


class Singer:
    def set_singer(self, name):
        self.name = name

    def hit_song(self, song):
        self.song = song

    def print_singer(self):
        print(f"가수이름 : {self.name}")
        self.song.print_song()
        #print(f"노래제목 : {self.song.title}({self.song.genre})")

# test
obj_song = Song()
obj_song.set_song('취중진담', '발라드')
obj_song.print_song()

obj_singer = Singer()
obj_singer.set_singer('김동률')
obj_singer.hit_song(obj_song)
obj_singer.print_singer()
