import os

from openai import OpenAI

def fourth():
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    # Sending a prompt to your fine-tuned model
    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::97QirxUL",  # Your model's name
        messages=[
            {"role": "system",
             "content": "You are tutor for students that are learning for a business administration course."},
            {"role": "user", "content": "Was ist der Unterschied zwischen der kurzfristigen Preisuntergrenze und den Selbstkosten?"}  # Your test prompt
        ]
    )

    # Printing the response
    print(completion.choices[0].message)

if __name__ == '__main__':
    fourth()
