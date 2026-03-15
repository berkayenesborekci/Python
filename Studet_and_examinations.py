import pandas as pd
def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    students_subjects = students.merge(subjects, how='cross')
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    return (
        students_subjects
        .merge(exam_counts, on=['student_id', 'subject_name'], how='left')
        .fillna({'attended_exams': 0})
        .astype({'attended_exams': 'Int64'})
        .sort_values(['student_id', 'subject_name'])
        .reset_index(drop=True)
    )
#pandas_schema
#data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
#students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
#data = [['Math'], ['Physics'], ['Programming']]
#subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
#data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
#examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})