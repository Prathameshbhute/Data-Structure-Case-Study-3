# Parking Management System
# Using Linked List, Queue and Stack

class Node:
    def __init__(self, vehicle_no, owner, slot):
        self.vehicle_no = vehicle_no
        self.owner = owner
        self.slot = slot
        self.next = None


class Parking:

    def __init__(self, capacity):
        self.capacity = capacity

        # Linked List
        self.head = None

        # Queue
        self.queue = []

        # Stack
        self.stack = []

        self.next_slot = 1


    def park(self, vehicle_no, owner):

        if self.next_slot <= self.capacity:

            new_node = Node(
                vehicle_no,
                owner,
                self.next_slot
            )

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next:
                    temp = temp.next

                temp.next = new_node

            print("Vehicle parked in Slot", self.next_slot)
            self.next_slot += 1

        else:
            self.queue.append((vehicle_no, owner))
            print("Parking full. Vehicle added to waiting queue.")


    def remove(self, search_value):

        temp = self.head
        previous = None

        while temp:

            if (temp.vehicle_no == search_value or
                    temp.owner.lower() == search_value.lower()):

                if previous is None:
                    self.head = temp.next
                else:
                    previous.next = temp.next

                self.stack.append(
                    (temp.vehicle_no, temp.owner, temp.slot)
                )

                print("\nVehicle removed successfully.")
                print("Vehicle:", temp.vehicle_no)
                print("Owner:", temp.owner)
                print("Slot:", temp.slot)

                if self.queue:

                    vehicle = self.queue.pop(0)

                    self.park(
                        vehicle[0],
                        vehicle[1]
                    )

                return

            previous = temp
            temp = temp.next

        print("\nVehicle or Owner not found.")


    def display(self):

        temp = self.head

        print("\nParked Vehicles:")

        if temp is None:
            print("No vehicles parked.")
            return

        while temp:

            print(
                "Vehicle:", temp.vehicle_no,
                "| Owner:", temp.owner,
                "| Slot:", temp.slot
            )

            temp = temp.next


    def last_removed(self):

        if self.stack:

            vehicle = self.stack[-1]

            print("\nLast Removed Vehicle:")
            print("Vehicle:", vehicle[0])
            print("Owner:", vehicle[1])
            print("Slot:", vehicle[2])

        else:
            print("No vehicle removed yet.")


# Main Program

parking = Parking(3)

while True:

    print("\n===== PARKING MANAGEMENT =====")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Display Parked Vehicles")
    print("4. Last Removed Vehicle")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        vehicle_no = input("Enter vehicle number: ")
        owner = input("Enter owner name: ")

        parking.park(vehicle_no, owner)

    elif choice == "2":

        search_value = input(
            "Enter Vehicle Number or Owner Name: "
        )

        parking.remove(search_value)

    elif choice == "3":

        parking.display()

    elif choice == "4":

        parking.last_removed()

    elif choice == "5":

        print("Thank you!")
        break

    else:
        print("Invalid choice.")