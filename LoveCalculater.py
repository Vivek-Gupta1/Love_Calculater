name=input("Enter Your Name that you want to check\n".lower())
name1 =input("Enter Your partner Name That You want to check\n".lower())
combine_name = name+name1
t=combine_name.count("t")
r=combine_name.count("r")
u=combine_name.count("u")
e=combine_name.count("e")
true = t+r+u+e

l=combine_name.count("l")
o=combine_name.count("o")
v=combine_name.count("v")
e=combine_name.count("e")

love = l+o+v+e
love_score = int(str(true)+str(love))
print(love_score)
if love_score<10 or love_score>90:
  print(f"Your Score Is {love_score} ,You go together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f" Your Score Is {love_score} ,You Are All Right Together")
else:
    print(f"Your Love Score IS {love_score}!")