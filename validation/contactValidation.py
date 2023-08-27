




def isValidContact(contactNumber):
    contactNumber= contactNumber.replace(" ","").replace("+","").strip()

    if len(contactNumber) != 12:
        return False

    return True
