import json

read_file = 'countries.json'
write_file = 'countries_with_links.txt'


class WikiArticle:
    def __init__(self, path, start):
        self.json = json.load(open(path, encoding='utf-8'))
        self.start = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        wiki_url = 'https://en.wikipedia.org/wiki/'
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration
        self.country = self.json[self.start]['name']['common']
        self.country_link = self.country.replace(' ', '_')
        return f'{self.country} - {wiki_url}{self.country_link}\n'


if __name__ == '__main__':
    article = WikiArticle(read_file, 0)
    with open(write_file, 'w') as f:
        for country in article:
            f.writelines(country)
