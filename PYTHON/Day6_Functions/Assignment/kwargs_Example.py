#**kwargs Example

def student_details(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


student_details(
    name="Kamlesh",
    age=22,
    course="Data Engineering"
)