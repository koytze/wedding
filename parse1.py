import argparse
import re

lst_guests = ["First Name", "Last Name", "City",
              "Relationship", "Received invitation?", "Confirmed attendance?"]

guest_args = []

for element in lst_guests:
    element = re.sub("\s", "_", element.lower())
    element = re.sub("\?", "", element)
    # element = re.sub(r"^", "--", element)
    guest_args.append(element)

# print(guest_args)
answers = []

def parse_arguments():
    """Initialize parameters"""
    parser = argparse.ArgumentParser()


    parser.add_argument('--first_name',
                        # choices=["BiosSetup", "Cd", "Diags", "Floppy", "Hdd", "None", "Pxe", "Usb"],
                        action='store',
                        help="Specify guest First Name",
                        required = True)
    parser.add_argument('--second_name',
                        # choices=["BiosSetup", "Cd", "Diags", "Floppy", "Hdd", "None", "Pxe", "Usb"],
                        action='store',
                        help="Specify guest Second Name",
                        required=True)
    parser.add_argument('--city',
                        # choices=["BiosSetup", "Cd", "Diags", "Floppy", "Hdd", "None", "Pxe", "Usb"],
                        action='store',
                        help="Specify the city where guest is living (default is Bucharest)",
                        required=True)
    parser.add_argument('--relationship',
                        # choices=["BiosSetup", "Cd", "Diags", "Floppy", "Hdd", "None", "Pxe", "Usb"],
                        action='store',
                        help="Specify relation with the guest (e.g Cousin, Brother, Parent)",
                        required=True)
    parser.add_argument('--received_invitation',
                        choices=["y", "Y", "n", "N"],
                        action='store',
                        help="Specify if guest had received the invitation (default is N)",
                        required=True,
                        default="N")
    parser.add_argument('--confirmed_attendance',
                        choices=["y", "Y", "n", "N"],
                        action='store',
                        help="Specify if guest confirmed hes participation (default is N)",
                        required=True,
                        default="N")

    return parser.parse_args()



# subprocess.run("python3 CSU_boot.py --ccmHost " + ccmHost + " --csuList " + serial + " -u " + ccmapi_user + " -p " + ccmapi_pass +" -b Pxe -i " + image, shell=True, check=True)

def main():
    args = parse_arguments()
    print(args)

    if args.first_name:
        answers.append(args.first_name)
    if args.second_name:
        answers.append(args.second_name)
    if args.city:
        answers.append(args.city)
    if args.relationship:
        answers.append(args.relationship)
    if args.received_invitation:
        answers.append(args.received_invitation)
    if args.confirmed_attendance:
        answers.append(args.confirmed_attendance)


    print(answers)


if __name__ == '__main__':
        main()
