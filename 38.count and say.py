def countAndSay(n: int) -> str:
        current = "1"  # Start with the base case

        for _ in range(1, n):  # Generate up to the nth term
            next_term = ""
            count = 1
            
            # Traverse through the current term
            for i in range(1, len(current)):
                if current[i] == current[i - 1]:
                    count += 1
                else:
                    next_term += str(count) + current[i - 1]
                    count = 1
            
            # Append the last group of digits
            next_term += str(count) + current[-1]
            current = next_term
        
        return current

print(countAndSay(n=4))
