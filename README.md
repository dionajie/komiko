# komiko
Download Manga Berbahasa Indonesia dari [Mangacanblog]. Komiko is one of apps on challenge list i made. You can read it on [my blog].

### Version
1.0

### Installation
``` python setup.py ```

### How to
``` sh
scrapy crawl mangacan -a manga=one_piece -a chapter=814 
scrapy crawl mangacan -a manga=naruto -a chapter=700 
```

### Manga Directories
open setting.py and edit this line
```sh
IMAGES_STORE = '/path/to/your/manga/folder' 
```

### List of Manga
* one_piece
* naruto
* fairy_tail
* hunter_x_hunter
* bleach
* detective_conan




[Mangacanblog]: <http://mangacanblog.com>
[my blog] : <https://blog.dionajie.com/python-apps-challenge-1bc71acbdc5f#.tgqxlbw31>