from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from course.models import User
from course.models import Customer

def is_customer(request):
  user_id            = request.user.id #Current user
  user_exist         = Customer.objects.filter(user_id=user_id)

  if len(user_exist) > 0:
    current_user = Customer.objects.get(user_id=user_id)
    if current_user.paid == True:
      return True
    else:
      return False
  else:
    return False

def is_staff(request):
  user_id      = request.user.id #Current user
  user         = User.objects.get(id=user_id)
  if user.is_staff:
    return True
  else:
    return False

def index(request):
  return render(request, 'course/index.html')

def about(request):
  return render(request, 'course/about.html')

def terms(request):
  return render(request, 'course/terms.html')

def privacy(request):
  return render(request, 'course/privacy.html')

@login_required
def administration(request):
  if is_staff(request):
    return render(request, 'course/administration.html')

@login_required
def add_time(request):
  if is_staff(request):
    return render(request, 'course/add_time.html')

@login_required
def inactivate_account(request):
  if is_staff(request):
    if request.method == "POST":
      user_id          = request.POST['user_id']
      user             = User.objects.get(id=user_id)
      user.is_active   =  0
      user.save()

    return render(request, 'course/inactivate_account.html')

@login_required
def activate_account(request):
  if is_staff(request):
    if request.method == "POST":
      user_id          = request.POST['user_id']
      user             = User.objects.get(id=user_id)
      user.is_active   =  1
      user.save()

    return render(request, 'course/activate_account.html')

@login_required
def submit_time(request):
  if is_staff(request):
    user_id          = request.POST['user_id']
    minutes          = request.POST['add_minutes']
    customer         = Customer.objects.get(user_id=user_id)
    current_minutes  = customer.time_spent
    new_minutes      = (int(current_minutes) + int(minutes))
    customer.time_spent  = new_minutes
    customer.save()

    context = {
      'user_id'       : user_id,
      'new_minutes'   : new_minutes
    }

    return render(request, 'course/submit_time.html', context)

@login_required
def contact(request):
  subject     = "Question from ADA"
  question    = request.POST['message']
  email       = request.POST['email']

  message     = "Email:" + email + " | ID: " + str(request.user.id) + " | Question: " + question

  from_email  = settings.EMAIL_HOST_USER
  password    = settings.EMAIL_HOST_PASSWORD
  to_list     = ['roman.leinwather@gmail.com']

  send_mail(subject, message, from_email, to_list, fail_silently=True)

  return render(request, 'course/contact.html')



@login_required
@require_http_methods(["POST"])
def set_customer_as_paid(request):
  user_id            = request.user.id #Current user
  current_user       = Customer.objects.create(user_id=user_id, paid=True)
  return HttpResponse("OK")

@login_required
def payment(request):
  return render(request, 'course/payment.html')

@login_required
def start(request):
  if is_customer(request):
    return render(request, 'course/start.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def inspiration(request):
  if is_customer(request):
    return render(request, 'course/inspiration.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def tools(request):
  if is_customer(request):
    return render(request, 'course/tools.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def future(request):
  if is_customer(request):
    return render(request, 'course/future.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def benefits(request):
  if is_customer(request):
    return render(request, 'course/benefits.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def grid(request):
  if is_customer(request):
    return render(request, 'course/grid.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def separation(request):
  if is_customer(request):
    return render(request, 'course/separation.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def visual_noise(request):
  if is_customer(request):
    return render(request, 'course/visual_noise.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def balance(request):
  if is_customer(request):
    return render(request, 'course/balance.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def iconography(request):
  if is_customer(request):
    return render(request, 'course/iconography.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def typography_fundation(request):
  if is_customer(request):
    return render(request, 'course/typography_fundation.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def typography_scale(request):
  if is_customer(request):
    return render(request, 'course/typography_scale.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def color_contrast(request):
  if is_customer(request):
    return render(request, 'course/color_contrast.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def color_palette(request):
  if is_customer(request):
    return render(request, 'course/color_palette.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def spacing(request):
  if is_customer(request):
    return render(request, 'course/spacing.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def composition(request):
  if is_customer(request):
    return render(request, 'course/composition.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def consistency(request):
  if is_customer(request):
    return render(request, 'course/consistency.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def resources(request):
  if is_customer(request):
    return render(request, 'course/resources.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def layers(request):
  if is_customer(request):
    return render(request, 'course/layers.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def history_tool(request):
  if is_customer(request):
    return render(request, 'course/history_tool.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def zoom_tool(request):
  if is_customer(request):
    return render(request, 'course/zoom_tool.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def rectangle_tool(request):
  if is_customer(request):
    return render(request, 'course/rectangle_tool.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def elipse_tool(request):
  if is_customer(request):
    return render(request, 'course/elipse_tool.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def line_tool(request):
  if is_customer(request):
    return render(request, 'course/line_tool.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def color(request):
  if is_customer(request):
    return render(request, 'course/color.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def gradient(request):
  if is_customer(request):
    return render(request, 'course/gradient.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def drop_shadow(request):
  if is_customer(request):
    return render(request, 'course/drop_shadow.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def transparency(request):
  if is_customer(request):
    return render(request, 'course/transparency.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def masking(request):
  if is_customer(request):
    return render(request, 'course/masking.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def text_tool(request):
  if is_customer(request):
    return render(request, 'course/text_tool.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def font_icons(request):
  if is_customer(request):
    return render(request, 'course/font_icons.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def text_fields(request):
  if is_customer(request):
    return render(request, 'course/text_fields.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def buttons(request):
  if is_customer(request):
    return render(request, 'course/buttons.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def sliders(request):
  if is_customer(request):
    return render(request, 'course/sliders.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def selection_controls(request):
  if is_customer(request):
    return render(request, 'course/selection_controls.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def chips(request):
  if is_customer(request):
    return render(request, 'course/chips.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def tooltips(request):
  if is_customer(request):
    return render(request, 'course/tooltips.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def cards(request):
  if is_customer(request):
    return render(request, 'course/cards.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def dialogs(request):
  if is_customer(request):
    return render(request, 'course/dialogs.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def lists(request):
  if is_customer(request):
    return render(request, 'course/lists.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def tables(request):
  if is_customer(request):
    return render(request, 'course/tables.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def navigations(request):
  if is_customer(request):
    return render(request, 'course/navigations.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def charts(request):
  if is_customer(request):
    return render(request, 'course/charts.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def menus(request):
  if is_customer(request):
    return render(request, 'course/menus.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def steps(request):
  if is_customer(request):
    return render(request, 'course/steps.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def snackbars(request):
  if is_customer(request):
    return render(request, 'course/snackbars.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def registration_interface(request):
  if is_customer(request):
    return render(request, 'course/registration_interface.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def application_interface(request):
  if is_customer(request):
    return render(request, 'course/application_interface.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def user_flows(request):
  if is_customer(request):
    return render(request, 'course/user_flows.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def interactive_prototype(request):
  if is_customer(request):
    return render(request, 'course/interactive_prototype.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def sample_app_instagram(request):
  if is_customer(request):
    return render(request, 'course/sample_app_instagram.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def sample_app_facebook(request):
  if is_customer(request):
    return render(request, 'course/sample_app_facebook.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def iterations(request):
  if is_customer(request):
    return render(request, 'course/iterations.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def spec(request):
  if is_customer(request):
    return render(request, 'course/rlp_spec.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def wireframes(request):
  if is_customer(request):
    return render(request, 'course/rlp_wireframes.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def rlp_user_flows(request):
  if is_customer(request):
    return render(request, 'course/rlp_user_flows.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def prototype(request):
  if is_customer(request):
    return render(request, 'course/rlp_prototype.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def design(request):
  if is_customer(request):
    return render(request, 'course/rlp_design.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def design_guide(request):
  if is_customer(request):
    return render(request, 'course/rlp_design_guide.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def assets(request):
  if is_customer(request):
    return render(request, 'course/rlp_assets.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def portfolio(request):
  if is_customer(request):
    return render(request, 'course/portfolio.html')
  else:
    return render(request, 'course/payment.html')

@login_required
def client(request):
  if is_customer(request):
    return render(request, 'course/client.html')
  else:
    return render(request, 'course/payment.html')
