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

    def show_training_info(self):
        return self.__class__

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

    def get_spent_calories(self):
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

class InfoMessage(Training):
    def __init__(self, action, weight, duration):
        super().__init__(action, duration, weight)
        self.training_type = self.show_training_info()
        self.distance = self.get_distance()
        self.speed = self.get_mean_speed()
        self.calories = self.get_spent_calories()

    def results(self):
        print(f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.')

if __name__ == '__main__': #как я понял, это часть для получения исходных данных. но покане понял, как это работает.
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)