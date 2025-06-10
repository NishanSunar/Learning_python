def goodday(name, end= "thank you"):  # default parameter value
    print(f"Good Day, {name}")
    print(end)
    
goodday("nishan","bye") #this will send "bye to the end parameter
goodday("Rohan")# this wiill not send any value to the end parameter so default parameter value is used