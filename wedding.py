"""TODO: guests list
            1. First name
            2. Last Name
            3. City
            4. Relationship (e.g. cousin, parent, friend, etc)
            5. Got the invitation (y/n)
            6. Confirmed participation (y/n)

TODO: preparation list (name, price, bought)
            1. dress
            2. toxedo
            3. chemise
            4. table flowers
            5. bride buquette
            6. godmother bouquete
            7. wedding candles
            8. wedding rings
            9. photo
            10. dj
            11. rental place
            12. hair dressing
            13. make-up

TODO: reports
            1. what have been paid
            2. what need to be paid
            3. who received the invitation
            4. who need to receive invitation
            5. confirmations
            6. needs to confirm
            7. min wage per guest

"""
import re
lst_guests = ["First Name", "Last Name", "City",
              "Relationship", "Received invitation?", "Confirmed attendance?"]

lst_preparations = ["dress", "toxedo", "chemise", "tbl_flowers",
                    "bride_b", "gmother_b", "wed_candles", "wed_rings",
                    "photo", "dj", "saloon", "hair_dressing", "makeup"]

lst_all_guests = []
dic_guest = {}
lst_all_preps = []
dic_prep = {}

# result = re.match(r"[a-zA-z]+", text)
# grab_data = input("Introduce {}: ".format(x))
def add_guest():
    """A function to add a guest to a dictionary based to input
    received and after it passes validation rules
    TODO: add duplication check on First + Last Name combination"""
    print("Start adding an wedding guest\n")
    gen_match_rule = re.compile('[a-zA-Z\-\s]*$')
    match_rule1 = re.compile('[yesnodauYESNODAU]*$')
    for x in lst_guests:
        grab_data = input("Introduce {}: ".format(x))
        grab_data = gen_match_rule.match(grab_data)
        if grab_data is None:
            raise ValueError("ERROR: Your input is wrong!")

        else:
            grab_data = grab_data.group()
            if x in ("First Name", "Last Name", "City", "Relationship"):
                # print("Column: {} with value: {}".format(x, grab_data))
                dic_guest[x] = grab_data
            if x in ("Received invitation?", "Confirmed attendance?"):
                grab_data = match_rule1.match(grab_data)
                if grab_data is None:
                    raise ValueError("ERROR: Your input is wrong!")

                else:
                    grab_data = grab_data.group()
                    # print("Column: {} with value: {}".format(x, grab_data))
                    dic_guest[x] = grab_data
    print("\nGuest details added as follows:\n"
          "===============================")
    for key in dic_guest:
        print("{}: {}".format(key, dic_guest[key]))


    lst_all_guests.append(dic_guest)


a = 0
while a < 3:
    add_guest()
    a += 1

add_guest()
for q in range(0,len(lst_all_guests)):
    print(lst_all_guests[q])
