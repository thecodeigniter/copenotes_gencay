import random
def generate(random_chars=12, alphabet="0123456789abcdefghijklmnopqrstABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    r = random.SystemRandom()
    return ''.join([r.choice(alphabet) for i in range(random_chars)])