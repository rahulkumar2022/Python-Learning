# Syntax

# Match expression
# case x:
#     code Block
# case y:
#     code Block
# case _:
#     code Block

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:  # Match both Saturday and Sunday
        print("Weekend")
    case _:
        print("Invalid day")  # Default case if no match found