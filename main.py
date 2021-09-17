import json


read_file = 'countries.json'
write_file = 'countries_with_links.txt'


class WikiArticle:
    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start

    def __iter__(self):
        self.start = self.start - 1
        return self

    def __next__(self):
        output = []
        for self.country in self.json:
            self.country = self.country['name']['common']
            self.country = self.country.replace(' ', '_')
            wiki_url = 'https://en.wikipedia.org/wiki/'
            country_page = wiki_url + self.country
            country_link_pair = f'{self.country}, {country_page} ' + ' \n'
            output.append(country_link_pair)
        self.start += 1
        if self.start >= len(output):
            raise StopIteration
        return output


if __name__ == '__main__':
    with open(write_file, 'w') as f:
        article = WikiArticle(read_file, 0)
        for country in article.__next__():
            f.writelines(country)
