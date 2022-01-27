class Training:
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self, action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self):
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self):
        return self.get_distance() / self.duration

    def get_spent_calories(self):
        pass

    def show_training_info(self):  # определить класс info message и создать объект от него
        return InfoMessage(self.action, self.duration, self.weight, self.get_mean_speed(), self.get_spent_calories())


class Running(Training):

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        return (self.get_mean_speed() * self.coeff_calorie_1 - self.coeff_calorie_2) * self.weight / self.M_IN_KM


class SportsWalking(Training):

    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):  # написать красиво

        return 0.035 * self.weight + (self.get_mean_speed()**2 // self.height * 0.29 * self.weight) * self.duration


class Swimming(Training):

    LEN_STEP = 1.38

    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self):
        return (self.get_mean_speed() + 1.1) * 2 * self.weight


class InfoMessage:
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training.action
        self.duration = training.duration
        self.distance = training.get_distance()
        self.speed = training.get_mean_speed()
        self.calories = training.get_spent_calories()

    def result(self):
        return (f'Тип тренировки: {training.action}; Длительность: {training.duration} ч.; Дистанция: {training.get_distance()} км; Ср.скорость: {training.get_mean_speed()} км/ч; Потрачено ккал: {training.get_spent_calories()}.')


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),  # action, duration, weight, length_pool, count_pool
        ('RUN', [15000, 1, 75]),  # acion, duration, weight
        ('WLK', [9000, 1, 75, 180]),  # action, duration, weight, height
    ]

    def read_package(workout_type, data): #Функция чтения принятых пакетов
        if workout_type == 'SWM':
            return Swimming(*data)
        elif workout_type == 'RUN':
            return Running(*data)
        elif workout_type == 'WLK':
            return SportsWalking(*data)


    def main(training):
        info = training.show_training_info()
        #print(f'Тип тренировки: {training.action}; Длительность: {training.duration} ч.; Дистанция: {training.get_distance()} км; Ср.скорость: {training.get_mean_speed()} км/ч; Потрачено ккал: {training.get_spent_calories()}.')
        print(info.result())

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
