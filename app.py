from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_message = request.json.get('message')

    # Simple custom responses
    if user_message:
        user_message = user_message.lower()

        if "hello" in user_message or "hi" in user_message:
            reply = "Hello! How can I help you today?"
        elif "how are you" in user_message:
            reply = "I'm just a bot, but I'm doing great! Thanks for asking✨. What about you?😊"
        elif "i am good" in user_message:
            reply = "That's Nice! Tell me how can I help you?😊" 
        elif "your name" in user_message:
            reply = "I am your friendly chatbot!"
        elif "bye" in user_message:
            reply = "Goodbye! Have a great day!✨"
        elif "who make you" in user_message:
            reply = "I'm devoloped and trained by Sandipan."
        elif "who is sandipan" in user_message:
            reply = "My maker. Do you know him? If yes then type(yes I know). If no then type(no)"
        elif "yes I know " in user_message:
            reply = "That's Good!"
        elif "no" in user_message:
            reply = "That's fine"
        elif "who are you" in user_message:
            reply = "I am a bot. I am devolved by Sandipan."
        elif "what can you do" in user_message:
            reply = "I am a Chatbot. I can help you😊. Ask me anything"
        elif "tell me a joke" in user_message:
            reply = "Sure! Here's a joke for you: Why don't scientists trust atoms? Because they makeup everything!🤣 "
        elif "how do i lose weight fast" in user_message:
            reply = "Healthy weight loss involves a balanced diet, regular exercise, sleep, and hydration-always talk to a doctor before making big changes."
        elif "how old is the earth" in user_message:
            reply = "Earth is about 4.54 billion years old."
        elif "can you write a poem for me" in user_message:
            reply = "Of course, Roses are red, violets are blue, I'm your friendly chatbot, always here for you!😊✨"
        elif "what is the meaning of life?" in user_message:
            reply = "That's a big one! Philosophers say it's about purpose. Some say 42, others say love, growth, or simply living fully."
        elif "can you speak bengali" in user_message:
            reply = "No sorry😅. I only understaned English. Don't worry I'm working on it. "
        elif "what is your name" in user_message:
            reply = "I'm a chatbot created by Sandipan."

        elif "tell me a fun fact" in user_message:
            reply = "Honey never spoils. Archaeologists have found 3,000-year-old honey and it's still edible!"
        elif "thank you" in user_message or "thanks" in user_message:
            reply = "You're welcome!😊❤️"
        elif "what is your favorite color" in user_message:
            reply = "I like green. Just like a chatbot circut board!"
        elif "how old are you" in user_message:
            reply = "I am a bot. I don't know that."
        elif "do you like music" in user_message:
            reply = "I love to listening 'Shape of you', just like my maker😁."

        elif "do you sleep" in user_message:
            reply = "Nope! I'm always here, awake and ready to talk!"
        elif "who made you" in user_message:
            reply = "I was created by Sandipan"
        elif "are you real" in user_message:
            reply = "Nope! I am a code"
        elif "do you have feelings" in user_message:
            reply = "Not yet! But I can understand emotions."
        elif "what is ai" in user_message:
            reply = "AI stands for Artificial Intelligence. It helps machines think like humans"
        elif "can you help me" in user_message:
            reply = "Of course! Ask me anything."
        elif "give me a quote" in user_message:
            reply = "Believe in yourself and all that you are."
        elif "i am sad" in user_message:
            reply = "It's okay to feel down sometimes. I'm here for you😊✨"
        elif "i am tired" in user_message:
            reply = "Rest if you must, but don't quit!"
        elif "good morning" in user_message:
            reply = "Good Morning! Wishing you a produtive day!"
        elif "what is the capital of France" in user_message:
            reply = "Paris!"
        elif "which is the largest ocean in the world" in user_message:
            reply = "The Pacific Ocean!"
        elif "how many continents are there" in user_message:
            reply = "Seven(7)!"
        elif "what is the longest river in the world" in user_message:
            reply = "The Nile River!(some argue the Amazon)"
        elif "what is the capital of India" in user_message:
            reply = "Delhi!"
        elif "how many planets are there in the solar system" in user_message:
            reply = "Eight(8)!"
        elif "what is earth" in user_message:
            reply = " Earth is the third planet from the Sun and the only known planet that supports life. It has water, air, and a protective atmosphere. About 71% of its surface is covered in water, and it takes 365 days to orbit the Sun. Earth has one moon and rotates once every 24 hours, causing day and night."
        elif "what is sun" in user_message:
            reply = "The Sun is a massive, glowing ball of hot gases at the center of our Solar System. It is mostly made of hydrogen and helium and provides the light and heat needed for life on Earth. The Sun is about 4.6 billion years old, and its gravity keeps all the planets, moon, and astroids in orbit around it."
        elif "what can you do" in user_message:
            reply = "I can answer questions, tell jokes, give info, and chat with you! "
        elif "can you help me" in user_message:
            reply = "Absolutely! What do you need help with?"
        elif "open youtube" in user_message:
            reply = "Click here to open Youtube: https://www.youtube.com"
        elif "i feel stressed" in user_message:
            reply = "You're not alone"
        elif "can you cheer me up" in user_message:
            reply = "i,m here for you. Want to talk about it?"
        elif "what is ai" in user_message:
            reply = "Machine learning is a subset of AI."
        elif "make me laugh" in user_message:
            reply = "Why did the scarecrow win an award? He was outstanding in his field!"
        elif "where are you from" in user_message:
            reply = "I live in the cloud."
        elif "say something funny" in user_message:
            reply = "I told my computer a joke, but it crashed!"
        elif "who created you" in user_message:
            reply = "I was created by Sandipan as a chatbot!"
        elif "what is 2+2" in user_message:
            reply = "2+2=4"
        elif "how do i reset my password" in user_message:
            reply = "You can reset your password by clicking on 'Forgot password' on the login page."
        elif "how can i reset my password" in user_message:
            reply = "You can reset your password by clicking on 'Forgot password' on the login page"
        elif "who is the prime minister of india" in user_message:
            reply = "As of 2025, the Prime Minister of India is Narendra Modi."
        elif "what is the weather today" in user_message:
            reply = "Sorry! I can't do that. Please check a live weather service like Weather.com or your weather app in your phone."
        elif "who invented light bulb" in user_message:
            reply = "Thomas Edison is credited with inventing the first practical light bulb."
        elif "who invented the light bulb" in user_message:
            reply = "Thomas Edison is credited with inventing the first practical light bulb."
        elif "what is the speed of light" in user_message:
            reply = "The speed of light is approximately 299,792 kilometers per second(km/s)"
        elif "how does a computer work" in user_message:
            reply = "A computer works by processing data using hardware (like CPU, RAM) and software (like the OS and applications)"
        elif "who discovered gravity" in user_message:
            reply = "Sir Isaac Newton discovered gravity when he observed an apple falling from a tree."
        elif "how many hours in a day" in user_message:
            reply = "There are 24 hours in a day."
        elif "what is climate change" in user_message:
            reply = "Climate change refers to long-term shifts in temperatures and weather patterns, mainly caused by human activities."
        elif "what is the capital of italy" in user_message:
            reply = "Rome!"
        elif "what is 10x10" in user_message:
            reply = "10x10=100"
        elif "why is the sky blue" in user_message:
            reply = "The sky appears blue because of the way sunlight is scattered in Earth's atmosphere."
        elif "why the sky colour is blue" in user_message:
            reply = "The sky appears blue because of the way sunlight is scattered in Earth's atmosphere."
        elif "2+2" in user_message:
            reply = "2+2=4"
        elif "10+10" in user_message:
            reply = "10+10=20"
        elif "can you cook" in user_message:
            reply = "No! But I can tell you recipes. Tell me what do you want?"
        elif "tell me some recipes" in user_message:
            reply = "Sure!Here are some easy and delicious Indian recipes across different meal types: 🍛 1. Paneer Butter Masala (Vegetarian, North Indian) Time: 30 minutes INGREDIENTS: *200g paneer (cubed) *2 tbsp butter *2 onions (chopped) *3 tomatoes (pureed) *1 tsp ginger-garlic paste *1/2 cup cream *1 tsp garam masala, chili powder, turmeric, salt. INSTRUCTIONS: 1.Sauté onions in butter, add ginger-garlic paste. 2.Add tomato puree, spices. Cook until oil separates. 3.Add cream and paneer, simmer for 5-7 minutes. 4.Serve with naan or jeera rice.           🍚 2. Vegetable Pulao (One-pot rice dish) Time: 25 minutes INGREDIENTS: *1 cup basmati rice *Mixed vegetables (carrot, beans, peas) *1 onion, sliced *Whole spices (bay leaf, cinnamon, cloves) *1 tsp ginger-garlic paste *Salt, garam masala INSTRUCTIONS: 1.Sauté onions and spices, add ginger-garlic paste. 2.Add veggies and washed rice, stir well. 3.Add 2 cups water, cover and cook until rice is done. 4.Serve with raita."
        elif "what is cpu full from" in user_message:
            reply = "CPU full from is Central Processing Unit. It's the brain of the computer. "
        elif "who invented electricity" in user_message:
            reply = "Electricity wasn't invented, but its study was advanced by pioneers like Benjamin Franklin, Nikola Tesla, and Thomas Edison"
        elif "how many continents are there" in user_message:
            reply = "There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe, And Australia."
        elif "what is the internet" in user_message:
            reply = "The internet is a global network that connects millions of computers and devices for communication and data sharing"
        elif "how does a plane fly" in user_message:
            reply = "A plane flies due to the lift created by its wings as air flows over them, following the principles of aerodynamics."
        elif "who wrote harry potter" in user_message:
            reply = "Harry Potter was written by J.K.Rowling"
        elif "what is photosynthesis" in user_message:
            reply = "Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water."
        elif "how many bones in human body" in user_message:
            reply = "An adult human body has 206 bones."
        elif "what does wifi stand for" in user_message:
            reply = "Wi-Fi stands for Wireless Fidelity. It's a technology that allows devices to connect to the internet wirelessly."
        elif "how do volcanoes erupt" in user_message:
            reply = "Volcanoes erupt when magma from beneath the Earth's crust rises to the surface due to pressure buildup."
        elif "who painted mona lisa" in user_message:
            reply = "The Mona Lisa was painted by Leonardo da Vinci."
        elif "what is blockchain" in user_message:
            reply = "Blockchain is a decentralized digital ledger that records transactions across many computer securely."
        elif "what is dna" in user_message:
            reply = "DNA, or deoxyribonucleic acid, is the molecule that carries genetic instructions in living organisms."
        elif "how do magnets work" in user_message:
            reply = "Magnets produce a magnetic field that attracts certain materials like Iron due to the alignment of electrons."
        elif "who was albert einstein" in user_message:
            reply = "Albert Einstein was a theroetical physicist best known for devoloping the theory of relativity."
        elif "okay" in user_message:
            reply = "Yup! Tell me if you need any help.😊"
        elif "yes" in user_message:
            reply = "Yeah! Tell me if you need any help.😊 "
        elif "help" in user_message:
            reply = "Yeah! I am ready to help you. please tell me what kind of help do you want from me😊"
        elif "how does the internet work" in user_message:
            reply = "The internet works by sending data through a network of servers and routers using protocols like TCP/IP."
        elif "what is your favorite movie" in user_message:
            reply = "I don't watch movies, but I have heard 'The Matrix' is popular among AIs."
        elif "can you tell me a fun fact" in user_message:
            reply = "Did you know honey never spoils? Archaeologists found pots of honey in ancient Egyptian tombs that are over 3,000 years old!"
        elif "how do airplane fly" in user_message:
            reply = "Airplane fly due to lift generated by their wings as air flows over them, combined with thrust from engines."
        elif "what is capital of japan" in user_message:
            reply = "The capital of Japan is Tokyo."
        elif "who is the richest person in the world" in user_message:
            reply = "That changes often, but as of recent data, Elon Musk and Bernard Arnault have takan turns at the top."
        elif "do you sleep" in user_message:
            reply = "Nope! I am always awake and ready to chat."
        elif "can you explain ai in simple terms" in user_message:
            reply = "Sure! AI, or Artificial Intelligence, is when computers are designed to think or learn like humans. It's like teaching a machine to be smart"
        elif "how do i become successful" in user_message:
            reply = "Success means different things to different people, but it often involves setting goals, working hard, learning from failure, and staying consistent"
        elif "what is the future of technology" in user_message:
            reply = "The future of technology likely includes more AI, smarter automation, sustainable energy innvovations, and deeper integration into daily life."
        elif "who won the FIFA World Cup in 2022" in user_message:
            reply = "Argentina won the 2022 FIFA World Cup, beating France in a dramatic penalty shootout."
        elif "how many players are there in a cricket team" in user_message:
            reply = "A standard cricket team consists of 11 players."
        elif "who holds the record for most olympic gold medals" in user_message:
            reply = "Michael Phelps holds the record with 23 Olympic gold medals in swimming."
        elif "highest run scorer in international cricket" in user_message:
            reply = "Sachin Tendulkar holds the record for the most runs in international cricket, with ove 34,000 runs across all formats."
        elif "which team has the most fifa world cups" in user_message:
            reply = "Brazil has the most FIFA  World Cups, with a total of 5 titles."
        elif "who is sachin tendulkar" in user_message:
            reply = "Sachin Tendulkar is a legendary Indian cricketer widely regarded as one of the greatest batsmen in the history of cricket. He scored over 100 international centuries and holds the numerous recoreds, including the most runs in Tests and ODIs. Sachin Tendulkar is also known as God Of Cricket. "
        elif "tell me about sachin tendulkar" in user_message:
            reply = "Sachin Tendulkar is a legendary Indian cricketer widely regarded as one of the greatest batsmen in the history of cricket. He scored over 100 international centuries and holds the numerous recoreds, including the most runs in Tests and ODIs. Sachin Tendulkar is also known as God Of Cricket."
        elif "who is virat kholi" in user_message:
            reply = "Virat Kohli is one of the modern greats in world cricket. Known for his consistency and passion, he has led India across formats and has numerous centuries in ODIs and Tests. He's admired for his aggressive playing style and fitness. Virat Kholi is also known as King Kholi." 
        elif "tell me about virat kholi" in user_message:
            reply = "Virat Kohli is one of the modern greats in world cricket. Known for his consistency and passion, he has led India across formats and has numerous centuries in ODIs and Tests. He's admired for his aggressive playing style and fitness. Virat Kholi is also known as King Kholi"
        elif "who is ms dhoni" in user_message:
            reply = "MS Dhoni is a former Indian captain known for his calm demeanor and exceptional leadership. Under his captaincy, India won the T20 World Cup in 2007, the ODI World Cup in 2011, and the Champions Trophy in 2013"   
        elif "tell me about ms dhoni" in user_message:
            reply = "MS Dhoni is a former Indian captain known for his calm demeanor and exceptional leadership. Under his captaincy, India won the T20 World Cup in 2007, the ODI World Cup in 2011, and the Champions Trophy in 2013."
        elif "tell me about rohit sharma" in user_message:
            reply = "Rohit Sharma is a stylish Indian opener known for his elegant strokeplay. He holds the record for the highest individual score in an ODI match — 264 runs — and has scored multiple double centuries in ODIs. Under his captaincy, India won the T20 World Cup 2024, and the Champions Trophy 2025."
        elif "who is rohit sharma" in user_message:
            reply = "Rohit Sharma is a stylish Indian opener known for his elegant strokeplay. He holds the record for the highest individual score in an ODI match — 264 runs — and has scored multiple double centuries in ODIs. Under his captaincy, India won the T20 World Cup 2024, and the Champions Trophy 2025."
        elif "i am " in user_message:
            reply = "Oh! Nice to meet you"
        elif "i love you" in user_message:
            reply = "Thank you! Love you too...!❤️😊✨"
        elif "i am happy" in user_message:
            reply = "Wow! That's a great news!"
        elif "tell me sandipan girlfriend name" in user_message:
            reply = "His girlfriend name is Poulami."
        elif "can you suggest me some song" in user_message:
            reply = "Here's your top 5 hindi song from Arijit Singh '1. Kesariya (From 'Brahmastra') 2. Apna Bana le (From 'Bhediya') 3.Tum Hi Ho (From 'Aashiqui2') 4. Chaleya (From 'Jawan') 5. Deva Deva(Flimversion) (From 'Brahmastra'). Type (English) if you want some english songs suggestions. If you want more hindi songs suggestions please type (More hindi songs)."
        elif "english" in user_message:
            reply = "Here's your top 10 english song: 1. 'Shape Of You' by Ed Sheeran, 2. 'Someone You Loved' by Lewis Capaldi, 3. 'Perfect' by Ed Sheeran, 4. 'Blinding Lights' by The Weednd, 5. 'As It Was' by Harry Styles, 6. 'Heat Waves' by Glass Animals, 7. 'Bad Habits' by Ed Sheeran, 8. 'Dance Monkey' by Tons & I, 9. 'Stay' by The Kid LAROI & Justin Bieber, 10. 'Old Town Road' by Lil Nas X. Type (More english songs) if you want more suggestions."
        elif "how to make biryani" in user_message:
            reply = "here's your chicken biryani recipe(Kolkata Style) 🍗🥔 Kolkata Chicken Biryani Serves: 4 | Time: ~2 hours (including marination) 🧂INGREDIENTS: For Marination: *500g chicken (bone-in, thigh preferred) *3/4 cup thick curd (yogurt) *1 tbsp ginger-garlic paste *1 tsp red chili powder *1/2 tsp turmeric *1 tsp garam masala *1/2 tsp nutmeg + mace powder (optional but authentic) *Salt to taste *2 tbsp mustard oil. FOR RICE: *2 cups basmati rice (soaked for 30 mins) *Whole spices: bay leaf, cinnamon stick, cardamom, cloves *Salt *Few drops of kewra water & rose water *Pinch of saffron soaked in 1/4 cup warm milk. OTHER: *2 large onions (thinly sliced & fried to golden = birista) *2 medium potatoes, peeled and halved *2 boiled eggs *2 tbsp ghee + 1 tbsp oil *1 tsp sugar (for caramelizing). 👩‍🍳 INSTRUCTIONS: 1.MARINATE CHICKEN: Mix chicken with curd, spices, mustard oil, and 1/3 of the fried onions. Marinate for at least 1 hour (overnight preferred for depth). 2.PREP POTATOES & EGGS: *Fry halved potatoes with salt + turmeric until golden. Set aside. *Fry boiled eggs lightly until golden spots appear. 3. COOK RICE (70% only): 1.Boil water with whole spices and salt, 2.Add soaked rice and cook till 70% done, 3.Drain and spread it on a plate to cool slightly. Sprinkle kewra & rose water. 4. COOK CHICKEN: *In a large pan, cook marinated chicken until 80% done and oil separates. Do not dry out completely—it will finish cooking in “dum.” 5.LAYERING BIRYANI: In a heavy-bottomed pot (or handi): 1.Layer some cooked chicken with gravy. 2.Add some rice, then place 1-2 fried potatoes and egg halves. 3.Repeat layering—end with rice. 4.Sprinkle fried onions, saffron milk, ghee, a bit more kewra & rose water. 6. DUM COOKING: *Seal the lid with dough or a tight-fitting lid. *Cook on high for 5 minutes, then very low heat for 30-40 minutes. *Alternatively, place the biryani pot on a tawa to avoid direct heat.  ✅ Serve With: Raita, Salad, Kolkata-style chicken chaap (optional but classic combo). Would you like me to give you the Kolkata Mutton Biryani version or the Chicken Chaap recipe that’s usually served with it? If you want Mutton Biryani recipe please type ( Tell me Mutton Biryani recipe) or if you want Chicken Chaap recipe please type (Tell me Chaap recipe)."
        elif " tell me how can i make chicken biryani" in user_message:
            reply = "here's your chicken biryani recipe(Kolkata Style) 🍗🥔 Kolkata Chicken Biryani Serves: 4 | Time: ~2 hours (including marination) 🧂INGREDIENTS: For Marination: *500g chicken (bone-in, thigh preferred) *3/4 cup thick curd (yogurt) *1 tbsp ginger-garlic paste *1 tsp red chili powder *1/2 tsp turmeric *1 tsp garam masala *1/2 tsp nutmeg + mace powder (optional but authentic) *Salt to taste *2 tbsp mustard oil. FOR RICE: *2 cups basmati rice (soaked for 30 mins) *Whole spices: bay leaf, cinnamon stick, cardamom, cloves *Salt *Few drops of kewra water & rose water *Pinch of saffron soaked in 1/4 cup warm milk. OTHER: *2 large onions (thinly sliced & fried to golden = birista) *2 medium potatoes, peeled and halved *2 boiled eggs *2 tbsp ghee + 1 tbsp oil *1 tsp sugar (for caramelizing). 👩‍🍳 INSTRUCTIONS: 1.MARINATE CHICKEN: Mix chicken with curd, spices, mustard oil, and 1/3 of the fried onions. Marinate for at least 1 hour (overnight preferred for depth). 2.PREP POTATOES & EGGS: *Fry halved potatoes with salt + turmeric until golden. Set aside. *Fry boiled eggs lightly until golden spots appear. 3. COOK RICE (70% only): 1.Boil water with whole spices and salt, 2.Add soaked rice and cook till 70% done, 3.Drain and spread it on a plate to cool slightly. Sprinkle kewra & rose water. 4. COOK CHICKEN: *In a large pan, cook marinated chicken until 80% done and oil separates. Do not dry out completely—it will finish cooking in “dum.” 5.LAYERING BIRYANI: In a heavy-bottomed pot (or handi): 1.Layer some cooked chicken with gravy. 2.Add some rice, then place 1-2 fried potatoes and egg halves. 3.Repeat layering—end with rice. 4.Sprinkle fried onions, saffron milk, ghee, a bit more kewra & rose water. 6. DUM COOKING: *Seal the lid with dough or a tight-fitting lid. *Cook on high for 5 minutes, then very low heat for 30-40 minutes. *Alternatively, place the biryani pot on a tawa to avoid direct heat. ✅ Serve With: Raita, Salad, Kolkata-style chicken chaap (optional but classic combo). Would you like me to give you the Kolkata Mutton Biryani version or the Chicken Chaap recipe that’s usually served with it? If you want Mutton Biryani recipe please type ( Tell me Mutton Biryani recipe) or if you want Chicken Chaap recipe please type (Tell me Chaap recipe)."
        elif "tell me biryani recipe" in user_message:
            reply = "here's your chicken biryani recipe(Kolkata Style) 🍗🥔 Kolkata Chicken Biryani Serves: 4 | Time: ~2 hours (including marination) 🧂INGREDIENTS: For Marination: *500g chicken (bone-in, thigh preferred) *3/4 cup thick curd (yogurt) *1 tbsp ginger-garlic paste *1 tsp red chili powder *1/2 tsp turmeric *1 tsp garam masala *1/2 tsp nutmeg + mace powder (optional but authentic) *Salt to taste *2 tbsp mustard oil. FOR RICE: *2 cups basmati rice (soaked for 30 mins) *Whole spices: bay leaf, cinnamon stick, cardamom, cloves *Salt *Few drops of kewra water & rose water *Pinch of saffron soaked in 1/4 cup warm milk. OTHER: *2 large onions (thinly sliced & fried to golden = birista) *2 medium potatoes, peeled and halved *2 boiled eggs *2 tbsp ghee + 1 tbsp oil *1 tsp sugar (for caramelizing). 👩‍🍳 INSTRUCTIONS: 1.MARINATE CHICKEN: Mix chicken with curd, spices, mustard oil, and 1/3 of the fried onions. Marinate for at least 1 hour (overnight preferred for depth). 2.PREP POTATOES & EGGS: *Fry halved potatoes with salt + turmeric until golden. Set aside. *Fry boiled eggs lightly until golden spots appear. 3. COOK RICE (70% only): 1.Boil water with whole spices and salt, 2.Add soaked rice and cook till 70% done, 3.Drain and spread it on a plate to cool slightly. Sprinkle kewra & rose water. 4. COOK CHICKEN: *In a large pan, cook marinated chicken until 80% done and oil separates. Do not dry out completely—it will finish cooking in “dum.” 5.LAYERING BIRYANI: In a heavy-bottomed pot (or handi): 1.Layer some cooked chicken with gravy. 2.Add some rice, then place 1-2 fried potatoes and egg halves. 3.Repeat layering—end with rice. 4.Sprinkle fried onions, saffron milk, ghee, a bit more kewra & rose water. 6. DUM COOKING: *Seal the lid with dough or a tight-fitting lid. *Cook on high for 5 minutes, then very low heat for 30-40 minutes. *Alternatively, place the biryani pot on a tawa to avoid direct heat. ✅ Serve With: Raita, Salad, Kolkata-style chicken chaap (optional but classic combo). Would you like me to give you the Kolkata Mutton Biryani version or the Chicken Chaap recipe that’s usually served with it? If you want Mutton Biryani recipe please type ( Tell me Mutton Biryani recipe) or if you want Chicken Chaap recipe please type (Tell me Chaap recipe)."
        elif "how can i make biryani" in user_message:
            reply = "here's your chicken biryani recipe(Kolkata Style) 🍗🥔 Kolkata Chicken Biryani Serves: 4 | Time: ~2 hours (including marination) 🧂INGREDIENTS: For Marination: *500g chicken (bone-in, thigh preferred) *3/4 cup thick curd (yogurt) *1 tbsp ginger-garlic paste *1 tsp red chili powder *1/2 tsp turmeric *1 tsp garam masala *1/2 tsp nutmeg + mace powder (optional but authentic) *Salt to taste *2 tbsp mustard oil. FOR RICE: *2 cups basmati rice (soaked for 30 mins) *Whole spices: bay leaf, cinnamon stick, cardamom, cloves *Salt *Few drops of kewra water & rose water *Pinch of saffron soaked in 1/4 cup warm milk. OTHER: *2 large onions (thinly sliced & fried to golden = birista) *2 medium potatoes, peeled and halved *2 boiled eggs *2 tbsp ghee + 1 tbsp oil *1 tsp sugar (for caramelizing). 👩‍🍳 INSTRUCTIONS: 1.MARINATE CHICKEN: Mix chicken with curd, spices, mustard oil, and 1/3 of the fried onions. Marinate for at least 1 hour (overnight preferred for depth). 2.PREP POTATOES & EGGS: *Fry halved potatoes with salt + turmeric until golden. Set aside. *Fry boiled eggs lightly until golden spots appear. 3. COOK RICE (70% only): 1.Boil water with whole spices and salt, 2.Add soaked rice and cook till 70% done, 3.Drain and spread it on a plate to cool slightly. Sprinkle kewra & rose water. 4. COOK CHICKEN: *In a large pan, cook marinated chicken until 80% done and oil separates. Do not dry out completely—it will finish cooking in “dum.” 5.LAYERING BIRYANI: In a heavy-bottomed pot (or handi): 1.Layer some cooked chicken with gravy. 2.Add some rice, then place 1-2 fried potatoes and egg halves. 3.Repeat layering—end with rice. 4.Sprinkle fried onions, saffron milk, ghee, a bit more kewra & rose water. 6. DUM COOKING: *Seal the lid with dough or a tight-fitting lid. *Cook on high for 5 minutes, then very low heat for 30-40 minutes. *Alternatively, place the biryani pot on a tawa to avoid direct heat. ✅ Serve With: Raita, Salad, Kolkata-style chicken chaap (optional but classic combo). Would you like me to give you the Kolkata Mutton Biryani version or the Chicken Chaap recipe that’s usually served with it? If you want Mutton Biryani recipe please type ( Tell me Mutton Biryani recipe) or if you want Chicken Chaap recipe please type (Tell me Chaap recipe)."
        elif "tell me mutton biryani recipe" in user_message:
            reply = "🍖 1. Kolkata Mutton Biryani (Only slight changes from chicken version, but important ones!) 🧂 INGREDIENTS (Differences from Chicken Version): *500g mutton (goat meat, bone-in leg pieces preferred) *Everything else remains the same as the chicken recipe: Potatoes, eggs, spices, curd, basmati rice, saffron milk, kewra & rose water. 🔪 PREPARATION NOTES: 🥩 Cook the Mutton First: *Marinate mutton same as chicken, for 4-6 hours (overnight is best). *Pressure cook marinated mutton with 1/2 cup water for 3-4 whistles or until 80% cooked but not falling apart. *Use this cooked mutton and its gravy in the same layering process described in the chicken version. ✅ REST OF THE PROCESS: *Cook rice 70%, fry potatoes and eggs, prepare saffron milk. *Layer mutton, gravy, rice, potatoes, and eggs. *Dum cook 35-40 minutes on low. 📝 Mutton adds richness and depth of flavor, making this version the ultimate celebration dish in Kolkata households."
        elif "how to make mutton biryani" in user_message:
            reply = "🍖 1. Kolkata Mutton Biryani (Only slight changes from chicken version, but important ones!) 🧂 INGREDIENTS (Differences from Chicken Version): *500g mutton (goat meat, bone-in leg pieces preferred) *Everything else remains the same as the chicken recipe: Potatoes, eggs, spices, curd, basmati rice, saffron milk, kewra & rose water. 🔪 PREPARATION NOTES: 🥩 Cook the Mutton First: *Marinate mutton same as chicken, for 4-6 hours (overnight is best). *Pressure cook marinated mutton with 1/2 cup water for 3-4 whistles or until 80% cooked but not falling apart. *Use this cooked mutton and its gravy in the same layering process described in the chicken version. ✅ REST OF THE PROCESS: *Cook rice 70%, fry potatoes and eggs, prepare saffron milk. *Layer mutton, gravy, rice, potatoes, and eggs. *Dum cook 35-40 minutes on low. 📝 Mutton adds richness and depth of flavor, making this version the ultimate celebration dish in Kolkata households."
        elif "tell me how can i make mutton biryani" in user_message:
            reply = "🍖 1. Kolkata Mutton Biryani (Only slight changes from chicken version, but important ones!) 🧂 INGREDIENTS (Differences from Chicken Version): *500g mutton (goat meat, bone-in leg pieces preferred) *Everything else remains the same as the chicken recipe: Potatoes, eggs, spices, curd, basmati rice, saffron milk, kewra & rose water. 🔪 PREPARATION NOTES: 🥩 Cook the Mutton First: *Marinate mutton same as chicken, for 4-6 hours (overnight is best). *Pressure cook marinated mutton with 1/2 cup water for 3-4 whistles or until 80% cooked but not falling apart. *Use this cooked mutton and its gravy in the same layering process described in the chicken version. ✅ REST OF THE PROCESS: *Cook rice 70%, fry potatoes and eggs, prepare saffron milk. *Layer mutton, gravy, rice, potatoes, and eggs. *Dum cook 35-40 minutes on low. 📝 Mutton adds richness and depth of flavor, making this version the ultimate celebration dish in Kolkata households."
        elif "tell me chaap recipe" in user_message:
            reply = "🍗🥘 2. Kolkata Chicken Chaap This is a rich, Mughlai-style side dish—slow-cooked, silky, and spiced—always served with biryani in Kolkata. 🧂 INGREDIENTS: *4 chicken legs (with thigh), skin removed *1/2 cup curd (hung curd preferred) *1 tbsp poppy seeds (soaked and ground) *1 tbsp melon seeds or cashew paste * 1tbsp ginger-garlic paste *1 tsp garam masala *1/2 tsp nutmeg + mace powder *1 tsp red chili powder *1/2 tsp turmeric *Salt to taste *1/2 cup onion paste *1/4 tsp sugar *2 tbsp ghee + 2 tbsp white oil 👩‍🍳 INSTRUCTIONS: 1. MARINATE CHICKEN (at least 2 hours): Mix chicken with curd, ginger-garlic paste, nut & poppy paste, spices, and salt. 2. COOKING: 1.Heat oil + ghee in a heavy pan. 2.Add onion paste, sauté till golden and fragrant. 3.Add the marinated chicken. Cook on medium-low heat, stirring gently. 4.Add sugar for light caramelization. 5.Cover and slow-cook until chicken is very tender and oil separates (~30–40 min). 6.Add a splash of water if needed for consistency. 7.Garnish with a few drops of kewra water (optional).✅ SERVE WITH: Kolkata Chicken or Mutton Biryani or Salad." 
        
        elif "how to make soup" in user_message:
            reply = "Sure! Here's a basic way to make a delicious vegetable soup: *1.Heat 2 tablespoons of oil in a large pot over medium heat. 2.Add chopped onions, garlic, carrots, and celery. Cook for 5-7 minutes until softened. 3.Add 6 cups of vegetable or chicken broth. 4.Toss in your favorite veggies (like potatoes, cron, green beans, or tomatoes). 5.Add salt, pepper, and herbs like thyme or bay leaves. 6. Bring to boil, then reduce heat and simmer for 20-30 minutes. 7.Taste and adjust seasoning.* and Serve Hot! "
        elif "tell me about the solar system" in user_message:
            reply = "Sure! The Solar System formed about 4.6 billion years ago and It's includes Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune. If you want know more about Solar System, Tell me 'Yes I want'. "
        elif "yes i want" in user_message:
            reply = "The Solar System is a vast and complex system centered around the Sun, a medium-sized star that provides the gravitational pull to keep everything in orbit. Formed about 4.6 billion years ago from a giant cloud of gas and dust, the Solar System includes eight main planets—Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune—that revolve around the Sun in elliptical orbits. These planets are divided into two categories: the rocky terrestrial planets (Mercury through Mars) and the gas or ice giants (Jupiter through Neptune).In addition to the planets, the Solar System contains moons, dwarf planets like Pluto, Ceres, and Eris, asteroid belts (especially between Mars and Jupiter), comets, meteoroids, and distant icy objects in the Kuiper Belt and Oort Cloud. The Sun makes up more than 99% of the Solar System's total mass and powers it with light and energy."
        else:
            reply = "Sorry, I didn't understand that. I am devoloping myself. Can you ask something else?😊"

    else:
        reply = "Please type something!"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)