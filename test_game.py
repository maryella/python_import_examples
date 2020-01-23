# importing outside file allows us to use it in our main game file
import countdown_function
import variable

# can use function from other file by filename.function_name()
example = countdown_function.countdown(10)

# can variables defined in other file with same format filename.variable_name
print("Test from variable.py: ", variable.test)
