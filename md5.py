import hashlib

read_file = 'countries_with_links.txt'
write_file = 'hashes.txt'


def gen_md5():
    with open(read_file, 'rb') as res:
        for country in res:
            yield hashlib.md5(country).hexdigest()


with open(write_file, 'w') as output:
    for item in gen_md5():
        print(item)
        output.write(item+'\n')
