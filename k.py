passes = []

def create_pass():
    pass_id = input("Enter Pass ID: ")
    name = input("Enter Passenger Name: ")
    route = input("Enter Route: ")
    validity = input("Enter Validity (e.g., 30 days): ")

    passes.append({
        "id": pass_id,
        "name": name,
        "route": route,
        "validity": validity
    })

    print("✅ Bus Pass Created Successfully!\n")


def view_passes():
    if not passes:
        print("No bus passes found.\n")
        return

    print("\n=== Bus Pass Records ===")
    for p in passes:
        print(
            f"ID: {p['id']} | "
            f"Name: {p['name']} | "
            f"Route: {p['route']} | "
            f"Validity: {p['validity']}"
        )
    print()


def search_pass():
    pass_id = input("Enter Pass ID: ")

    for p in passes:
        if p["id"] == pass_id:
            print("\nPass Found:")
            print(p)
            return

    print("❌ Pass not found.\n")


def renew_pass():
    pass_id = input("Enter Pass ID to renew: ")

    for p in passes:
        if p["id"] == pass_id:
            p["validity"] = input("Enter New Validity: ")
            print("✅ Pass Renewed Successfully!\n")
            return

    print("❌ Pass not found.\n")


def delete_pass():
    pass_id = input("Enter Pass ID to delete: ")

    for p in passes:
        if p["id"] == pass_id:
            passes.remove(p)
            print("✅ Pass Deleted Successfully!\n")
            return

    print("❌ Pass not found.\n")


def main():
    while True:
        print("===== Bus Pass Manager =====")
        print("1. Create Pass")
        print("2. View Passes")
        print("3. Search Pass")
        print("4. Renew Pass")
        print("5. Delete Pass")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_pass()
        elif choice == "2":
            view_passes()
        elif choice == "3":
            search_pass()
        elif choice == "4":
            renew_pass()
        elif choice == "5":
            delete_pass()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.\n")

main()