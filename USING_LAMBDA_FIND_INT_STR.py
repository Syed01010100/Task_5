#Task: Write a Python code using the Lambda function to check every element of a list is an integer or string

user_list =[250,'syed','ali','python',300,3.5]

result= lambda x: f"{x} is an integer" if type(x) is int\
    else f"{x} is a string" if type(x) is str\
    else f"{x} is not a defined data type"

for x in user_list:

    print(result(x))
