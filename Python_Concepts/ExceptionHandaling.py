from Exceptions import ExceptionType as et
try:
    l = [4,5,7]
    print(l[2])
except IndexError: # Executed if Indexerror occured
    print("IndexError ocurred")
except (NameError, KeyError):
    print("Name Error")
except:
    print("Some exceptions has ocurred")
else:
    print("Try executed perfectly")


b= "Rohit"
score = 56
try:
    et.scores[b].append(score)
except:
    et.scores[b] = score
print(et.scores)