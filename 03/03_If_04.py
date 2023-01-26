mobile_number = input()

if mobile_number[:2] in ['06', '08', '09'] and len(mobile_number) == 10:
    print("Mobile number")
else:
    print("Not a mobile number")