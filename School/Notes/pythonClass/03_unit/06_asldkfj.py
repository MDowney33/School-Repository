class Resume:
    def __init__(self, Name, experience, education):
        self.Name, self.experience, self.education = Name, experience, education

    def __str__(self):
        return f'{self.Name} \n{self.experience} \n{self.education} \n'

class Listing:
    def __init__(self,title,requirements,salary,candidates=[]):
        self.title,self.requirements,self.salary,self.candidates = title,requirements,salary,candidates

    def __str__(self):
        return self.title

    def count_candidates(self):
        return len(self.candidates)

    def print_candidates(self):
        for i in self.candidates:
            print(i)

class Candidate:
    def __init__(self,name,age,title,resume):
        self.name,self.age,self.title,self.resume = name,age,title,resume

    def __str__(self):
        return f'{self.name}, {self.title}'

    def apply(self,job):
        job.candidates.append(self)

resume_1 = Resume('JM', 'Lawyer', 'University of AMERICA')
resume_2 = Resume('WW', 'Chwem', 'MIT... bruh')

print(resume_1)

job = Listing('CEO... bruh', ['bus', 'ms'], 3555555555500000000)
print(job)

candida_1 = Candidate('SG... Why is this different', 50, 'lawyer', resume_1)
candida_2 = Candidate('WW', 54, 'Chwemist', resume_2)

print(candida_2)

candida_1.apply(job)
candida_2.apply(job)

print(job.count_candidates())

job.print_candidates()
