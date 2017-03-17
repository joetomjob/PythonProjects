import turtle as t

class Weight:
    def __init__(self):
        self.mass = None
        self.magnitude = None


class Beam:
    def __init__(self,name):
        self.name = name
        self.child = []
        self.magnitude = None

        self.totalWeight = None
        self.totalWeight_unsigned  = None

    def verify(self):
        if int(self.totalWeight) != 0:
            return False
        else:
            return True

    def Draw(self):
        if len(self.child)>0:
            x = self
            self.Draw_beam(x)

    def Draw_beam(self, mainb):
         if len(mainb.child)>0:
             for i in range(len(mainb.child)):
                mainbeam = mainb
                if type(mainb.child[i]).__name__ == 'Beam':
                    if mainbeam.child[i].magnitude is not None:
                        self.draw_main_beam(mainbeam.child[i].magnitude,200)
                    mainbeam = mainbeam.child[i]
                    self.Draw_beam(mainbeam)
                    if mainbeam.child[i].magnitude is not None:
                        self.draw_main_beam_back(mainbeam.magnitude, 200)
                else:
                    for j in range(len(mainbeam.child)):
                        if type(mainbeam.child[j]).__name__ == 'Weight':
                            c = mainbeam.child[j]
                            self.draw_leaf(c)
                    return

    def draw_leaf(self,c):
        self.draw_the_leaf(int(c.magnitude), 20, float(c.mass))

    def draw_main_beam(self,magnitude,scalefactor):
        t.fd(50)
        moving_distance = abs(int(magnitude)) * scalefactor
        t.left(self.left_or_right(magnitude))
        t.fd(moving_distance)
        t.right(self.left_or_right(magnitude))

    def draw_main_beam_back(self,magnitude,scalefactor):
        moving_distance = abs(int(magnitude)) * scalefactor
        t.left(self.left_or_right(magnitude))
        t.back(moving_distance)
        t.right(self.left_or_right(magnitude))
        t.back(50)

    def draw_the_leaf(self,magnitude, scalefactor, mass):
        t.speed(0)
        moving_distance = abs(magnitude) * scalefactor
        t.fd(50)
        t.left(self.left_or_right(magnitude))
        t.fd(moving_distance)
        t.right(self.left_or_right(magnitude))
        t.fd(50)
        t.up()
        t.fd(15)
        t.down()
        t.write(mass)
        t.up()
        t.back(50 + 15)
        t.left(self.left_or_right(magnitude))
        t.back(moving_distance)
        t.right(self.left_or_right(magnitude))
        t.back(50)
        t.down()

    def left_or_right(self,magnitude):
        if int(magnitude) < 0:
            return -90
        else:
            return 90

    # def calculate_scale_factor(self):
    #     t = self
    #     if self.child is no



def main():
    f = input('Enter the message filename(with .txt): ')
    #f = "balance.txt"
    total = []
    with open(f) as data:
        for x in data:
            x = x.strip()
            partsop = x.strip().split(' ')
            beam = Beam(partsop[0])
            leftmass = 0
            rightmass = 0
            total_mass = 0
            tmass_unsign = 0
            empty_flag = 0
            for i in range(int(len(partsop)/2)):
                w = Weight()
                if partsop[2 + (2 * i)] == '-1':
                    empty_flag = 1
                    w.magnitude = partsop[1 + (2 * i)]
                    w.mass = partsop[2 + (2 * i)]
                    beam.child.append(w)
                elif partsop[2 + (2 * i)][0] == 'B':
                    for j in range(len(total)):
                        if partsop[2 + (2 * i)] == total[j].name:
                            total_mass += float(total[j].totalWeight)
                            tmass_unsign += float(total[j].totalWeight_unsigned)
                            if int(partsop[1+(2*i)]) < 0:
                                leftmass += tmass_unsign* float(partsop[1+(2*i)])
                            else:
                                rightmass += tmass_unsign * float(partsop[1+(2*i)])
                            beam.child.append(total[j])
                            total[j].magnitude = partsop[1+(2*i)]
                else:
                    w.mass = partsop[2 + (2 * i)]
                    w.magnitude = partsop[1+(2*i)]
                    total_mass += float(w.mass)*float(w.magnitude)
                    tmass_unsign += float(w.mass)*abs(float(w.magnitude))

                    if float(w.magnitude) < 0:
                        leftmass += float(w.mass) * float(w.magnitude)
                    else:
                        rightmass += float(w.mass) * float(w.magnitude)
                    total_mass = rightmass+leftmass
                    beam.child.append(w)
            if empty_flag == 1:
                for i in range(len(beam.child)):
                   if type(beam.child[i]).__name__ == 'Weight':
                        if beam.child[i].mass == "-1":
                            beam.child[i].mass = abs(float(total_mass)/float(beam.child[i].magnitude))
                            print("To balance the beam, the empty pan should have a weight of : "+str(beam.child[i].mass))
                            total_mass += beam.child[i].mass* float(beam.child[i].magnitude)
            beam.totalWeight = total_mass
            beam.totalWeight_unsigned = tmass_unsign
            total.append(beam)

    total = total[len(total) - 1]
    t.up()
    t.right(90)
    t.back(200)
    t.down()
    # total.calculate_scale_factor()
    if total.verify() == True:
        print("The beam is balanced")
    else:
        print("The beam is not balanced")
    total.Draw()



if __name__ == '__main__':

    main()
    t.mainloop()