import re
class RegularExpression:

    # program for validating Email_address
    def validate_email_id(self, email):
       pattern = r"^[a-z0-9_.]+@[a-z0-9]+\.[a-z]{2,6}"
       if re.match(pattern, email):
            return True
       else:
            return False

    # program for validating Mobile number of bangladesh
    def validate_bangladesh_mobile_number(self, mobile_number):
        pattern = r"^[2]+\-[0-9]{8}$"  # bagladesh mobile number - 2-55067364
        if re.match(pattern, mobile_number):
            return True
        else:
            return False
     # program for validating telephone number of USA
    def validate_usa_telephone_number(self, telephone_number):
        pattern = r"^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$"
          # bagladesh mobile number - 2-55067364
        if re.match(pattern, telephone_number):
            return True
        else:
            return False

    # program for validating password ( Alphanumeric, Small,Caps,spacial charactor )
    def password_validation(self, password):
        pattern = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        if re.match(pattern,password):
            return True
        else:
            return False
if __name__ == "__main__":
    Result = RegularExpression()
    email_id = "suman@guvi.in"
    mobile_number = "2-55067364"
    telephone_number = "(123) 123-1234"
    password = "*256@Hmd"
    print(Result.validate_email_id(email_id))
    print(Result.validate_bangladesh_mobile_number(mobile_number))
    print(Result.validate_usa_telephone_number(telephone_number))
    print(Result.password_validation(password))
