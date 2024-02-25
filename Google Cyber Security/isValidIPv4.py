# Function to check for valid IPv4 Address
def isValidIPv4(ipAddress):
    ipAddress = str(ipAddress)
    addressParts = []
    temp = ""

    # Breaking Down IP address to a list
    for numb in ipAddress:
        if numb.isdigit() or numb == ".": # Checking if it contains invlaid characters
            if numb == ".":
                if temp == "": # Returning false if it contains empty string
                    return False
                addressParts.append(int(temp))
                addressParts.append(numb)
                temp = ""
            else:
                temp += numb
        else:
            return False
    addressParts.append(int(temp))

    # Checking for invalid conditions
    for count in range(len(addressParts)):
        if count % 2 != 0:
            if addressParts[count] != ".":
                return False
        else:
            if addressParts[count] < 0 or addressParts[count] > 255:
                return False
    
    return True


ip = "..."
