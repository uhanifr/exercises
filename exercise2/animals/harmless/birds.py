class Birds:
    def __init__(self):
        'constructor for this class'
        #create some members
        self.members = ['Duck','Cockatoos','Dove']
    
    def printMembers(self):
        print('printing members of the birds class')
        for member in self.members:
            print('\t%s' % member)
