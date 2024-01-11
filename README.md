# AI-driven-SaaS-Application
Python, React, TS, AWS

# To run app:
cd app 
uvicorn api_recipe_generator:app --reload

# To check Open AI API:

1st option:
cd app 
python3 recipe_generator.py --input 'nuts, orange, honey'
(print(recipe, 'recipe') should be uncommented)

2nd option:
Go to http://127.0.0.1:8000/docs#/default/generate_recipe_api_generate_recipe_get
Execute get request in generate_recipe

3rd option:
Make a request in browser:
http://127.0.0.1:8000/generate_recipe?prompt=orange%2C%20honey

