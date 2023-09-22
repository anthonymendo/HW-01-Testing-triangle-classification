import unittest     # this makes Python unittest module available

def classify_triangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    # Note: This code is completely bogus but demonstrates a few features of python
    
    right = [a, b, c]
    right.sort()
    a, b, c = right[0], right[1], right[2]

    if a + b <= c:
        return 'NotATriangle'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return "Isosceles"
    elif a**2 + b**2 == c**2:
        return 'Right'
    else:
        return 'Scalene'

        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

class TestTriangles(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene")
        # 3,4,5 returns Right instead of Scalene; failed Test

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(6, 8, 10), "Right")
        self.assertEqual(classify_triangle(1, 2, 3), "Right")
        #1,2,3 is not a Right triangle; failed Test

    def testSet1(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        self.assertNotEqual(classify_triangle(10,10,10),'Equalateral','Should be Equilateral')
        self.assertEqual(classify_triangle(10,15,30),'NotATriangle','Should be Isoceles')

    def testNotTriangle(self):
        self.assertEqual(classify_triangle(1,1,1),'NotATriangle','1,1,1 should be equilateral')
        #1,1,1 is equilateral; failed test 

if __name__ == '__main__':
    # examples of running the code
    #runClassifyTriangle(1,2,3)
    #runClassifyTriangle(1,1,1)
    
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line