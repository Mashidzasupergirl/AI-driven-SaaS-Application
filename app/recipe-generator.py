from openai import OpenAI
import argparse

 


def main():
    print("Recipehelper is running!")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print("List of products from input:", user_input)
    generate_recipe(user_input)

    pass

def generate_recipe(prompt: str):
    client = OpenAI()

    subject = prompt

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a generetor of recipe for a written products"},
        {"role": "user", "content": f'{subject}'}
    ]
    )
    AI_answer = completion.choices[0].message

    recipe_name = AI_answer.content.split('\n')[0].split(': ')[-1]

    print(recipe_name, 'recipe name')
    pass


if __name__ == "__main__":
    main()
