prompt = "\n hello, how are you?"
prompt += "\n to stop the program write 'quit' "

#message = ""
#while message != 'quit':
#    message = input(prompt)
#    print(message)

#print('the program is stopped')

#active = True

#while active:
#    message = input(prompt)

#    if message == "quit":
#        active = False
#        print("the program is stopped")
#    else:
#        print(message)

unconfirmed_user = ['mina', 'lina', 'tina', 'rina','karim', 'rahim','jodu','modhu']
confirmed_user = []

#for user in unconfirmed_user:
#    confirmed_user.append(user)
#    print(f"Verifying user: {user.title()}")

#while unconfirmed_user:
#    current_user = unconfirmed_user.pop()
#    print(f"the verifying user: {current_user.title()}")
#    confirmed_user.append(current_user)

#print("the following users have been confirmed:")
#for user in confirmed_user:
#    print(user.title())

responses ={}

poll_active = True



while poll_active:
     name = input("\n what is your name?")
     response = input('\n In which mountain you want to climb?')

     responses[name] = response
     print("\ndo you want more response?")
     answer = input("\n yes or no")

     if answer == "no":
        poll_active = False
print("\n____poll_result_____")

print(responses)


for name, response in responses.items():
    print(f"{name.title()} loves to climb {response}.")





