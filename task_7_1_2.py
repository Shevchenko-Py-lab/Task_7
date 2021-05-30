import os
from pathlib import Path


def parse_yaml():
    with open('config2.yaml', 'r', encoding='utf-8') as f:
        current_folder_path = Path.cwd()
        current_nest = 0
        for raw_line in f:
            processed_line = raw_line.strip("-: \n\r")

            if raw_line.endswith(':\n'):

                # если cur_nest == 0 мы в корне
                if current_nest == 0:
                    current_folder_path = current_folder_path.joinpath(
                        processed_line
                    )

                    current_nest += 1

                # если пошли вверх по иерархии
                elif raw_line.index('-') < (current_nest * 4):

                    new_folder_nest = raw_line.index('-') // 4

                    parent_nest = current_nest - new_folder_nest - 1

                    current_folder_path = \
                        Path(current_folder_path).parents[parent_nest].joinpath(
                            processed_line
                        )

                    current_nest = raw_line.index('-') // 4

                # вниз по иерархии
                else:
                    current_folder_path = \
                        Path(current_folder_path).joinpath(processed_line)

                # создаём папку из сформированного пути
                if not os.path.exists(current_folder_path):
                    os.mkdir(current_folder_path)

            # это файл
            else:
                filename = current_folder_path.joinpath(processed_line)

                # вложенность увеличивается при создании файла
                if raw_line.index('-') > (current_nest * 4):
                    current_nest += 1

                if not os.path.exists(filename):
                    open(filename, 'w').close()


if __name__ == '__main__':
    parse_yaml()
