from classes.guest import Guest
from classes.room import Room
from classes.song import Song


room = Room("Night at the Roxbury Room", 2, 20)

song_1 = Song("What Is Love", "Haddaway")
song_2 = Song("Stayin Alive", "The Bee Gees")

guest_1 = Guest("Steve Butabi", 100, "What Is Love")
guest_2 = Guest("Doug Butabi", 80, "Stayin Alive")
guest_3 = Guest("Malcolm Holwill", 10, "What Is Love")
guest_4 = Guest("Katie Jeffree",50, "Stayin Alive")


def print_menu():
    print("CodeClan Caraoke - Night at the Roxbury Room:")
    print("1: Room Status")
    # print("2: Get Uncompleted Tasks")
    # print("3: Get Completed Tasks")
    # print("4: Mark Task as Complete")
    # print("5: Get Tasks Which Take Longer Than a Given Time")
    # print("6: Find Task by Description")
    # print("7: Add a new Task to list")
    print("Q or q: Quit")

while (True):
    print_menu()
    option = input("Select one of the above options or (Q)uit: ")
    if (option.lower() == 'q'):
        break

    if option == '1':
        print(f"\n{room.name}: \nCapacity: {room.capacity} \nOccupants: {room.occupants} \nSong Queue: {room.song_queue} \nBill: {room.bill} \n")
        print



    # elif option == '2':
    #     print_list(get_uncompleted_tasks(tasks))
    # elif option == '3':
    #     print_list(get_completed_tasks(tasks))
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