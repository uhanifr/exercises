class Mammals:
    def __init__(self):
        'constructor for this class'
        #create some members
        self.members = ['Dog','Cat','Fox']
    
    def printMembers(self):
        print('printing members of the Mammals class')
        for member in self.members:
            print('\t%s' % member)
