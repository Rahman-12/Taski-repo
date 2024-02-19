from django.shortcuts import render
from django.http import HttpResponse
from . import models


# function for the home page
def home(request):
    return render(request, "home.html")


# function for the signup page
def signup(request):
    if request.method == "POST":
        inputed_username = request.POST["username"]
        inputed_password = request.POST["password"]
        inputed_phone_number = request.POST["phone_number"]
        inputed_e_mail = request.POST["e_mail"]
        try:
            existing_customer = models.Customer.objects.filter(
                username=inputed_username
            )
            if existing_customer:
                print(f"error : user {inputed_username} already exists.")
                return HttpResponse(f"username {inputed_username} already exists")
            else:
                print("ready to go ?")
                new_customer = models.Customer(
                    username=inputed_username,
                    password=inputed_password,
                    phone_number=inputed_phone_number,
                    e_mail=inputed_e_mail,
                )
                new_customer.save()
                return HttpResponse(f"Hello {inputed_username}, welcome to my site.")
        except Exception as e:
            print(f"{str(e)}")
        try:
            existing_customer = models.Customer.objects.filter(
                phone_number=inputed_phone_number
            )
            if existing_customer:
                print(f"error : user {inputed_phone_number} already exists.")
                return HttpResponse(
                    f"Phone number, {inputed_phone_number} already exists"
                )
            else:
                print("ready to go ?")

                new_customer = models.Customer(
                    username=inputed_username,
                    password=inputed_password,
                    phone_number=inputed_phone_number,
                    e_mail=inputed_e_mail,
                )
                new_customer.save()
                return HttpResponse(
                    f"Hello {inputed_phone_number}, welcome to my site."
                )
        except Exception as e:
            print(f"{str(e)}")

    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        inputed_username = request.POST["username"]
        inputed_password = request.POST["password"]
        try:
            existing_user = models.Customer.objects.get(username=inputed_username)
            if existing_user:
                if inputed_password == existing_user.password:
                    print("User exists and password is correct")
                else:
                    print("Password is invalid")
            else:
                print("Error : not found")
        except Exception as e:
            print(str(e))
    return render(request, "login.html")


def create_task(request):
    if request.method == "POST":
        inputted_task_name = request.POST["task_name"]
        inputted_task_description = request.POST["task_description"]
        owner_id = request.POST["customer_id"]
        try:
            task_owner = models.Customer.objects.get(id=owner_id)
        except Exception as e:
            return HttpResponse(
                f"Owner with id {owner_id} doesnt not exist, error code : {str(e)}, error code : {str(e)}"
            )
        new_task = models.Task(
            name=inputted_task_name,
            description=inputted_task_description,
            customer_id=task_owner,
        )
        new_task.save()
        return HttpResponse(f"your task{inputted_task_name}, has been created")
    return render(request, "create_task.html")

