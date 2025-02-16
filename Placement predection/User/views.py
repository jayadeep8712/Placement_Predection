from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
# from django.contrib import auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def error_(request):
    return render(request,'error_.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method == "POST":
        u=request.POST['uname']
        p=request.POST['psw']
        user = auth.authenticate(username=u, password=p)
        if user is not None:
            auth.login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,"Invalid username or password")
            return render(request,'login.html')
    return render(request,"login.html")


def signup(request):
    if request.method == 'POST':
        u=request.POST['uname']
        e=request.POST['email']
        p1=request.POST['psw']
        p2=request.POST['psw-repeat']
        if p1==p2:
            if User.objects.filter(username=u).exists():
                messages.info(request,"Username already exists")
                return redirect('login')
            elif User.objects.filter(email=e).exists():
                messages.info(request,"Email Id already registered")
                return render(request,"login.html")
            else:
                user =User.objects.create_user(username=u, email=e, password=p2, first_name=u, last_name=u)
                user.save()
                return render(request,"index.html")
        else:
            messages.info(request,"Passwords do not match")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    return render(request,"login.html")

def placement(request):
    return render(request,'placement.html')

# --------------Prediction code-------------------------

# import io
# import base64
# # import matplotlib.pyplot as plt
# import numpy as np
# from django.contrib import messages
# from django.shortcuts import render
# from sklearn.tree import DecisionTreeClassifier

# def prediction(request):
#     if request.method == "POST":
#         age = int(request.POST.get("age"))
#         gender = request.POST.get("gender")
#         stream = request.POST.get("stream")
#         intern = request.POST.get("intern")
#         cgpa = int(request.POST.get("cgpa"))
#         hostel = request.POST.get("hostel")
#         back = request.POST.get("back")
#         # k = float(request.POST.get("klvl"))

#         gender_dict = {
#             'Male': 1,
#             'Female': 2
#         }

#         stream_dict = {
#             'Electronics And Communication': 0,
#             'Computer Science': 1,
#             'Mechanical': 2,
#             'Civil': 3,
#             'Information Technology': 4,
#             'Electrical': 5
#         }
#         import pandas as pd
#         df = pd.read_csv(r"static/dataset/collegePlace.csv")

#         df['gender_Num'] = df['Gender'].map(gender_dict)
#         df['stream_Num'] = df['Stream'].map(stream_dict)

#         # plt.xlabel('PlacedOrNot')
#         # plt.ylabel('Count')
#         # plt.title('PlacedOrNot Distribution')

#         # buf = io.BytesIO()
#         # plt.savefig(buf, format='png')
#         # plt.close()
#         # buf.seek(0)
#         # plot_data = base64.b64encode(buf.read()).decode('utf-8')

#         X_train = df[["Age", "gender_Num ", "stream_Num", "Internships", "CGPA", "Hostel", "HistoryOfBacklogs"]]
#         y_train = df["PlacedOrNot"]

#         r = DecisionTreeClassifier()
#         r.fit(X_train, y_train)

#         data = np.array([[age, gender_dict[gender], stream_dict[stream], intern, cgpa, hostel, back]], dtype=int)
#         pred_outcome = r.predict(data)

#         return render(request, "prediction.html", {
#             "age": age,
#             "gender": gender,
#             "stream": stream,
#             "intern": intern,
#             "cgpa": cgpa,
#             "hostel": hostel,
#             "back": back,
#             "output": pred_outcome,
#             # "plot_data": plot_data
#         })

#     return render(request, "prediction.html")

import io
import base64
import numpy as np
from django.contrib import messages
from django.shortcuts import render
from sklearn.tree import DecisionTreeClassifier

def prediction(request):
    if request.method == "POST":
        age = float(request.POST.get("age"))
        gender = request.POST.get("gender")
        stream = request.POST.get("stream")
        intern = float(request.POST.get("intern"))  # Convert to integer
        cgpa = float(request.POST.get("cgpa"))     # Convert to float
        hostel = float(request.POST.get("hostel"))    # Convert to integer
        back = float(request.POST.get("back"))        # Convert to integer

        gender_dict = {
            'Male': 1,
            'Female': 0
        }

        stream_dict = {
            'Electronics And Communication': 0,
            'Computer Science': 1,
            'Mechanical': 2,
            'Civil': 3,
            'Information Technology': 4,
            'Electrical': 5
        }

        import pandas as pd
        df = pd.read_csv(r"static/dataset/collegePlace.csv")

        df['gender_Num'] = df['Gender'].map(gender_dict)
        df['stream_Num'] = df['Stream'].map(stream_dict)
        X_train = df[["Age", "gender_Num", "stream_Num", "Internships", "CGPA", "Hostel", "HistoryOfBacklogs"]]
        y_train = df["PlacedOrNot"]

        r = DecisionTreeClassifier()
        r.fit(X_train, y_train)

        data = np.array([[age, gender_dict[gender], stream_dict[stream], intern, cgpa, hostel, back]], dtype=float)
        pred_outcome = r.predict(data)

        if intern == 1:
            intern_message = "Yes"
        else:
            intern_message = "No"
        
        if hostel == 1:
            hostel_message = "Hosteller"
        else:
            hostel_message = "Dayscholar"

        if back == 1:
            back_message = "Yes"
        else:
            back_message = "No"

        if pred_outcome[0] == 1:
            prediction_message = "You will be placed."
        else:
            prediction_message = "Sorry, you will not be placed."

        return render(request, "prediction.html", {
            "age": age,
            "gender": gender,
            "stream": stream,
            "intern": intern_message,
            "cgpa": cgpa,
            "hostel": hostel_message,
            "back": back_message,
            #"output": pred_outcome,
            "output": prediction_message,
        })

    return render(request, "prediction.html")
