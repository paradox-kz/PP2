from functools import reduce
print("\n" + "=" * 50)
print("Exercise 3: enumerate() and zip()")
print("=" * 50)
 
# enumerate: пронумеровать задачи
tasks = ["Write tests", "Fix bug", "Deploy app", "Update docs"]
print("Task list:")
for i, task in enumerate(tasks, start=1):
    print(f"  {i}. {task}")
 
# enumerate: найти индекс конкретного элемента
for i, task in enumerate(tasks):
    if task == "Fix bug":
        print(f"\n'Fix bug' is at index {i}")
 
# zip: объединить студентов с оценками
students = ["Alice", "Bob", "Charlie", "Diana"]
scores   = [88, 72, 95, 61]
grades   = ["B", "C", "A", "D"]
 
print("\nStudent report:")
for name, score, grade in zip(students, scores, grades):
    status = "PASS" if score >= 70 else "FAIL"
    print(f"  {name:10} | {score:3} | {grade} | {status}")
 
# zip для создания словаря
score_dict = dict(zip(students, scores))
print("\nScore dictionary:", score_dict)
 
# zip с enumerate вместе
print("\nIndexed pairs:")
for i, (name, score) in enumerate(zip(students, scores), start=1):
    print(f"  #{i} {name}: {score}")