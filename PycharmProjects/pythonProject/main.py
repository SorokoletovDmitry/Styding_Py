def calculate_average(scores):
    # Функция для расчета среднего балла
    total = sum(scores)
    average = total / len(scores)
    return average

def get_exam_results(filename):
    # Функция для получения результатов экзамена из файла
    results = {}
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split()
            score = int(score)

            if name in results:
                results[name].append(score)
            else:
                results[name] = [score]

    return results


def get_students_with_high_grades(filename):
    # Функция для получения списка фамилий студентов с высокими оценками
    results = get_exam_results(filename)
    class_avg = calculate_average([score for scores in results.values() for score in scores])

    students = []

    for name, scores in results.items():
        avg = calculate_average(scores)
        if avg >= (class_avg + 3):
            diff = avg - class_avg
            students.append((name, diff))

    return students


# Пример использования:
filename = 'grades.txt'
students = get_students_with_high_grades(filename)

for student, diff in students:
    print(f"Студент {student} - отличник. Средний балл выше среднего класса на {diff}")