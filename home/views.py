from django.shortcuts import render, redirect
from .models import Category, ElectricianService, ApplianceService, PlumberService, CarpenterService, PainterService, CleaningService, SalonService, MainService, Booking
from .forms import BookingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm

# Existing views
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        description = request.POST.get("description")
        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            description=description
        )
        return render(request, 'home/home.html', {'success': True})
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')
def contact(request):
    return render(request, 'home/contact.html')

def services(request):
    main_services = MainService.objects.all()
    return render(request, 'home/services.html', {'main_services': main_services})

# Rename this function to match the URL pattern
def electrician(request):
    services = ElectricianService.objects.all()
    return render(request, 'home/electrician.html', {'services': services})

def appliance(request):
    ac_services = ApplianceService.objects.filter(category='AC')
    wm_services = ApplianceService.objects.filter(category='WM')
    rf_services = ApplianceService.objects.filter(category='RF')
    return render(request, 'home/appliance.html', {
        'ac_services': ac_services,
        'wm_services': wm_services,
        'rf_services': rf_services,
    })
def plumber(request):
    services = PlumberService.objects.all()
    return render(request, 'home/plumber.html', {'services': services})
def carpenter(request):
    services = CarpenterService.objects.all()
    return render(request, 'home/carpenter.html', {'services': services})
def painter(request):
    services = PainterService.objects.all()
    return render(request, 'home/painter.html', {'services': services})
def cleaning(request):
    services = CleaningService.objects.all()
    return render(request, 'home/cleaning.html', {'services': services})
def salon(request):
    women_services = SalonService.objects.filter(gender='Women')
    men_services = SalonService.objects.filter(gender='Men')
    return render(request, 'home/salon.html', {
        'women_services': women_services,
        'men_services': men_services,
    })

def register(request):
    success = False
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            success = True
            form = RegisterForm()  # Reset form
    else:
        form = RegisterForm()
    return render(request, 'home/register.html', {'form': form, 'success': success})

def Login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})

def booking_view(request):
    booking_number = None
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking_number = booking.booking_number
            return render(request, 'home/bookingform.html', {
                'form': BookingForm(),
                'success': True,
                'booking_number': booking_number
            })
    else:
        form = BookingForm()
    return render(request, 'home/bookingform.html', {'form': form})

def custom_logout(request):
    logout(request)
    return render(request, 'home/logout.html')