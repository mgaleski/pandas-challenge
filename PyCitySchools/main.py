import pandas as pd
import numpy as np

schools_df = pd.read_csv('./Resources/schools_complete.csv')
students_df = pd.read_csv('./Resources/students_complete.csv')

school_count = schools_df['School ID'].count()
student_count = students_df['Student ID'].count()
school_count = schools_df['School ID'].count()
total_budget = schools_df['budget'].sum()
average_math_score = students_df['math_score'].mean()
average_reading_score = students_df['reading_score'].mean()

math_passing = students_df[students_df.math_score >= 70]
reading_passing = students_df[students_df.reading_score >= 70]

math_pass_rate = math_passing['Student ID'].count()*100/student_count
reading_pass_rate = reading_passing['Student ID'].count()*100/student_count

overall_pass_rate = (math_pass_rate + reading_pass_rate)/2



district_summary = pd.DataFrame(
        {'Total Schools': [school_count],
         'Total Students': [student_count],
         'Total Budget': [total_budget],
         'Average Math Score': [average_math_score],
         'Average Reading Score': [average_reading_score],
        '% Passing Math': [f'{math_pass_rate}%'],
         '% Passing Reading':  [f'{reading_pass_rate}%'],
         'Overall Passing Rate': [f'{overall_pass_rate}%']})
