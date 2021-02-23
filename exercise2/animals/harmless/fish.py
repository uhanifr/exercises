class Fish:
    def __init__(self):
        'constructor for this class'
        #create some members
        self.members = ['salmon','tuna','mackerel']
    
    def printMembers(self):
        print('printing members of the Fishs class')
        for member in self.members:
            print('\t%s' % member)

