def print_keyword_args(**kwargs):
     # kwargs is a dict of the keyword args passed to the function
    for key, value in kwargs.iteritems():
        print "%s = %s" % (key, value)

print_keyword_args(first_name="John", last_name="Doe", middle_name="Freakin'")
#first_name = John
#last_name = Doe