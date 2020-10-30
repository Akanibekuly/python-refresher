def divide(dividend,divisor):
    if divisor==0:
        raise ZeroDivisionError("Divisor cannot be zero.")
        
    return dividend/divisor

# divide(15,0)

students=[
    {"name": "Bob","grades":[75,90]},
    {"name": "Rolf","grades":[50]},
    {"name": "Jen","grades":[100,90]}
]
grades=[]

print("Welcome to average grade programm")
try: 
    for student in students:
        name=student["name"]
        grades=student["grades"]
        average=divide(sum(grades),len(grades))
        print(f"{name } averaged {average}")
except ZeroDivisionError: 
    print(f"ERROR {name} has no grades!")
else:
    print("-- All students averages calculated --")
finally: 
    print("-- End of tudent average calcualtions --")
