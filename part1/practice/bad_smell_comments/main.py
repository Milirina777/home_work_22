# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, x0, y0, direction, fly, crawl, speed=1):
        """Функция реализует перемещение юнита по полю"""
        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        if fly:
            speed *= 1.2
            if direction == 'UP':
                y1 = y0 + speed
                x1 = x0
            elif direction == 'DOWN':
                y1 = y0 - speed
                x1 = x0
            elif direction == 'LEFT':
                y1 = y0
                x1 = x0 - speed
            elif direction == 'RIGHT':
                y1 = y0
                x1 = x0 + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                y1 = y0 + speed
                x1 = x0
            elif direction == 'DOWN':
                y1 = y0 - speed
                x1 = x0
            elif direction == 'LEFT':
                y1 = y0
                x1 = x0 - speed
            elif direction == 'RIGHT':
                y1 = y0
                x1 = x0 + speed

            field.set_unit(x=x1, y=y1, unit=self)