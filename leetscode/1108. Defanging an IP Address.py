class Solution(object):
    def defangIPaddr(self, address):
        remoded_address = []
        for char in address:
            if char != ".":
                remoded_address.append(char)
            else:
                remoded_address.append("[.]") 
        new_string = "".join(remoded_address)
        return new_string 
       
            

