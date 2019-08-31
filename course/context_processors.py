from course.models import Customer

# The context processor function
def all_lessons(request):
  all_lessons       = 62

  return {
      'all_lessons': all_lessons,
  }


def time_spent(request):
  if request.user.id:
    user_id          = request.user.id
    user_exist       = Customer.objects.filter(user_id=user_id)

    if len(user_exist) > 0:
      customer       = Customer.objects.get(user_id=user_id)
      time_spent     = customer.time_spent
      time_percent   = time_spent / (120/100)
    else:
      time_spent     =  0
      time_percent   = 0

    return {
      'time_spent': time_spent,
      'time_percent': time_percent,
    }

  else:
    return {
      'time_spent': 0,
      'time_percent': 0,
    }
