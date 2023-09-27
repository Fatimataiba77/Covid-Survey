print("WELCOME TO THE COVID-19 AWARENESS SURVEY")
print("PERSONAL DETAILS:-")
name=input("Enter your name: ")
age= int(input("Enter your age: "))
gender=input("Specify your gender: ")

print("Since this is a covid related quiz/survey/awareness program , please answer the following questions. (Answer in caps/numbers as mentioned): ")
print("_________________________________________________________________")

a=input("Q.HAVE YOU TAKEN THE PCR TEST FOR COVID-19 ANYTIME AFTER THE START OF THE PANDEMIC? (YES/NO)\nAns: ")

if a=="YES":
    b=input("Q. WERE YOU TESTED +VE OR -VE? (P/N)\nAns: ")

    if b=="P":
        
        g=input("Q.What symptoms are you having right now?\nAns: ")
        h=input("Q.How long have you been facing these symptoms?\nAns: ")
        i=input("Q.How long has the treatment been going on?\nAns: ")
        j=input("Q.What have you been doing in quarantine to gain motivation?\nAns: ")
        k=input("Q.Can you name some variants of coronavirus?\nAns: ")
        print("Dear Friend, please take care of the following things")
        print("________________________________\n")
        print("We know this is a hard time but it shall pass soon!!!\n")
        print("1)Use a thermometer to keep a track on the body Temperature\n2)Use the oximeter's pulse reading to keep a track on the pulse\n3)Try to sleep on stomach & avoid lying on the bacl\n4)Start steam inhaling & hot water gargling\n5)Practice betadine gargles in case of sore throat\n6)Practice yoga exercises daily!")
        print("Take care!")
    else:
    
        c=input("Q.WERE ANY OF YOUR FAMILY MEMBER TESTED POSITIVE/ HAD COVID? (YES/NO)\nAns: ")
       
        if c=="YES":
            
            g1=input("Q.What symptoms are they having right now?\nAns: ")
            h1=input("Q.How long have they been facing these symptoms?\nAns: ")
            i1=input("Q.How long has the treatment been going on?\nAns: ")
            j1=input("Q.What have you been doing in quarantine to gain motivation?\nAns: ")
            k1=input("Q.Can you name some variants of coronavirus?\nAns: ")
            print("Dear Friend, please take care of the following things")
            print("__________________________________________________________\n")
            print("We know this is a hard time but it shall pass soon!!!\n")
            print("1)Use a thermometer to keep a track on the body Temperature\n2)Use the oximeter's pulse reading to keep a track on the pulse\n3)Try to sleep on stomach & avoid lying on the bacl\n4)Start steam inhaling & hot water gargling\n5)Practice betadine gargles in case of sore throat\n6)Practice yoga exercises daily!")
            print("Take care!")
        else :
            d=input("Q.Are you vaccinated? (YES/NO)\nAns: ")
            
            if d=="YES":
                x=input("Please enter the name of the vaccine taken (Covishield/Covaxin):")
                y=input("Please state the post vaccine symptoms experienced(if multiple answers, seperate using comma(,):")
                z=int(input("Please enter number of recovery days required post the vaccine(in numbers only):"))

    
                str1='''
Thank you for being a responsible citizen of the country and taking your assigned dose of the vaccine early on. However, the pandemic still continues to target mankind and during these tough times all of us must be responsible, atleast at our own levels to curb and prevent the spread of the virus. The following tips have been curated with instructions from doctors and tips from people who recovered after contracting the virus and these will surely help you to keep you and those around you, safe from COVID-19.'''
                print(str1)

                #diet
                str3='''
DIET

It is important to have a nutrition rich diet to support our immunity consisting of:
1. Protiens- Eggs, Chicken and other types of meats, Pulses(Lentils,Beans,etc), Nuts(Almonds,Peanuts,etc.), Cereals(Oats,Wheat,etc.), Paneer/Tofu.

2. Fibre- Raw vegetables and fruits in salads or whole, seasonal fruits(Mango,Watermelon,etc.) & Citrus fruits rich in Vitamin C.  

3. Fats- Unsaturated fats(Fishes,Soy) and cooking oils with unsaturated fats(Olive oil,Sunflower oil)

4. Vitamins- Various vitamins like A(Papaya,Carrots), Bcomplex(Milk,Eggs,Meat,Legumes,etc.), C(Citrus,Amla), D(Basking in sunlight,Salmon,etc.),E(Various nuts and seeds), K(Green leafy vegetables)

5. Other elemental components- Food rich in Iron(Cashews,Lentils,etc.), Zinc(Seeds, Meat,Etc.), Potassium(Bananas,Beetroots,etc.), Calcium(Milk,Yogurt,etc.)

It is advisable to:
1. Avoid outside foods.
2. Avoid salty foods
3. Consume healthy homecooked food.'''
                print(str3)

                #physical and mental wellbeing
                str4='''
PHYSICAL AND MENTAL WELLBEING

1. Sleep- Sleeping for 7-8 hours everyday helps the immune system.
2. Hydrate- Drink atleast 8 glasses of water in a day.
3. Exercise- Along with a good diet, exercising daily does wonders for the immunity.
4. Meditation- Practice Yoga for destressing and building up your immunity.
5. Less Panic,More Action- Even if you contract the virus, remember that more than 80% of the patients recover without any complications.So, do not panic and take the necessary measure accordingly.
6. Rest- Take appropriate amount of rest to unwind and relax after excessive screentime.'''
                print(str4)https://www.onlinegdb.com/online_python_compiler#_editor_5631468511

    
            
            else:
                s1=input("Q.DO YOU GET TIRED EASILY? (YES/NO) \nAns: ") 
                s2=input("Q.DO YOU GET FEVER OR CHILLS? (YES/NO) \nAns: ")
                s3=input("Q.DO YOU HAVE DIFFICULTY IN BREATHING? (YES/NO) \nAns: ")
                s4=input("Q.DO YOU FEEL LOSS OF SENSE OF SMELL OR TASTE? (YES/NO) \nAns: ")
                diet1="When a person is sick, they may find it difficult to develop an appetite.\n However, it is important to receive nourishment and stay hydrated, \n especially when feeling unwell.\n1)Herbal tea \n2)Honey \n3)Citrus fruits & berries. \nAvoid dairy and alcohol."
                diet2="Eat a variety of foods:\nEvery day, eat a combination of different foods including whole grains \nsuch as wheat, maize and rice, \nlegumes like lentils and beans, fruit and vegetables and some foods from animal sources \n(e.g. meat, fish, eggs and milk"
                diet3="Be strategic about the use of ingredients - prioritize fresh products \nPrepare home-cooked meals \nFollow safe food handling practices \nLimit your salt intake \nLimit your sugar intake. \nLimit your fat intake \nConsume enough fibre & stay hydrated."
                if(s1=="YES" and s2=="YES"):
                    if(s3=="YES" and s4=="YES"):
                        print("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                    elif(s3=="NO" and s4=="YES"):
                        print(diet1)
                    elif(s3=="YES" and s4=="NO"):
                        print(diet2)
                    else:
                        print(diet3)
                elif(s1=="NO" and s2=="NO"):
                    if(s3=="YES" and s4=="YES"):
                          print("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                    elif(s3=="NO" and s4=="YES"):
                        print(diet1)
                    elif(s3=="YES" and s4=="NO"):
                        print(diet2)
                    else:
                        print(diet3)
                elif(s1=="YES" and s2=="NO"):
                    if(s3=="YES" and s4=="YES"):
                        print("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                    elif(s3=="NO" and s4=="YES"):
                        print(diet1)
                    elif(s3=="YES" and s4=="NO"):
                        print(diet2)
                    else:
                        print(diet3)
                elif(s1=="NO" and s2=="YES"):
                    if(s3=="YES" and s4=="YES"):
                        print("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                    elif(s3=="NO" and s4=="YES"):
                        print(diet1)
                    elif(s3=="YES" and s4=="NO"):
                        print(diet2)
                    else:
                        print(diet)

else:
    e=input("Q.WERE ANY OF YOUR FAMILY MEMBER TESTED POSITIVE/ HAD COVID? (YES/NO)\nAns: ")
        
    if e=="Y":
        
        g2=input("Q.What symptoms are they having right now?\nAns: ")
        h2=input("Q.How long have they been facing these symptoms?\nAns: ")
        i2=input("Q.How long has the treatment been going on?\nAns: ")
        j2=input("Q.What have you been doing in quarantine to gain motivation?\nAns: ")
        k2=input("Q.Can you name some variants of coronavirus?\nAns: ")
        print("Dear Friend, please take care of the following things")
        print("________________________________________________________________________\n")
        print("We know this is a hard time but it shall pass soon!!!\n")
        print("1)Use a thermometer to keep a track on the body Temperature\n2)Use the oximeter's pulse reading to keep a track on the pulse\n3)Try to sleep on stomach & avoid lying on the bacl\n4)Start steam inhaling & hot water gargling\n5)Practice betadine gargles in case of sore throat\n6)Practice yoga exercises daily!")
        print("Take care!")
    else:
            
        f=input("Q.Are you vaccinated? (YES/NO)\nAns: ")
            
        if f=="YES":
            x1=input("Please enter the name of the vaccine taken (Covishield/Covaxin):")
            y1=input("Please state the post vaccine symptoms experienced(if multiple answers, seperate using comma(,):")
            z1=int(input("Please enter number of recovery days required post the vaccine(in numbers only):"))

    
            str5='''
Thank you for being a responsible citizen of the country and taking your assigned dose of the vaccine early on. However, the pandemic still continues to target mankind and during these tough times all of us must be responsible, atleast at our own levels to curb and prevent the spread of the virus. The following tips have been curated with instructions from doctors and tips from people who recovered after contracting the virus and these will surely help you to keep you and those around you, safe from COVID-19.'''
            print(str5)

            #diet
            str6='''
DIET

It is important to have a nutrition rich diet to support our immunity consisting of:
1. Protiens- Eggs, Chicken and other types of meats, Pulses(Lentils,Beans,etc), Nuts(Almonds,Peanuts,etc.), Cereals(Oats,Wheat,etc.), Paneer/Tofu.

2. Fibre- Raw vegetables and fruits in salads or whole, seasonal fruits(Mango,Watermelon,etc.) & Citrus fruits rich in Vitamin C.  

3. Fats- Unsaturated fats(Fishes,Soy) and cooking oils with unsaturated fats(Olive oil,Sunflower oil)

4. Vitamins- Various vitamins like A(Papaya,Carrots), Bcomplex(Milk,Eggs,Meat,Legumes,etc.), C(Citrus,Amla), D(Basking in sunlight,Salmon,etc.),E(Various nuts and seeds), K(Green leafy vegetables)

5. Other elemental components- Food rich in Iron(Cashews,Lentils,etc.), Zinc(Seeds, Meat,Etc.), Potassium(Bananas,Beetroots,etc.), Calcium(Milk,Yogurt,etc.)

It is advisable to:
1. Avoid outside foods.
2. Avoid salty foods
3. Consume healthy homecooked food.'''
            print(str6)

            #physical and mental wellbeing
            str7='''
PHYSICAL AND MENTAL WELLBEING

1. Sleep- Sleeping for 7-8 hours everyday helps the immune system.
2. Hydrate- Drink atleast 8 glasses of water in a day.
3. Exercise- Along with a good diet, exercising daily does wonders for the immunity.
4. Meditation- Practice Yoga for destressing and building up your immunity.
5. Less Panic,More Action- Even if you contract the virus, remember that more than 80% of the patients recover without any complications.So, do not panic and take the necessary measure accordingly.
6. Rest- Take appropriate amount of rest to unwind and relax after excessive screentime.'''
            print(str7)

        else:
            sy1=input("Q.DO YOU GET TIRED EASILY? (YES/NO) \nAns: ") 
            sy2=input("Q.DO YOU GET FEVER OR CHILLS? (YES/NO) \nAns: ")
            sy3=input("Q.DO YOU HAVE DIFFICULTY IN BREATHING? (YES/NO) \nAns: ")
            sy4=input("Q.DO YOU FEEL LOSS OF SENSE OF SMELL OR TASTE? (YES/NO) \nAns: ")
            d1="When a person is sick, they may find it difficult to develop an appetite.\n However, it is important to receive nourishment and stay hydrated, \n especially when feeling unwell.\n1)Herbal tea \n2)Honey \n3)Citrus fruits & berries. \nAvoid dairy and alcohol."
            d2="Eat a variety of foods:\nEvery day, eat a combination of different foods including whole grains \nsuch as wheat, maize and rice, \nlegumes like lentils and beans, fruit and vegetables and some foods from animal sources \n(e.g. meat, fish, eggs and milk"
            d3="Be strategic about the use of ingredients - prioritize fresh products \nPrepare home-cooked meals \nFollow safe food handling practices \nLimit your salt intake \nLimit your sugar intake. \nLimit your fat intake \nConsume enough fibre & stay hydrated."
            if(sy1=="YES" and sy2=="YES"):
                if(sy3=="YES" and sy4=="YES"):
                    print("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                elif(sy3=="NO" and sy4=="YES"):
                    print(d1)
                elif(sy3=="YES" and sy4=="NO"):
                    print(d2)
                else:
                    print(d3)
            elif(sy1=="NO" and sy2=="NO"):
                if(sy3=="YES" and sy4=="YES"):
                      print ("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                elif(sy3=="NO" and sy4=="YES"):
                    print(d1)
                elif(sy3=="YES" and sy4=="NO"):
                    print(d2)
                else:
                    print(d3)
            elif(sy1=="YES" and sy2=="NO"):
                if(sy3=="YES" and sy4=="YES"):
                    print("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                elif(sy3=="NO" and sy4=="YES"):
                    print(d1)
                elif(sy3=="YES" and sy4=="NO"):
                    print(d2)
                else:
                    print(d3)
            elif(sy1=="NO" and sy2=="YES"):
                if(sy3=="YES" and sy4=="YES"):
                    print ("PLEASE VISIT A DOCTOR AND GET TESTED IMMEDIATELY. TAKE CARE AND STAY SAFE ☺")
                elif(sy3=="NO" and sy4=="YES"):
                    print(d1)
                elif(sy3=="YES" and sy4=="NO"):
                    print(d2)
                else:
                    print(d3)
print("_________________________________________________________________________________")
print("Prevention methods: ")
print("To prevent the spread of COVID-19:\nClean your hands often. \nUse soap and water, or an alcohol-based hand rub.\nMaintain a safe distance from anyone who is coughing or sneezing.\nWear a mask when physical distancing is not possible.\nDon’t touch your eyes, nose or mouth.\nCover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\nStay home if you feel unwell.\nIf you have a fever, cough and difficulty breathing, seek medical attention.\nCalling in advance allows your healthcare provider to quickly direct you to the right health facility. \nThis protects you, and prevents the spread of viruses and other infections.\nMasks can help prevent the spread of the virus from the person wearing the mask to others. \nMasks alone do not protect against COVID-19, and should be combined with physical distancing and hand hygiene. \nFollow the advice provided by your local health authority.")
print("Alongside the safety measures, to help follow Covid-19 social distancing guidelines, \nhere is a little contribution towards maintaining safety distance.\nThe Covid Safety Sensor")
print(" ☺ THANKYOU FOR YOUR VALUABLE TIME ☺ ")
p=input("(Press any key to continue)")
import webbrowser
webbrowser.open("https://www.tinkercad.com/embed/fkZHKmhkMFE?editbtn=1")


    
                
