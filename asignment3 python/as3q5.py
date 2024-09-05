class circle:
    
  r=0

  def __init__(self,radius):

    self.r=r

    print("Area of circle is :",self.r*self.r*3.14)

    print("Circumference of circle is :",2*self.r*3.14)

r=int(input("Enter the radius:"))

obj=circle(r)
