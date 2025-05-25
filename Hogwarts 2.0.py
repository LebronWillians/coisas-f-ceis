print("🧙 Welcome to Hogwarts! Step up to the Sorting Hat...")
print("Sorting Hat: Come closer, I must read you...")

houses = {
    'Gryffindor': 0,
    'Ravenclaw': 0,
    'Hufflepuff': 0,
    'Slytherin': 0
}

def score(answer, house_map):                                                 #def -> define uma função, sendo score o nome dessa função
    for key, value in house_map.items():
        if answer == key:
            houses[value] += 2
            return
        print('Invalid Answer')

questions = [                                                                 # [] p/ abrir a lista de perguntas
    ("Q1) When I'm dead, I want people to remember me as:",
     ['1) The Good', '2) The Great', '3) The Wise', '4) The Bold'],           # [] p/ abrir a liasta da=e alternativas
     {1:'Hufflepuff', 2: 'Slytherin', 3:'Ravenclaw', 4:'Gryfindor'}),         # {} p/ validar as casas, validando a linha 13 e 14

    ('Q2) You see someone being bullied in the hallway. What do you do?',
     ['1) Stand up to the bully', '2) Tell a teacher', '3) Try to outsmart the bully whith wit', '4) Help the person feel better later'],
     {1:'Gryffindor', 2:'Slytherin', 3:'Ravenclaw', 4:'Hufflepuff'}),

    ('Q3) Which of these word you must people to call you?',
      ['1) Cowardly', '2) Ignorant', '3)Ordinary', '4) Selfish'],
      {1:'Gryffinfor', 2:'Ravenclaw', 3:'Slytherin', 4:'Hufflepuff'}),

    ('Q4) What dp you value most in a friend?',
     ['1) Loyalty', '2) Intelligence', '3) Ambition', '4) Courage'],
     {1:'Hufflepuff', 2:'Ravenclaw', 3:'Slytherin', 4:'Gryffindor'}),

    ('Q5) Wich magical creature do you fell most connected to?',
     ['1) Phoenix', '2) Dragon', '3) Badger', '4) Eagle'],
     {1:'Gryffindor', 2:'Slytherin', 3:'Hufflepuff', 4:'Ravenclaw'}),

    ('Q6) How would you spend a free afternoon at Hogwarts?',
     ['1) Praticing spells', '2) Studying in the library', '3) Hanging out with friends', '4) Exploring secret passages'],
     {1:'Gryffindor', 2:'Ravenclaw', 3:'Hufflepuff', 4:'Sçytherin'}),

    ("Q7) Which potion would you choose to brew?",
     ["1) Love", "2) Wisdom", "3) Courage", "4) Power"],
     {1: "Hufflepuff", 2: "Ravenclaw", 3: "Gryffindor", 4: "Slytherin"}),

    ("Q8) Pick a class at Hogwarts:",
     ["1) Herbology", "2) Defense Against the Dark Arts", "3) Potions", "4) Astronomy"],
     {1: "Hufflepuff", 2: "Gryffindor", 3: "Slytherin", 4: "Ravenclaw"}),

    ("Q9) What do you fear most?",
     ["1) Being alone", "2) Being defeated", "3) Being misunderstood", "4) Being bored"],
     {1: "Hufflepuff", 2: "Gryffindor", 3: "Slytherin", 4: "Ravenclaw"}),

    ("Q10) What would you do if you found a wallet on the ground?",
     ["1) Return it", "2) Keep it but feel bad", "3) Look for ID", "4) Take the money"],
     {1: "Hufflepuff", 2: "Gryffindor", 3: "Ravenclaw", 4: "Slytherin"}),

    ("Q11) Choose a weapon:",
        ["1) Wand", "2) Sword", "3) Book", "4) Cloak"],
        {1: "Hufflepuff", 2: "Gryffindor", 3: "Ravenclaw", 4: "Slytherin"}),
   
    ("Q12) Which quality do you most admire?",
        ["1) Determination", "2) Creativity", "3) Kindness", "4) Cunning"],
        {1: "Gryffindor", 2: "Ravenclaw", 3: "Hufflepuff", 4: "Slytherin"}),
   
    ("Q13) Your ideal pet is:",
        ["1) Owl", "2) Cat", "3) Snake", "4) Badger"],
        {1: "Ravenclaw", 2: "Gryffindor", 3: "Slytherin", 4: "Hufflepuff"}),
   
    ("Q14) Pick a path through the forest:",
        ["1) Sunny trail", "2) Shadowy path", "3) Mysterious route", "4) Steep challenge"],
        {1: "Hufflepuff", 2: "Slytherin", 3: "Ravenclaw", 4: "Gryffindor"}),
   
    ("Q15) What's your dream job?",
            ["1) Teacher", "2) Healer", "3) Politician", "4) Explorer"],
            {1: "Ravenclaw", 2: "Hufflepuff", 3: "Slytherin", 4: "Gryffindor"}),
       
    ("Q16) What kind of book would you read?",
            ["1) Fantasy", "2) Mystery", "3) Biography", "4) Self-help"],
            {1: "Gryffindor", 2: "Ravenclaw", 3: "Hufflepuff", 4: "Slytherin"}),
       
    ("Q17) What motivates you the most?",
            ["1) Justice", "2) Knowledge", "3) Success", "4) Friendship"],
            {1: "Gryffindor", 2: "Ravenclaw", 3: "Slytherin", 4: "Hufflepuff"}),
       
    ("Q18) Which spell would you cast first?",
            ["1) Lumos", "2) Accio", "3) Expelliarmus", "4) Alohomora"],
            {1: "Ravenclaw", 2: "Hufflepuff", 3: "Gryffindor", 4: "Slytherin"}),
       
    ("Q19) What's your favorite time of day?",
            ["1) Morning", "2) Afternoon", "3) Evening", "4) Midnight"],
            {1: "Hufflepuff", 2: "Gryffindor", 3: "Ravenclaw", 4: "Slytherin"}),
       
    ("Q20) What's more important?",
            ["1) Loyalty", "2) Bravery", "3) Wisdom", "4) Ambition"],
            {1: "Hufflepuff", 2: "Gryffindor", 3: "Ravenclaw", 4: "Slytherin"}),
]

for q, option, mapping in questions:
    print('\n' + q)
    for opt in option:
        print(opt)
    try:
        ans = int(input('Your Answer'))
        score(ans, mapping)
    except: 
        print('Please, put a number between 1-4.')

print('\n Final Points:')
for house, points in houses.items():
    print(f"{houses}: {points}")

max_score = max(houses.values())
top_houses = [house for house, score in houses.items() if score == max_score]

print('\n Sporting Result')
if len(top_houses) == 1:
    chosen = top_houses[0]
    print(f'The Sorting Hat has decided: {chosen.upper()}!')
else:
    print("It's tie between:", ' and '.join(top_houses))
    print("The Sorting Hat is undecided - you show traits of multiple houses!")