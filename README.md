# komiko
Download Manga Berbahasa Indonesia dari [Mangacanblog]

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
``` IMAGES_STORE = '/path/to/your/manga/folder' ```

### List of Manga
* one_piece
* naruto
* fairy_tail
* hunter_x_hunter
* bleach
* detective_conan



[Mangacanblog]: <http://mangacanblog.com>