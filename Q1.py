# HTML python DSA Java SQL
class Participant:
    def __init__(self, roll, skills):
        self.roll = roll
        self.skills = skills
        self.is_mentoring = False
        self.placed = False
        self.project = "no"

    def __str__(self):
        return "Roll: {}\tProject: {}".format(self.roll, str(self.project))

class Project:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.complete = False
        self.participants = []
        self.posts_full = [False for skill in skills]
        for ind, skill in enumerate(skills):
            if skill == 0:
                self.posts_full[ind] = True
    
    def is_complete(self):
        for item in self.posts_full:
            if not item:
                return False
        self.complete = True
        return True
    
    def __str__(self) -> str:
        s = "Name: {}\tComplete: {}\tPosts: {}\n".format(*map(str, [self.name,self.complete, self.posts_full]))
        s2 = ""
        for item in self.participants:
            s2 += str(item) + "\t"
        s += "Participants:- {}\n".format(s2)
        return s
        
n = int(input())
participants = []
for _ in range(n):
    i = input().split()
    participants.append(Participant(i[0], list(map(int, i[1:]))))

m = int(input())
projects = []
for _ in range(m):
    j = input().split()
    projects.append(Project(j[0], list(map(int, j[1:]))))

complete_proj = []
placed_particip = []

for student in participants:
    for proj in projects:
            if student.placed:
                placed_particip.append(student)
                del student
                break
            for ind, skill in enumerate(proj.skills):
                if student.skills[ind] >= skill and not proj.posts_full[ind]:
                    student.project = [proj.name, ind]
                    student.placed = True
                    proj.posts_full[ind] = True
                    proj.participants.append(student)
                    if proj.is_complete():
                        complete_proj.append(proj)
                        del proj
                    break

for student in participants:
    for proj in projects:
        if student.placed:
            placed_particip.append(student)
            del student
            break
        for ind, skill in enumerate(proj.skills):
            if student.skills[ind] == skill-1 and not proj.posts_full[ind]:
                can_mentor = False
                for member in proj.participants:
                    if member.skills[ind] > skill and not member.is_mentoring:
                        can_mentor = True
                        mentor = member
                        break
                if not can_mentor:
                    break
                mentor.is_mentoring = True
                student.project = [proj.name, ind]
                student.placed = True
                proj.posts_full[ind] = True
                proj.participants.append(student)
                if proj.is_complete():
                    complete_proj.append(proj)
                    del proj
                break


print("The no. of completed projects: ", len(complete_proj))

