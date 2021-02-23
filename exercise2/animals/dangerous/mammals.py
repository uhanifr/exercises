class Mammals:
    def __init__(self):
        'constructor for this class'
        #create some members
        self.members = ['Bat','Tiger','Lion']
    
    def printMembers(self):
        print('printing members of the Mammals class')
        for member in self.members:
            print('\t%s' % member)
