"""
Patron de diseño: Builder con Python
Agrega en un array un listado de objetos todos polimórficos 
para luego ejecutarlos en secuencia.
Tener en cuenta que los items a agregar deben ser pequeñas clases. 
No deben ser complejas.


"""
class Item(object): 
   def __init__(self, name):
      self.name = name
   
   def getName(self):
      return self.name

   def changeName(name) :
      self.name = name
   


class Builder(object) :

   def __init__(self) :
      self._items = []
   

   def add(self, e) :
      self._items.append(e)
   


   def getItems(self) :
     return self._items
   

   def showItems(self) : 
      for item in self._items :
         print(item.getName())
      
   


class MyBuilder(object) :
   def preprarItems(self) :
      builder = Builder()
      builder.add( Item("Item 1") )
      builder.add( Item("Item 2") )
      builder.add( Item("Item 3") )

      return builder
   

   def preprarOtrosItems(self) :
      builder = Builder()
      builder.add( Item("Lapicera") )
      builder.add( Item("Cuaderno") )
      builder.add( Item("Notebook") )
      builder.add( Item("Cables") )
      builder.add( Item("Auriculares") )
      return builder
   


class BuilderPatternDemo(object) :
   def main(self) :
   
      builderItems = MyBuilder()
      myItems = builderItems.preprarItems()
      myOtrosItems = builderItems.preprarOtrosItems()
      
      print("\n\rMyItems: ")
      myItems.showItems()

      print("\n\rMyOtrosItems: ")
      myOtrosItems.showItems()
   


builder = BuilderPatternDemo()
builder.main()