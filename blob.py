import random


class Blob:

    #called dunder init method
    def __init__(self, color, x_boundary, y_boundary, size_range=(4,8), movement_range=(-1,2)):

        #self.size = random.randrange(size_range[0],size_range[1])
        #use an unpacking operator * to unpack the tuple automatically
        self.size = random.randrange(*size_range)

        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.movement_range = movement_range

    #repr is for debugging purposes and should be as condensed as possible
    def __repr__(self):
        # return 'Blob({}, {}, ({}, {}))'.format(self.color,
        #                                        self.size,
        #                                        self.x,
        #                                        self.y)

        #easier way of using the format brackets per comments in ep 24
        return 'Blob({s.color}, {s.size}, ({s.x},{s.y})'.format(s=self)

    def __str__(self):
        return 'Blob of color:({}, size: {}, location: ({}, {}))'.format(self.color,
                                                                           self.size,
                                                                           self.x,
                                                                           self.y)

    def move(self):
        #the upper bound on randrange is NOT included.  so a <= x < b
        self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
        #print(self.move_x, self.move_y)
        self.x += self.move_x
        self.y += self.move_y

    def change_movement_range(self, movement_adjust):
        self.movement_range = (self.movement_range[0] - movement_adjust, self.movement_range[1] + movement_adjust)

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary