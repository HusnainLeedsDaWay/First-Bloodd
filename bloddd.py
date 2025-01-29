def draw_animal(animal):
    if animal.lower() == 'cat':
        print("      /\\_/\\")
        print("     ( o.o )")
        print("      > ^ <")

    elif animal.lower() == 'fish':
        print("     ><(((('>")
        print("       =====")

    elif animal.lower() == 'butterfly':
        print("     /\\  /\\")
        print("    ( ==  == )")
        print("     \\_)(_/")

    else:
        print("Sorry, I don't know how to draw that animal.")

if __name__ == "__main__":
    animal = input("Which animal do you want to draw (cat, fish, butterfly)? ")
    draw_animal(animal)