import ell

ell.init(verbose=True)

@ell.simple(model="gpt-4o")
def hello(name: str):
    """You are a helpful assistant.""" # System prompt
    return f"Say hello to {name}!" # User prompt

greeting = hello("Dan McAteer")
print(greeting)