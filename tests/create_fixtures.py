from os import path

cwd = path.abspath(path.dirname(__file__))


def create_file(length, blank=True):
    filepath = path.join(
        cwd, f'{"fixture_blank" if blank else "fixture"}_{length}.txt')
    with open(filepath, 'w') as testf:
        content = ' ' * length
        if not blank:
            content += 'foo'
        testf.write(content)


if __name__ == '__main__':
    for length in [100, 250, 500]:
        length = length * 1000000
        create_file(length, blank=True)
        create_file(length, blank=False)
