import os
from jinja2 import Environment, FileSystemLoader
import base64
import openai

class CodeGenerator():
    def __init__(self):
        # Absolute path to the directory containing the template file
        template_dir = 'D:\\Image code generator\\Screenshot-to-Code\\backend'
        print("Template directory:", template_dir)
        
        #check if the template file exists
        if not os.path.exists(os.path.join(template_dir, 'template.j2')):
            print("Template file does not exist in the specified directory.")
        else:
            print("Template file found.")

        self.file_loader = FileSystemLoader(template_dir)
        self.env = Environment(loader=self.file_loader)
        
        try:
            self.template = self.env.get_template('template.j2')
            print("Template loaded successfully.")
        except Exception as e:
            print("Error loading template: ", e)

    def get_template(self):
        return self.env.get_template('template.j2')
    
    def rendering_template(self, image_path=None, languages="HTML CSS", user_prompt="No Prompt"):
        self.template = self.get_template()
        # Create the prompt message using the template
        prompt_message = self.template.render(
            programming_languages=languages,
            prompt=user_prompt
        )
        
        print("prompt_message: ", prompt_message)
        # Return a list of messages in the required format
        return [
            {"role": "system", "content": "Please generate the code according to the prompt provided by the user"},
            {"role": "user", "content": [
                {"type": "text", "text": prompt_message},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{self.image_encoder(image_path)}"
                }}
            ]}
        ]
    
    def image_encoder(self, image_path):
        if image_path:
            with open(image_path, "rb") as image_file:
                finalimage = base64.b64encode(image_file.read()).decode("utf-8")
                return finalimage
        return None
    
    def code_generating_agent(self, image_path, programming_language="HTML CSS", user_prompt="No Prompt"):
        try:
            messages = self.rendering_template(image_path, programming_language, user_prompt)
            return openai.chat.completions.create(
                model="gpt-4o",
                messages=messages,
            )
        except Exception as e:
            print("An error occurred while generating code: ", str(e))
            return str("Error: " + str(e))
