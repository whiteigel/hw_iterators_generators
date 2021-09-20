import hashlib

read_file = 'countries_with_links.txt'
write_file = 'hashes.txt'

res = open(read_file, 'rb')


def gen_md5(input):
    for country in input:
        yield hashlib.md5(country).hexdigest()


with open(write_file, 'w') as output:
    for item in gen_md5(res):
        print(item)
        output.write(item+'\n')
