class father:
      def skills(self):
          print('father has skills in chewing food')
          
class mother:
      def skills(self):
          print('mother serves dad each and everything he wants')
          
class child(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
c= child()
c.skills( )      