nomre = {"riazi": 20, "farsi": 18, "shimi": 19}
print(nomre)

student_nomre = {"jadi": {"riazi": 20, "farsi": 18, "shimi": 19}, "mahan": {"riazi": 20, "farsi": 19, "shimi": 17}, "mohammad": {"riazi": 10, "farsi": 20, "shimi": 16}, "reza": {"riazi": 14, "farsi": 16, "shimi": 2}}
print(student_nomre)

print(student_nomre["mahan"]["riazi"])

print(student_nomre.keys())
print(student_nomre.values())
print(student_nomre.items())

print(student_nomre.get("jadi", False))
print(student_nomre.get("gholam", False))