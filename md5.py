from hashlib import md5

read_file = 'countries_with_links.txt'
write_file = 'hashes.txt'

res = open(read_file, encoding='utf-8')


def gen_md5(input):
    for country in input:
        data = md5(country.encode())
        hash = data.hexdigest()
        yield hash


with open(write_file, 'w') as output:
    for item in gen_md5(res):
        print(item)
        output.write(item+'\n')
