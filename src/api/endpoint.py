class Endpoint:
    def __init__(self, url_template: str):
        self.url_template = url_template

    def __call__(self, region, **kwargs):
        path = self.url_template.format(**kwargs)
        url = f"https://{region}.api.riotgames.com{path}"
        return url