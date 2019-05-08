from scrapy.loader.processors import Compose, MapCompose


def filter_world(s):
    return None if s == 'world' else s
if __name__ == '__main__':
    proc = Compose(lambda v : v[0], str.upper)
    print(proc(['hello', 'world']))
    proc2 = MapCompose(filter_world, str.upper)
    print(proc2(['hello', 'world','apple']))
