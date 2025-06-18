from django.shortcuts import render ,redirect 
import os
from .models import *

def resume_list(request):
    data=ResumeModel.objects.all()
    context={
        'resumes' : data
    }
    return render(request,"list.html",context)
def resume_add(request):
    if request.method == "POST":
      data=ResumeModel(
         FullName=request.POST.get('FullName'),
         ProfilePicture=request.FILES.get('ProfilePicture'),
         Email=request.POST.get('Email'),
         Phone=request.POST.get('Phone'),
         Address=request.POST.get('Address'),
         Summary=request.POST.get('Summary'),
         Degree=request.POST.get('Degree'),
         InstituteName=request.POST.get('InstituteName'),
         YearofGraduation=request.POST.get('YearofGraduation'),
         CompanyName=request.POST.get('CompanyName'),
         Position=request.POST.get('Position'),
         YearsofExperience=request.POST.get('YearsofExperience'),
         Skills=request.POST.get('Skills'),
         Hobbies=request.POST.get('Hobbies'),
         Achievements=request.POST.get('Achievements')

      )
      data.save()
      return redirect('resumelist')
    return render (request,"add.html")
    
def resume_view(request,id):
   data=ResumeModel.objects.get(id=id)
   context={
      'resume' : data
   }
   return render(request,"view.html",context)
def resume_delete(request,id):
   ResumeModel.objects.get(id=id).delete()
   return redirect('resumelist')


def resume_edit(request,id):
   data=ResumeModel.objects.get(id=id)
   ProfilePicture=request.FILES.get('ProfilePicture')
   if ProfilePicture:
            if data.ProfilePicture:
                old_image_path = data.ProfilePicture.path
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)
   else:
            ProfilePicture = data.ProfilePicture 
   if request.method =="POST":
       data=ResumeModel(
         id=id,
         FullName=request.POST.get('FullName'),
         ProfilePicture=ProfilePicture,
         Email=request.POST.get('Email'),
         Phone=request.POST.get('Phone'),
         Address=request.POST.get('Address'),
         Summary=request.POST.get('Summary'),
         Degree=request.POST.get('Degree'),
         InstituteName=request.POST.get('InstituteName'),
         YearofGraduation=request.POST.get('YearofGraduation'),
         CompanyName=request.POST.get('CompanyName'),
         Position=request.POST.get('Position'),
         YearsofExperience=request.POST.get('YearsofExperience'),
         Skills=request.POST.get('Skills'),
         Hobbies=request.POST.get('Hobbies'),
         Achievements=request.POST.get('Achievements')
      )
       data.save()
       return redirect('resumelist')
   context={
      'resume' : data
   }
   return render(request,"edit.html",context)