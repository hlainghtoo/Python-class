#condition Rendering
# asking people age

# if people age about 18
# drink beer

# under 
# drink cocacolar

age = int (input("Enter your age: "))
if age >=18:
    print("enjoy beer!")
else:
    print("Enjoy cocacolar")

# ကိန်းတစ်ခု အသေထည့်ပေးထားယ်
# ခန့်မှန်းကိန်း တစ်ခုထောင်းပေးထားမယ်
# ခန့်မှန်း ကိန်းက ကိန်းအသေ ထက်ကြီးလျှင်
   # ခန့်မှန်းကုန်က ကြီးနေပါတယ်၊၊
# အဲ့တာမဟုတ်ရင် 


result=5
guess = int(input("Enter unber between 1 to 10: "))
if guess > result:
    print("your guess is bigger. Wrong Guess")
elif guess < result:
    print ("your guess is smaller. wrong Guess")
elif guess == result:
    print("Bingo!")
