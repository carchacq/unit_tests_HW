import requests



class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path_to_folder):
        params = {"path": path_to_folder}
        response = requests.put(self.url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.status_code



if __name__ == '__main__':
    token = ''
    poster = YaUploader(token)
    # poster.create_folder("folder4")
