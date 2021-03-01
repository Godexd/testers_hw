import yandex


class TestApp:

    def test_create_folder(self):
        name = 'folder'
        uploader = yandex.YandexApi()
        uploader.create_folder(name)
        exist = yandex.requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=' + '%2F'
                                  + name, headers=uploader.headers)
        assert exist.status_code == 200

    def test_delete_folder(self):
        name = 'folder'
        uploader = yandex.YandexApi()
        uploader.delete_folder(name)
        exist = yandex.requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=' + '%2F'
                                  + name, headers=uploader.headers)
        assert exist.status_code != 200