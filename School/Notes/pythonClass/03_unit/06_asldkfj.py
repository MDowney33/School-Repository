
class Resume:
    def __init__(self, Name, experience, education):
        self.Name, self.experience, self.education = Name, experience, education

    def __str__(self):
        return f'{self.Name} \n{self.experience} \n{self.education} \n'

p = Resume('hi', 'I\'m', 'Matthew')
print(p)


