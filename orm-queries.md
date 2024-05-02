```python
objects.all()
objects.create()
objects.filter()
objects.get()
objects.add()
objects.save()
objects.remove()
objects.count()

# fetch all data from a table
object.objects.all()
object.objects.all()[index]

# fetch data using constraints
object.objects.get(index or column)
object.objects.get(column='some attribute')
# example Student.objects.get(name='Ali')

# example using lookups 
Student.objects.get(name__startswith='A')
Student.objects.get(name__contains='Ali')

# find objects with relation using predicates
object.objects.get(anotherobject__columnname='some attribute')
# example Student.objects.get(Course__coursename='ERP')

# using lookup
object.objects.get(anotherobject__columnname__startswith='some attribute')
# example Student.objects.get(Course__coursename__startswith='ER')

# filter
object.objects.filter() # returns a list same as all()

# with lookups
object.objects.filter(column__startswith='some attr')

# with multiple lookups AND
object.objects.filter(column__startswith='some attr', column2='some value')

# with relation 1:1 or 1:n etc
object.objects.filter(relation__column__startswith='some attr')

# query set
object.relation_set.all()
object.relation_set.create()
object.relation_set.filter()
object.relation_set.get()
object.relation_set.add()

object.objects.all().relation_set.filter()

studentobject.Course_set.all() # fetch all the courses Student is linked with

Course.objects.get(coursename__startswith='ERP').Student_set.all() # fetches all students who is linked with the course 'ERP'

object.create()
object.save()
```
