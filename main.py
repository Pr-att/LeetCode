import openai

openai.api_key = "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"
print(openai.Image.create(
    prompt="alien with apple",
    n=1,
    size="1024x1024",
    response_format="url",
))