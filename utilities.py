def convert_score_to_grade(score: float) -> str:
    if score >= 80: return "A"
    elif score >= 75: return "B+"
    elif score >= 70: return "B"
    elif score >= 65: return "C+"
    elif score >= 60: return "C"
    elif score >= 55: return "D+"
    elif score >= 50: return "D"
    else: return "F"

def convert_grade_to_comment(student_id: str, name: str, subject: str, grade: str) -> str:
    if grade == "A": return f"{name} (ID: {student_id}) is Excelent in {subject}"
    elif grade == "B+": return f"{name} (ID: {student_id}) is Good in {subject}"
    elif grade == "B": return f"{name} (ID: {student_id}) is Good in {subject}"
    elif grade == "C+": return f"{name} (ID: {student_id}) is Normal in {subject}"
    elif grade == "C": return f"{name} (ID: {student_id}) is Normal in {subject}"
    elif grade == "D+": return f"{name} (ID: {student_id}) is Bad in {subject}"
    elif grade == "D": return f"{name} (ID: {student_id}) is Bad in {subject}"
    else: return f"{name} (ID: {student_id}) is Fail in {subject}"