### Docker Notları:

* docker image ls -> imageleri listeler
* docker run .... -> dockerı çalıştırır.
* docker image rm -rf 'imageid' -> imageid siler
* docker built -t selamet_django:0.2 -> 0.2 versionlu image oluşturur
* docker exec -it 'dockerid' -> dockerid bashini açar

### Docker Compose:
* docker-compose build -> image oluşturur
* docker-compose run web django-admin startproject django_backend . -> terminale komut göndermemizi sağlar
* docker-compose run web python manage.py startapp exam
* docker-compose up --build -> hem çalıştırır hem build eder güncelleme yapıldığı zaman vs
* docker-compose run web bash -> image bashini açar