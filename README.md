# Vorwärts Kleinanzeigen

## bootstrap the project

* Clone from github

```sh
    git clone git@github.com:staeff/vorwaerts-gallery.git
```

* Download the image files

Download the following files and place them into the project folder `vorwaerts-gallery`

scans.tar.gz - https://wetransfer.com/downloads/1ef5a16f37245d8d0208638d6b6cddab20211026191832/24a57a

thumbs.tar.gz - https://wetransfer.com/downloads/874aa306a8b8c461705136e92fdb98b820211027101625/5e6bbc

ads.tar.gz - tbd

* Bootstrap Django app. Requires `make` and `tar`

```sh
    make bootstrap
```

* Run the app

```
    make run
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in the Browser
