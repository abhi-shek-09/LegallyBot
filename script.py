import pprint
import google.generativeai as genai
from load_creds import load_creds

creds = load_creds()

genai.configure(credentials=creds)

print()
name = "legallybot-nmz2rvthhb9b"
model = genai.GenerativeModel(model_name=f'tunedModels/{name}')

result = model.generate_content('When can the Enrollment Application can be obtained from Bar Council?')
print(result.text)