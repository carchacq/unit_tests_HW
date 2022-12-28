import pytest
import requests
from yandex import YaUploader

token = ''
yandex = YaUploader(token)
path_to_folder = 'newish_folder'


def test_create_folder():
    assert yandex.create_folder(path_to_folder) == 201

class tear_d(YaUploader):
    def tear_down(self, path):
        params = {'path': path}
        requests.delete(self.url, params=params, headers=self.get_headers())

yandex_del = tear_d(token)
yandex_del.tear_down(path_to_folder)