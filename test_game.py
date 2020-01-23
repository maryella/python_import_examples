# importing outside file allows us to use it in our main game file
import countdowns

# can use function from other file by filename.function_name()
example = countdowns.countdown(10)

# can variables defined in other file with same format filename.variable_name
print("test: ", countdowns.test)
