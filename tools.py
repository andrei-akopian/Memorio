def selectionInput(prompt,clargs,checkfunction=lambda x: (True, None)):
    """An upgraded input function

    prompt = input(prompt)
    clargs = sys.argv
    checkfunction = function that checks if the input is valid eg. if it can be parsed as int, should return a bool and a value

    Checks if there is a valid input in argv, if not, loops untile the user enters a valid one.


    user_name, _ = (tools.)selectionInput("User Name:",clargs)
    raw_input, full_name = (tools.)selectionInput("Full Name:",clargs,lambda name: (True,name.split(" ")))
    """
    validInput,resultValue= False, None
    if len(clargs)>0:
        user_input=clargs[0]
        del clargs[0]
        validInput,resultValue=checkfunction(user_input)
        print(prompt+user_input)
    else:
        user_input=input("Enter "+prompt)
        validInput,resultValue=checkfunction(user_input)
    while not(validInput):
        user_input=input("Reenter "+prompt)
        validInput,resultValue=checkfunction(user_input)
    return user_input, resultValue