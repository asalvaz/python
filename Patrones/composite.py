"""
Patron de diseño: Composite con Python
Arma un árbol de la misma clase. Va agregándolas a un 
array y luego con foreach podés obtener todos los
hijos de un objeto.


"""
class Empleado(object):

   def __init__(self, name,dept, sal): 
      self.name = name
      self.dept = dept
      self.salary = sal
      self.subordinates = []
   

   def add(self,e): 
      self.subordinates.append(e)
   


   def getSubordinates(self):
     return self.subordinates
   

   def __str__(self):
      return "Empleado :[ Name : " + self.name + ", dept : " + self.dept + ", salary :" + str(self.salary) +" ]"
      



class CompositePatternDemo(object): 
   def main(self): 
      
      CEO = Empleado("John","CEO", 30000)

      headSales =  Empleado("Robert","Head Sales", 20000)

      headMarketing =  Empleado("Michel","Head Marketing", 20000)

      clerk1 =  Empleado("Laura","Marketing", 10000)
      clerk2 =  Empleado("Bob","Marketing", 10000)

      salesExecutive1 =  Empleado("Richard","Sales", 10000)
      salesExecutive2 =  Empleado("Rob","Sales", 10000)

      CEO.add(headSales)
      CEO.add(headMarketing)

      headSales.add(salesExecutive1)
      headSales.add(salesExecutive2)

      headMarketing.add(clerk1)
      headMarketing.add(clerk2)

      # #print all Empleados of the organization
      print(CEO) 
      
      for headEmpleado in CEO.getSubordinates(): 
         print(headEmpleado)

         for empleado in headEmpleado.getSubordinates() : 
            print(empleado)
           
   


composite = CompositePatternDemo()
composite.main()