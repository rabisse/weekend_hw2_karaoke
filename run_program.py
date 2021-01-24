from classes.guest import Guest
from classes.room import Room
from classes.song import Song

room = Room("Night at the Roxbury Room", 2, 20)

song_1 = Song("What Is Love", "Haddaway")
song_2 = Song("Stayin Alive", "The Bee Gees")
available_songs = [song_1, song_2]

guest_1 = Guest("Steve Butabi", 100, "What Is Love")
guest_2 = Guest("Doug Butabi", 80, "Stayin Alive")
guest_3 = Guest("Malcolm Holwill", 10, "What Is Love")
guest_4 = Guest("Katie Jeffree",50, "Stayin Alive")
guest_list = [guest_1, guest_2, guest_3, guest_4]


def print_menu():
    print("\nCodeClan Caraoke - Night at the Roxbury Room:")
    print("1: Room Status")
    print("2: Add Guest")
    print("3: Add Song to Queue")
    # print("4: Mark Task as Complete")
    # print("5: Get Tasks Which Take Longer Than a Given Time")
    # print("6: Find Task by Description")
    # print("7: Add a new Task to list")
    print("(Q)uit\n")

while (True):
    print_menu()
    option = input("Select one of the above options or (Q)uit: ")
    if (option.lower() == 'q'):
        break

    if option == '1':
        print(f"\n{room.name}: \nCapacity: {room.capacity} \nOccupants: {room.num_of_occupants()} {[guest.name for guest in room.occupants]} \nSong Queue: {room.give_song_queue()} \nBill: {room.bill} ")

    elif option == '2':
        print(f"\nGuests: \n1: {guest_list[0].name} \n2: {guest_list[1].name} \n3: {guest_list[2].name} \n4: {guest_list[3].name}")     # what is best way to do this for a long guest list? Using index means that removing a guest from list when added returns an error when trying to list it again
        guest_selection = input("Which of the above guests: \n")
        if (guest_selection == '1'):
            room.add_guest_to_room(guest_1)
#            guest_list.remove(guest_1)
        elif (guest_selection == '2'):
            room.add_guest_to_room(guest_2)
#            guest_list.remove(guest_2)
        elif (guest_selection == '3'):
            room.add_guest_to_room(guest_3)
#            guest_list.remove(guest_3)
        elif (guest_selection == '4'):
            room.add_guest_to_room(guest_4)
#            guest_list.remove(guest_4)
        else:
            print("Invalid Input - choose another option")


    elif option == '3':
        print(f"\nAvailable Songs:")
        counter = 1
        for song in available_songs:    # [print(song.give_song()) for song in available_songs]
            print(f"{counter}: {song.give_song()}")
            counter += 1
        song_selection = input("Add which of the above songs to the queue: \n")
        if (song_selection == '1'):
            room.add_song_to_song_queue(song_1)
        elif (song_selection == '2'):
            room.add_song_to_song_queue(song_2)
        else:
            print("Invalid Input - choose another option")


    # elif option == '4':
    #     description = input("Enter task description to search for: ")
    #     task = get_task_with_description(tasks, description)
    #     if task != "Task Not Found":
    #         mark_task_complete(task)
    # elif option == '5':
    #     time = int(input("Enter task duration: "))
    #     print_list(get_tasks_taking_longer_than(tasks, time))
    # elif option == '6':
    #     description = input("Enter task description to search for: ")
    #     print(get_task_with_description(tasks, description))
    # elif option == '7':
    #     description = input("Enter description: ")
    #     time_taken = int(input("Enter time taken: "))
    #     task = create_task(description, time_taken)
    #     tasks.append(task)
    else:
        print("Invalid Input - choose another option")