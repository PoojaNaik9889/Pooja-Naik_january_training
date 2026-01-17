#Message Counter (Immutable Parameter)
# function to count messages

def count_message(msg, count=0):
    count += 1
    print("Message:", msg, "Count:", count)
    return count

count_message("heya")
count_message("hello")
