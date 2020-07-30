class Beans():
    def __init__(self):
        self.frozen = {

        	'velocity': True,
            'posistion': False,
        	'acceleration': False,
        	'mass': True,
        }

mr = Beans()

for attribute in mr.frozen:
    if not mr.frozen[attribute]:
        print(attribute,"is not frozen")