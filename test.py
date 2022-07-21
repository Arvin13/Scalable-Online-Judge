from database.forms import NewUserForm
from django.utils import timezone

data = { 'username' : 'arvind1', 'email' : 'arvindmeena8058@gmail.com', 'password' : 'qwertyuiop[]789', 'first_name' : 'Arvind', 'last_name' : 'Meena'}
f = NewUserForm()
f = NewUserForm(data)
f.is_valid

for field in f:
    print("Field Error:", field.name,  field.errors)