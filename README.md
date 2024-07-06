# Screenshot-to-Code

Converts your Screenshots to Html, Css or React or Flutters code as per your need.
Used gpt-4 omini so you would require an openAI api_key.

# Running the Project:
Go to the backendfolder --> Codegenerator.py  -->  line9: template_dir = 'D:\\Image code generator\\Screenshot-to-Code\\backend' (path for template.j2)
Change it according to the directory you have cloned the project in, you can do it by simply right clicking on the template.j2 --> copy path --> swap it with the one already on line9 in Codegenerator.py.

- cd frontend
- start interface.html
- python flask_app.py

The uploaded image will be visible on the right, just like in the screenshot below.
- ![image](https://github.com/MohsinAliIrfan/Screenshot-to-Code/assets/80330344/fab440b4-0485-403c-b2e3-21b6d56a5c95)


THATS IT!!

The backend directory holds all the backend working of the website which includes code generating agent, image conversion, jira termplate, dealing with possible error.
I have also inluded some images directly in the backend direcory so you can test the backend directly if required without running the frontend.
so, for that
- cd backend

In the main.py file, include your api key and call the function(), and you can see the output directly in your console.
