def write_note():
    notes = input("Write your note: ")
    with open("mynotes.txt", "a") as file:
        file.write(notes + "\n")
        print("Note saved successfully.")