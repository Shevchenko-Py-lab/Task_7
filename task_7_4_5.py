import os
import json


def file_size():
    size_stats = {}

    # по сути то же самое, что было на разборе, но я упёрся чтобы всё в рамках "PycharmProject" работало.
    # в задании также было сказано про то, что должны попасть только расширения файлов

    for item in os.scandir('../../'):
        if item.is_dir():
            for x in os.scandir('.'):
                if x.is_file():
                    size = x.stat().st_size
                    threshold = 10 ** len(str(size))
                    ext = x.name.split('.')[-1]
                    try:
                        size_stats[threshold][0] += 1
                        ext_list = size_stats[threshold][1]
                        if ext in ext_list:
                            pass
                        else:
                            ext_list.append(ext)

                    except (KeyError, IndexError):
                        size_stats[threshold] = [1, [ext]]

    with open('summary.json', 'w') as f:
        f.write(json.dumps(size_stats))


if __name__ == '__main__':
    file_size()

