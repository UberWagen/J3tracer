from inputs import get_gamepad
while 1:
    events = get_gamepad()
    for event in events:
        print(event.code(1),event.state(1))
       
        
        
