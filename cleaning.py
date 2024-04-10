# import re
# import pandas as pd

# with open('dummy.txt', 'r') as file:
#     text = file.read()
# qa_pairs = re.split(r'\bQ:\s*', text)[1:]
# questions_answers = []
# questions = []
# answers = []
# for qa_pair in qa_pairs:
#     question, answer = qa_pair.split(':', 1)
#     question = question[:-2]
#     questions.append(question)
#     answers.append(answer)
#     questions_answers.append((question.strip(), answer.strip()))

# df = pd.DataFrame()
# df['Header'] = questions
# df['Description'] = answers
# df2 = pd.read_csv('check.csv')
# combined_df = pd.concat([df, df2], axis=0, ignore_index=True)
# print(len(combined_df))
# combined_df.to_csv('check2.csv', index = False)

#PART 2 OF CLEANING

# import re
# import pandas as pd

# with open('dummy2.txt', 'r') as file:
#     text = file.read()
# qa_pairs = re.split(r'Q\. No\.\s*\d+\s*:', text)[1:]
# questions = []
# answers = []
# for qa_pair in qa_pairs:
#     question, answer = qa_pair.split('Ans:', 1)
#     questions.append(question.strip())
#     answers.append(answer.strip())

# df = pd.DataFrame()
# df['Header'] = questions
# df['Description'] = answers
# df2 = pd.read_csv('check2.csv')
# combined_df = pd.concat([df2, df], axis=0, ignore_index=True)
# print(len(combined_df))
# combined_df.to_csv('check3.csv', index = False)


#PART 3 OF CLEANING

import re
import pandas as pd

with open('dummy9.txt', 'r', encoding='utf-8') as file:
    text = file.read()
qa_pairs = re.split(r'Q\d+\. ', text)[1:]
questions = []
answers = []
for qa_pair in qa_pairs:
    question, answer = qa_pair.split('Ans. ', 1)
    questions.append(question.strip())
    answers.append(answer.strip())

df = pd.DataFrame()
df['Header'] = questions
df['Description'] = answers
df2 = pd.read_csv('check8.csv')
combined_df = pd.concat([df2, df], axis=0, ignore_index=True)
print(len(combined_df))
combined_df.to_csv('check9.csv', index = False)