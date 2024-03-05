import random
import string

# Define the number of random paths you want to generate
num_paths = 10000

# Define the length range for the random paths
min_length = 4
max_length = 10

# Define the starting words for the paths
starting_words = ['admin', 'login', 'dashboard', 'user', 'panel', 'control', 'secure', 'access',
                  'inicio', 'entrada', 'perfil', 'usuario', 'administrador', 'acceso', 'seguro']

# Define the possible endings for the paths
path_endings = ['.php', '.asp', '.js', '.html']

# Generate random paths
paths = []
for _ in range(num_paths):
    path_length = random.randint(min_length, max_length)
    starting_word = random.choice(starting_words)
    remaining_length = path_length - len(starting_word)
    random_path = starting_word + ''.join(random.choices(string.ascii_lowercase, k=remaining_length))
    random_path += random.choice(path_endings)
    paths.append(random_path)

# Write the generated paths to PATH.py
with open('PATH.py', 'w') as file:
    file.write('paths = [\n')
    for path in paths:
        file.write(f'    "{path}",\n')
    file.write(']\n')

print("Random paths generated and imported into PATH.py successfully!")
