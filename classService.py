class Service:
    
    def __init__(self,service):
        self.service = service
        print('{}Service is start.'.format(self.service))
        
    def __del__(self):
        print('{}Service is finish.'.format(self.service))

s = Service('guide')
del s