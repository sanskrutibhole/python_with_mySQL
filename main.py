from db_helper import DBHelper


def main():
    db = DBHelper()  # object
    while True:
        print("*********WELCOME************")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit user")
        print()
        try:
            choice = int(input())
            if (choice == 1):
                # insert user
                userID = int(input("Enter new userID:"))
                userName = input("Enter new userName:")
                userPhoneNo = input("Enter new userPhoneNo:")
                db.insert_user(userID, userName, userPhoneNo)
                pass
            elif choice == 2:
                # display user
                db.fetch_all()
                pass
            elif choice == 3:
                # delete user
                userID = int(input("Enter userID to be deleted"))
                db.delete_user(userID)
                pass
            elif choice == 4:
                # update user
                userID = int(input("Enter userID to be updated:"))
                userName = input("Enter userName to be updated::")
                userPhoneNo = input("Enter userPhoneNo to be updated::")

                db.update_user(userID, userName, userPhoneNo)
                pass
            elif choice == 5:
                break
            else:
                print("Invalid Output! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details! Try again")


if __name__ == "__main__":
    main()
