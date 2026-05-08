from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best = ("none", 0)

    for student, score in scores:
        best_name, best_score = best
        if score > best_score:
            best = (student, score)

    return best[0]


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
