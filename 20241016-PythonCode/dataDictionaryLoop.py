learners = [
    {"name": "Carolina Cenacchi", "level": 3, "target": "Pass"},
    {"name": "Raolf Loret", "level": 2, "target": "Pass"},
    {"name": "Alexei Sokolov", "level": 4, "target": "Pass"},
    {"name": "Aman Nwosu", "level": 1, "target": "Merit"},
    {"name": "Irina Zaytesev", "level": 3, "target": "Merit"},
    {"name": "Ida Andersen", "level": 3, "target": "Distinction"},
    {"name":"Mi Rou-Wan", "level": 4, "target": "Pass"},
    {"name": "Malcom Johnson", "level": 5, "target": "Merit"},
    {"name": "Leah Bolm", "level": 3, "target": "Distinction"},
    {"name": "Bahiah Medhat", "level": 3, "target": "Pass"},
    {"name": "Mah Ning", "level": 2, "target": "Merit"},
    {"name": "Husrev Aksu", "level": 2, "target": "Merit"},
    {"name": "Janan Al-Fayyoumi", "level": 4, "target": "Pass"},
    {"name": "Hessa Diba", "level": 3, "target": "Pass"},
    {"name": "Marie Smerdel", "level": 3, "target": "Distinction"}
]

# Start Writing Your Code Here

for learner in learners:
    name = learner["name"]
    level = learner["level"]
    grade = learner["target"]
    message = f"This is {name}. They are on a Level {level} course, and their target grade is {grade}."
    print(message)
