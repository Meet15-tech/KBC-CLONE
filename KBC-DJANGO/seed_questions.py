import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kbc_project.settings")
django.setup()

from kbc.models import Question

Question.objects.all().delete()

questions = [
    # SIMPLE 1-20
    ("What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", "B", "simple"),
    ("How many colors are there in a rainbow?", "5", "6", "7", "8", "C", "simple"),
    ("Which animal is known as the King of the Jungle?", "Tiger", "Lion", "Elephant", "Leopard", "B", "simple"),
    ("What is the national bird of India?", "Peacock", "Sparrow", "Eagle", "Parrot", "A", "simple"),
    ("How many days are there in a leap year?", "364", "365", "366", "367", "C", "simple"),
    ("Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", "B", "simple"),
    ("What is the chemical formula of water?", "H2O", "CO2", "O2", "NaCl", "A", "simple"),
    ("Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "C", "simple"),
    ("Which organ pumps blood in the human body?", "Lungs", "Brain", "Heart", "Liver", "C", "simple"),
    ("What is the square root of 64?", "6", "7", "8", "9", "C", "simple"),
    ("What is the national animal of India?", "Tiger", "Lion", "Elephant", "Horse", "A", "simple"),
    ("Which vitamin is obtained from sunlight?", "Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "D", "simple"),
    ("How many hours are there in a day?", "12", "18", "24", "36", "C", "simple"),
    ("What is the freezing point of water in Celsius?", "0°C", "10°C", "50°C", "100°C", "A", "simple"),
    ("Which device is used to measure temperature?", "Thermometer", "Barometer", "Telescope", "Microscope", "A", "simple"),
    ("What is the largest ocean on Earth?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", "D", "simple"),
    ("Which country is famous for the Eiffel Tower?", "Italy", "Germany", "France", "Spain", "C", "simple"),
    ("What is the currency of Japan?", "Yen", "Dollar", "Rupee", "Euro", "A", "simple"),
    ("Which planet is closest to the Sun?", "Mercury", "Venus", "Earth", "Mars", "A", "simple"),
    ("Who invented the telephone?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Isaac Newton", "A", "simple"),

    # MEDIUM 21-40
    ("Who developed Python programming language?", "James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "B", "medium"),
    ("Which is the fastest land animal?", "Lion", "Tiger", "Cheetah", "Horse", "C", "medium"),
    ("Who wrote the Indian national anthem?", "Rabindranath Tagore", "Mahatma Gandhi", "Bankim Chandra Chatterjee", "Sarojini Naidu", "A", "medium"),
    ("Which language is used to create web pages?", "Python", "HTML", "Java", "C++", "B", "medium"),
    ("Which is the largest continent in the world?", "Africa", "Europe", "Asia", "Australia", "C", "medium"),
    ("What is the largest desert in the world?", "Sahara Desert", "Gobi Desert", "Arabian Desert", "Kalahari Desert", "A", "medium"),
    ("Which is the longest river in the world?", "Amazon River", "Nile River", "Ganges River", "Yangtze River", "B", "medium"),
    ("Who is known as the Father of Computers?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", "A", "medium"),
    ("Which country has the largest population in the world?", "India", "USA", "China", "Russia", "C", "medium"),
    ("What is the boiling point of water in Celsius?", "90°C", "100°C", "110°C", "120°C", "B", "medium"),
    ("Which planet has rings around it?", "Earth", "Mars", "Saturn", "Venus", "C", "medium"),
    ("Which instrument is used to see stars and planets?", "Microscope", "Telescope", "Thermometer", "Barometer", "B", "medium"),
    ("How many players are there in a cricket team?", "9", "10", "11", "12", "C", "medium"),
    ("What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", "C", "medium"),
    ("Which metal is liquid at room temperature?", "Iron", "Mercury", "Gold", "Silver", "B", "medium"),
    ("Who wrote the famous play Romeo and Juliet?", "William Shakespeare", "Charles Dickens", "Leo Tolstoy", "Mark Twain", "A", "medium"),
    ("Which blood group is known as the universal donor?", "A+", "B+", "AB+", "O-", "D", "medium"),
    ("What is the largest organ in the human body?", "Heart", "Liver", "Skin", "Brain", "C", "medium"),
    ("Which planet is known as the Morning Star?", "Mercury", "Venus", "Earth", "Mars", "B", "medium"),
    ("Which country gifted the Statue of Liberty to the USA?", "Germany", "France", "England", "Canada", "B", "medium"),

    # HARD 41-60
    ("What is the hardest natural substance on Earth?", "Gold", "Diamond", "Iron", "Platinum", "B", "hard"),
    ("Who discovered gravity?", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla", "A", "hard"),
    ("Which is the smallest continent in the world?", "Asia", "Australia", "Europe", "Antarctica", "B", "hard"),
    ("What is the currency of the United Kingdom?", "Dollar", "Pound Sterling", "Euro", "Yen", "B", "hard"),
    ("Which gas is most abundant in Earth's atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "B", "hard"),
    ("Which Indian scientist is known as the Missile Man of India?", "Homi Bhabha", "Vikram Sarabhai", "A.P.J. Abdul Kalam", "C.V. Raman", "C", "hard"),
    ("What is the speed of light in vacuum?", "3 × 10⁸ m/s", "3 × 10⁶ m/s", "3 × 10⁴ m/s", "3 × 10² m/s", "A", "hard"),
    ("Which is the largest country in the world by area?", "USA", "China", "Russia", "Canada", "C", "hard"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo", "A", "hard"),
    ("Which is the national game of India?", "Hockey", "Cricket", "Football", "Kabaddi", "A", "hard"),
    ("How many bones are there in an adult human body?", "206", "208", "210", "212", "A", "hard"),
    ("Which planet is called the Blue Planet?", "Mars", "Earth", "Neptune", "Jupiter", "B", "hard"),
    ("What does CPU stand for in computers?", "Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Control Processing Unit", "A", "hard"),
    ("Who was the first President of India?", "Jawaharlal Nehru", "Rajendra Prasad", "Sardar Patel", "B.R. Ambedkar", "B", "hard"),
    ("Which is the longest bone in the human body?", "Femur", "Tibia", "Humerus", "Fibula", "A", "hard"),
    ("What is the currency of China?", "Yen", "Dollar", "Yuan", "Won", "C", "hard"),
    ("Which gas is used for breathing by humans?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", "A", "hard"),
    ("Who invented the light bulb?", "Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "James Watt", "A", "hard"),
    ("Which Indian city is known as the Pink City?", "Jaipur", "Jodhpur", "Udaipur", "Delhi", "A", "hard"),
    ("Which is the largest island in the world?", "Greenland", "Madagascar", "Australia", "Borneo", "A", "hard"),

    # HARDEST 61-80
    ("What is the capital of Canada?", "Toronto", "Ottawa", "Vancouver", "Montreal", "B", "hardest"),
    ("Which element has the chemical symbol 'Au'?", "Silver", "Gold", "Iron", "Copper", "B", "hardest"),
    ("Who wrote the Ramayana?", "Valmiki", "Tulsidas", "Ved Vyasa", "Kalidasa", "A", "hardest"),
    ("How many states are there in India?", "28", "29", "30", "31", "A", "hardest"),
    ("Which bird can mimic human speech?", "Parrot", "Crow", "Eagle", "Sparrow", "A", "hardest"),
    ("Which ocean lies between Africa and Australia?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "C", "hardest"),
    ("What is the SI unit of force?", "Newton", "Joule", "Watt", "Pascal", "A", "hardest"),
    ("Which planet is the largest in the Solar System?", "Saturn", "Jupiter", "Mars", "Neptune", "B", "hardest"),
    ("Who is known as the Father of the Nation in India?", "Mahatma Gandhi", "Subhash Chandra Bose", "Jawaharlal Nehru", "Bhagat Singh", "A", "hardest"),
    ("Which part of the plant absorbs water from soil?", "Stem", "Leaf", "Root", "Flower", "C", "hardest"),
    ("What is the freezing point of water in Fahrenheit?", "32°F", "0°F", "100°F", "212°F", "A", "hardest"),
    ("Which device converts electrical energy into mechanical energy?", "Generator", "Motor", "Transformer", "Battery", "B", "hardest"),
    ("Which country is known as the Land of the Rising Sun?", "China", "Japan", "Thailand", "Korea", "B", "hardest"),
    ("Who invented the World Wide Web?", "Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Mark Zuckerberg", "A", "hardest"),
    ("Which gas is filled inside balloons to make them float?", "Oxygen", "Hydrogen", "Helium", "Nitrogen", "C", "hardest"),
    ("Which continent is known as the Dark Continent?", "Asia", "Africa", "Europe", "Australia", "B", "hardest"),
    ("What is the capital city of Brazil?", "Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador", "C", "hardest"),
    ("Which instrument is used to measure earthquakes?", "Barometer", "Seismograph", "Thermometer", "Telescope", "B", "hardest"),
    ("Who discovered penicillin?", "Alexander Fleming", "Louis Pasteur", "Marie Curie", "Isaac Newton", "A", "hardest"),
    ("How many planets are there in the Solar System?", "7", "8", "9", "10", "B", "hardest"),

    # EXTREME 81-90
    ("Which country is famous for the Great Wall?", "India", "Japan", "China", "South Korea", "C", "extreme"),
    ("What is the hardest substance in the human body?", "Enamel", "Bone", "Nail", "Hair", "A", "extreme"),
    ("Which is the largest volcano in the Solar System?", "Mount Everest", "Olympus Mons", "Mount Fuji", "Mauna Loa", "B", "extreme"),
    ("What is the study of earthquakes called?", "Geology", "Seismology", "Astronomy", "Meteorology", "B", "extreme"),
    ("Who wrote the famous Harry Potter book series?", "J.R.R. Tolkien", "J.K. Rowling", "George Orwell", "Agatha Christie", "B", "extreme"),
    ("Which blood cells help in fighting diseases?", "Red Blood Cells", "White Blood Cells", "Platelets", "Plasma", "B", "extreme"),
    ("Which is the largest freshwater lake in the world?", "Lake Victoria", "Lake Superior", "Lake Baikal", "Caspian Sea", "B", "extreme"),
    ("Which country has the most time zones?", "Russia", "USA", "France", "China", "A", "extreme"),
    ("What is the smallest unit of matter?", "Molecule", "Atom", "Electron", "Proton", "B", "extreme"),
    ("Who invented the airplane?", "Wright Brothers", "Thomas Edison", "Nikola Tesla", "Galileo Galilei", "A", "extreme"),

    # ULTIMATE 91-100
    ("What is the name of the first artificial satellite launched into space?", "Sputnik 1", "Apollo 11", "Voyager 1", "Explorer 1", "A", "ultimate"),
    ("Which mathematician is known for the Last Theorem proved by Andrew Wiles in 1994?", "Isaac Newton", "Pierre de Fermat", "Euclid", "Carl Gauss", "B", "ultimate"),
    ("Which country was formerly known as Abyssinia?", "Ethiopia", "Egypt", "Sudan", "Libya", "A", "ultimate"),
    ("What is the SI unit of electric conductance?", "Siemens", "Ohm", "Henry", "Farad", "A", "ultimate"),
    ("Which element has the highest melting point among all pure metals?", "Tungsten", "Iron", "Platinum", "Titanium", "A", "ultimate"),
    ("What is the name of the deepest known point in Earth's oceans?", "Mariana Trench", "Challenger Deep", "Java Trench", "Tonga Trench", "B", "ultimate"),
    ("Who composed the famous classical piece 'The Four Seasons'?", "Mozart", "Beethoven", "Antonio Vivaldi", "Bach", "C", "ultimate"),
    ("Which ancient civilization built the city of Machu Picchu?", "Roman", "Greek", "Inca", "Egyptian", "C", "ultimate"),
    ("In computer science, what does SQL stand for?", "Standard Query Language", "Structured Query Language", "Simple Question Language", "System Query Logic", "B", "ultimate"),
    ("Which scientist proposed the uncertainty principle in quantum mechanics?", "Albert Einstein", "Niels Bohr", "Werner Heisenberg", "Max Planck", "C", "ultimate"),
]

for q in questions:
    Question.objects.create(
        question=q[0],
        option_a=q[1],
        option_b=q[2],
        option_c=q[3],
        option_d=q[4],
        answer=q[5],
        difficulty=q[6]
    )

print("100 questions inserted successfully!")
print("Total questions:", Question.objects.count())