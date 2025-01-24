class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pass

    def dist_from_origin(self):
        dist = (self.x**2 + self.y**2)**(0.5) # distance formula
        return dist

    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()


    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()

    def __eq__(self, other):
        return self.dist_from_origin() == other.dist_from_origin()

    def __str__(self):
        return f'Point({self.x}, {self.y})'
        


# ^^^Implement class and functionality above (remember to include docstrings!)
# vvvImplement tests below

if __name__ == '__main__':
   
   p1 = Point(3, 4) # dist = 5
   p2 = Point(3, 4) # dist = 5
   p3 = Point(4, 3) # dist = 5
   p4 = Point(0, 1) # dist = 1

   assert p1.x == 3 #expected True
   assert p1.y == 4 # expected True
   assert not p3.y == 4 #expected False

   assert p1 > p4 # expected True
   assert not p4 > p1 # expected False
   
   assert p4 < p1 # expected True
   assert not p1 < p2 # expected False

   assert p1 == p3 #expected True
   assert not p3 == p4 #expected False

   assert str(p1) == 'Point(3, 4)'
   assert not str(p4) == 'Point(3, 4)'
   
   


   
   
   
   
    # All tests should use `assert`, not `print`
    
    ##### test init #####
    # assert correct x
    # assert correct y

    ##### test lt #####
    # Expected True (e.g `p1 < p2`)
    # Expected False (e.g. `not p1 < p2`)

    ##### test gt #####
    # Expected True (e.g `p1 > p2`)
    # Expected False (e.g. `not p1 > p2`)

    ##### test eq #####
    # Expected True (e.g `p1 == p2`)
    # Expected False (e.g. `not p1 == p2`)

    
    ##### test str #####
    # assert str(some_point) == expected_string

    ##### test dist_from_origin() #####
   