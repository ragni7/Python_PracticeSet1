def generate_prime():
        for number in range(2,20+1):
            if number > 1:
                for j in range(2,number): 
                    if (number % j) ==0:
                        break;
                else:
                    print(f"Prime numbers between 1 to 20 are:", number)
    
generate_prime()
