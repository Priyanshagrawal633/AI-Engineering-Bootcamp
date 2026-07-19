import tiktoken
encoding = tiktoken.encoding_for_model("gpt-4")
text= input("Enter your text: ")
token_ids=encoding.encode(text)
tokens = [encoding.decode([token]) for token in token_ids]
print("\n=======Token Analysis=======\n")
print(f"original text: {text}")
print(f"token count: {len(token_ids)}")
print(f"token ids: {token_ids}")

print("\n=======Token Breakdown=======\n")
for index, token in enumerate(tokens,start=1):
    print(f"{index}. {repr(token)}")