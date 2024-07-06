import openai
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.Codegenerator import CodeGenerator

class Main():
       
    def main_fun(self, api_key, programming_languages, image_path, prompt):
        
        openai.api_key = api_key
        self.code_generator = CodeGenerator()
        
        self.result = self.code_generator.code_generating_agent(
            image_path, 
            programming_languages,
            prompt
            )
        
        #checking if our agenr has retuned a error or a generated code 
        if "Error" in self.result:
            return self.result 
        else:
            return self.result.choices[0].message.content