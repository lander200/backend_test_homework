class Piu:
    def __init__(self, action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight

    m_in_im = 1000
    len_step = 0.65
            
    def get_distance(self):
        """Получить дистанцию в км."""
        dist = self.action * self.len_step / self.m_in_im
        return dist

mao = Piu(200,200,300)
afaa = mao.get_distance()
print(afaa)
