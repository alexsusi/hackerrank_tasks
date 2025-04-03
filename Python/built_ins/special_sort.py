if __name__ == "__main__":
    chaos = str(input())  
    
    # letters
    lower_chaos = [char for char in chaos if char.islower()]
    lower_chaos.sort()
    upper_chaos = [char for char in chaos if char.isupper()]
    upper_chaos.sort()
    
    # numbers
    odd_chaos = [num for num in chaos if num.isdigit() and int(num) % 2 == 1]
    odd_chaos.sort()
    even_chaos = [num for num in chaos if num.isdigit() and int(num) % 2 == 0]
    even_chaos.sort()
    
    # join the parts
    sorted_chaos = "".join(lower_chaos) + "".join(upper_chaos) + "".join(odd_chaos)+ "".join(even_chaos)
    
    print(sorted_chaos)