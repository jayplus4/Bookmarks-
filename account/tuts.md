# Views

```python
from django.contrib.auth.models import User
from .models import Profile

user = User.objects.get(username="admin")
user.profile.all()

Profile.objects.get(user=user)
```
