response = client.chat.completions.create(
    model="example-3.5-turbo",
    messages=messages,
    temperature=0,
    max_tokens=1000
)
