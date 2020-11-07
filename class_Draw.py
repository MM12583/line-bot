class Draw :
    def __init__(self) :
        self.rf = 'gift.csv'
        self.SSR = []  
        self.SR = [] 
        self.UR = []
        self.define_gift(self.rf)
        self.draw(1)

    def define_gift(self, readfile = 'gift.csv') :
        with open ('gift.csv', 'r' ,encoding = 'utf-8') as g_l :
            for g in g_l :
                level, item = g.strip().split(',')
                if '品級' in g :
                    continue
                elif 'SSR' in g :
                    self.SSR.append(item)
                elif 'SR' in g :
                    self.SR.append(item)
                else :
                    self.UR.append(item)

    def draw(self, times = 1) :
        import random as r
        for p in range(times) :    
            p = int(r.randint(1,1000))
            if p <= 25 :
                self.quality = 'SSR'
            elif p <= 100 :
                self.quality = 'SR'
            else :
                self.quality = 'UR'

        if self.quality == 'SSR' :
            get = int(r.randint(0,4))
            self.result = self.SSR[get]
        elif self.quality == 'SR' :
            get = int(r.randint(0,7))
            self.result = self.SR[get]
        else :
            get = int(r.randint(0,16))
            self.result = self.UR[get]

