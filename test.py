from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        #{"role": "system", "content": "你是一个大学生"},
        {"role": "user", "content": "描述一下中南财经政法大学统计与数学学院"}
    ]
)

print(completion.choices[0].message)




