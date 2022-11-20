def main():
    x, y = 100, 100
    width, height = 200, 200
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Функция рисует домик
    :param x: середина нижней части фундамента
    :param y: середина нижней части фундамента
    :param width: общая ширина
    :param height: общая высота домика
    :return: None
    """
    print('Типа рисую домик', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height-walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)

def draw_house_foundation(x, y, width, height):
    """
        Функция рисует домик
        :param x: середина нижней части фундамента
        :param y: середина нижней части фундамента
        :param width: общая ширина фундамента
        :param height: общая высота фундамента
        :return: None
        """
    print('Типа рисую фундамент', x, y, width, height)

def draw_house_walls(x, y, width, height):
    print('Типа рисую стену', x, y, width, height)

def draw_house_roof(x, y, width, height):
    print('Типа рисую крышу', x, y, width, height)

main()
