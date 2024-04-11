import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('YOUR_API_KEY')
genai.configure(api_key=client_id)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 8192,
}

safety_settings = [
]

model = genai.GenerativeModel(model_name="tunedModels/legallybot-nmz2rvthhb9b",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "input: When can the Enrollment Application can be obtained from Bar Council?",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)