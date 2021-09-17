import json


read_file = 'countries.json'
write_file = 'countries_with_links.txt'


class WikiArticle:
    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration
        self.country = self.json[self.start]['name']['common']
        self.country = self.country.replace(' ', '_')
        wiki_url = 'https://en.wikipedia.org/wiki/'
        country_page = wiki_url + self.country
        country_link_pair = f'{self.country}, {country_page} ' + ' \n'
        return country_link_pair


if __name__ == '__main__':
    article = WikiArticle(read_file, 0)
    with open(write_file, 'w') as f:
        for country in article:
            f.writelines(country)
