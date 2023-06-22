#KAUN BANEGA CROREPATI USING LISTS IN PYTHON

print("*********************WELCOME TO KAUN BANEGA CROREPATI************************\n")

name=input("Your good name:")
print(f"\nThank you{name}\n\nAre you ready!!!!!\n\nToh chaliye shuru krte hai\n\nYour 1st question is on your screen! Here it is:-")

questions=["Which country is famous for the Taj Mahal?","Who wrote the play \"Romeo and Juliet\"?","Which planet is known as the \"Giant of our Solar System\"?","Who invented the telephone?","Which is the largest democracy in the world?","Who painted the famous artwork \"The Starry Night\"?","Which country won the FIFA World Cup in 2018?","Who is the CEO of Tesla and SpaceX?","Who is the author of the Harry Potter book series?","Which is the longest river in the world?","Which is the largest ocean in the world?","Who painted the Mona Lisa?","Who is known as the \"Father of the Nation\" in India?","Which planet is known as the \"Red Planet\"?","Which country hosted the 2020 Summer Olympics?"]


options=[
   ["a)India","b)Egypt","c)China","d)Italy"],

   ["a)Arthur Miller","b)George Bernard Shaw","c)Oscar Wilde","d)William Shakespeare"],
   
   ["a)Mercury","b)Venus","c)Jupiter","d)Uranus"],
   
   ["a) Thomas Edison","b) Alexander Graham Bell","c) Nikola Tesla","d) Isaac Newton"],
   
   ["a) United States","b) China","c) Russia","d) India"],
   
   ["a) Vincent van Gogh","b) Pablo Picasso","c) Leonardo da Vinci","d) Claude Monet"],
   
   ["a) Germany","b) Argentina","c) Brazil","d) France",],
   
   ["a) Tim Cook","b) Jeff Bezos","c) Elon Musk","d) Mark Zuckerberg"],
   
   ["a) J.R.R. Tolkien","b) George R.R. Martin","c) J.K. Rowling","d) Stephen King"],
   
   ["a) Nile River","b) Amazon River","c) Yangtze River","d) Mississippi River"],
   
   ["a) Atlantic Ocean","b) Indian Ocean","c) Pacific Ocean","d) Arctic Ocean"],
   
   ["a) Leonardo da Vinci","b) Pablo Picasso","c) Vincent van Gogh","d) Michelangelo"],
   
   ["a) Mahatma Gandhi","b) Jawaharlal Nehru","c) Subhash Chandra Bose","d) Bhagat Singh"],
   
   ["a) Venus","b) Mars","c) Jupiter","d) Saturn"],
   
   ["a) Japan","b) Brazil","c) China","d) Russia"]]

answers=[1,4,3,2,4,1,4,3,3,1,3,1,1,2,1]
amount=0

money = [1000,2000,3000,5000,11000,20000,40000,80000,160000,320000,1000000,2000000,5000000,7500000,10000000]
for i in range(0,len(questions)):

    print(f"Question for Rs.{money[i]}\n\n",questions[i])
    for items in options[i]:
        print(items)
    reply = int(input("\n\nEnter your answer (1-4) or  0 to quit:" ))
    if (reply == 0):
     amount = money[i-1]
     break
    if(reply == answers[i]):
        print(f"\n\nCorrect answer, you have won Rs. {money[i]}\n\n")
        amount=money[i]
    else:
       print("\n\nOops!! Wrong Answer!\n\nI'm sorry to say ki aapka safar yahi tak tha\n\n")
       break
print(f"Your take away money is Rs.{amount}")
if (amount==10000000):
   print(f"\nCongratulations!! {name} aap bn gye hai CROREPATI")