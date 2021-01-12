print("Welcome to my first game!!")
name = input("What is your name? ")
age = int(input("How old are you? "))
print("Nice to meet you", name, "you are ", age, "years old")

health = 10

print("You are starting the game with", 10, "health")
if age >= 18:
    print("You are old enough")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Lets play!!")

        left_or_right = input(
            "First choice... Left or Right(type left/right?) "
        ).lower()
        if left_or_right == "left":
            ans = input(
                "Nice choice, you followed the path and reach a lake, do you swim acorss or go around (type across/around)"
            ).lower

            if ans == "around":
                print(
                    "You have gone around the lake and have come to the forest, do you follow the trail or find another way? (type: trail/anotherway"
                ).lower

            elif ans == "across":
                print(
                    "you have gone across the shallow pond and survived, do you follow the trail in the forest or make your own way? (type: trail/anotherway"
                ).lower

            else:
                print("You chose to do nothing and lost the game")

        else:
            print("You fell down and died sorry!")

    else:
        print("See you later!!")

else:
    print("You are not old enough to play, sorry")
