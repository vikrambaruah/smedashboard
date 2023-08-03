from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dashboard_app_main.forms import UserForm
import requests
import xml.etree.ElementTree as ET
from .models import AccumulatedTime, AxisFeedrate,AxisFeedrate2, Position, User, Temperature
import json
import time
import big_o
import csv
class IndexView(View):
    def get(self,request):
        return render(request,'dashboard_app_main/index.html')
    def post (self,request):
        return render(request,'dashboard_app_main/index.html')
# Create your views here.
# class ParseXMLView(View):
#     def get(self, request):
#         # Fetch XML data from the API
#         url = "http://mtconnect.mazakcorp.com:5609/sample"
#         response = requests.get(url)
#         xml_data = response.content

#         # Parse the XML data
        
#         root = ET.fromstring(xml_data)
#         for child in root.iter('*'):
#             if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AccumulatedTime"):
#                 atime=AccumulatedTime()
#                 atime.timestamp=child.attrib["timestamp"]
#                 atime.name = child.attrib["name"]
#                 atime.sequence = child.attrib["sequence"]
#                 atime.subType = child.attrib["subType"]
#                 atime.value = int(child.text)
#                 print(child.attrib["timestamp"])
#                 atime.save()
        # for accumulated_time in accumulated_times:
        #     atime = AccumulatedTime()
        #     atime.timestamp = accumulated_time.attrib["timestamp"]
        #     atime.name = accumulated_time.attrib["name"]
        #     atime.sequence = accumulated_time.attrib["sequence"]
        #     atime.subType = accumulated_time.attrib["subType"]
        #     atime.value = accumulated_time.text
        #     atime.save()

        # Process AxisFeedrate elements
        # axis_feedrates = component_stream.findall("./Samples/AxisFeedrate")
        # for axis_feedrate in axis_feedrates:
        #     af = AxisFeedrate()
        #     af.timestamp = axis_feedrate.attrib["timestamp"]
        #     af.name = axis_feedrate.attrib["name"]
        #     af.sequence = axis_feedrate.attrib["sequence"]
        #     af.value = axis_feedrate.text
        #     af.save()

        # # Process Position elements
        # positions = component_stream.findall("./Samples/Position")
        # for position in positions:
        #     pos = Position()
        #     pos.timestamp = position.attrib["timestamp"]
        #     pos.name = position.attrib["name"]
        #     pos.sequence = position.attrib["sequence"]
        #     pos.subType = position.attrib["subType"]
        #     pos.value = position
class DownloadCSVTime(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5609/sample"
        response = requests.get(url)
        xml_data = response.content
        
        root = ET.fromstring(xml_data)
        AccumulatedTime.objects.all().delete()
        AxisFeedrate.objects.all().delete()
        Position.objects.all().delete()
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}ComponentStream"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AccumulatedTime"):
                        atime=AccumulatedTime()
                        atime.component=component
                        atime.component_id=component_id
                        atime.component_name=component_name
                        atime.component=child.attrib["name"]
                        atime.timestamp=child.attrib["timestamp"]
                        atime.name = child.attrib["name"]
                        atime.sequence = child.attrib["sequence"]
                        atime.subType = child.attrib["subType"]
                        atime.value = int(child.text)
                        atime.save()
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AxisFeedrate"):
                        ax=AxisFeedrate()
                        ax.component=component
                        ax.component_id=component_id
                        ax.component_name=component_name
                        ax.timestamp=child.attrib["timestamp"]
                        ax.name = child.attrib["name"]
                        ax.sequence = child.attrib["sequence"]
                        ax.value = float(child.text)
                        ax.save()
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}Position"):
                        pos=Position()
                        pos.component=component
                        pos.component_id=component_id
                        pos.component_name=component_name
                        pos.timestamp=child.attrib["timestamp"]
                        pos.name = child.attrib["name"]
                        pos.sequence = child.attrib["sequence"]
                        pos.subType = child.attrib["subType"]
                        pos.value = float(child.text)
                        pos.save()
        
        
        # Fetch data from the database
        data = AccumulatedTime.objects.all()

        # Create a CSV writer
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Create a CSV writer
        writer = csv.writer(response)
        writer.writerow(['Component', 'Component Name', 'Component ID', 'Timestamp', 'Name', 'Sequence', 'Value'])

        # Write data rows to the CSV
        for item in data:
            writer.writerow([
                item.component,
                item.component_name,
                item.component_id,
                item.timestamp,
                item.name,
                item.sequence,
                item.value,
            ])

        return response
class DownloadCSVPosition(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5609/sample"
        response = requests.get(url)
        xml_data = response.content
        
        root = ET.fromstring(xml_data)
        AccumulatedTime.objects.all().delete()
        AxisFeedrate.objects.all().delete()
        Position.objects.all().delete()
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}ComponentStream"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AccumulatedTime"):
                        atime=AccumulatedTime()
                        atime.component=component
                        atime.component_id=component_id
                        atime.component_name=component_name
                        atime.component=child.attrib["name"]
                        atime.timestamp=child.attrib["timestamp"]
                        atime.name = child.attrib["name"]
                        atime.sequence = child.attrib["sequence"]
                        atime.subType = child.attrib["subType"]
                        atime.value = int(child.text)
                        atime.save()
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AxisFeedrate"):
                        ax=AxisFeedrate()
                        ax.component=component
                        ax.component_id=component_id
                        ax.component_name=component_name
                        ax.timestamp=child.attrib["timestamp"]
                        ax.name = child.attrib["name"]
                        ax.sequence = child.attrib["sequence"]
                        ax.value = float(child.text)
                        ax.save()
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}Position"):
                        pos=Position()
                        pos.component=component
                        pos.component_id=component_id
                        pos.component_name=component_name
                        pos.timestamp=child.attrib["timestamp"]
                        pos.name = child.attrib["name"]
                        pos.sequence = child.attrib["sequence"]
                        pos.subType = child.attrib["subType"]
                        pos.value = float(child.text)
                        pos.save()
        
        
        # Fetch data from the database
        data = Position.objects.all()

        # Create a CSV writer
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Create a CSV writer
        writer = csv.writer(response)
        writer.writerow(['Component', 'Component Name', 'Component ID', 'Timestamp', 'Name', 'Sequence', 'Value'])

        # Write data rows to the CSV
        for item in data:
            writer.writerow([
                item.component,
                item.component_name,
                item.component_id,
                item.timestamp,
                item.name,
                item.sequence,
                item.value,
            ])

        return response
class DownloadCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5609/sample"
        response = requests.get(url)
        xml_data = response.content
        
        root = ET.fromstring(xml_data)
        AccumulatedTime.objects.all().delete()
        AxisFeedrate.objects.all().delete()
        Position.objects.all().delete()
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}ComponentStream"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AxisFeedrate"):
                        ax=AxisFeedrate()
                        ax.component=component
                        ax.component_id=component_id
                        ax.component_name=component_name
                        ax.timestamp=child.attrib["timestamp"]
                        ax.name = child.attrib["name"]
                        ax.sequence = child.attrib["sequence"]
                        ax.value = float(child.text)
                        ax.save()
        
        
        # Fetch data from the database
        data = AxisFeedrate.objects.all()

        # Create a CSV writer
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Create a CSV writer
        writer = csv.writer(response)
        writer.writerow(['Component', 'Component Name', 'Component ID', 'Timestamp', 'Name', 'Sequence', 'Value'])

        # Write data rows to the CSV
        for item in data:
            writer.writerow([
                item.component,
                item.component_name,
                item.component_id,
                item.timestamp,
                item.name,
                item.sequence,
                item.value,
            ])

        return response

class RegisterView(View):
    #get the register form
    def get(self,request):
        registered=False
        user_form = UserForm()
        return render(request, 'dashboard_app_main/register.html',context={ 'user_form':user_form,
                                                                      'registered':registered})

    #post the register form
    def post(self,request):
        registered=False
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            registered=True
            return render(request, 'dashboard_app_main/login.html')
        else:
            print(user_form.errors)
        return render(request, 'dashboard_app_main/register.html',context={ 'user_form':user_form,
                                                                      'registered':registered})

class LoginView(View):
    #if request is get send the log in form
    def get(self,request):
        return render(request, 'dashboard_app_main/login.html')
    
    #if request is post then check and log user in
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate teh username and password recieved
        user = authenticate(username = username, password = password)
        if user:
            #is the account active? it could have been disabled
            if user.is_active:
                #if the account is valid and active we can log the user in
                #we will send the user to the respective dashboard
                login(request,user)
                return redirect('dashboard_app_main:dashboard')
            else:
                #if an inactive account was used we are not logging them in
                return HttpResponse("Your account is disabled.")
        else:
            #bad login details were provided, so we can't log user in
            print(f"Invalid user details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

#logout view
class LogoutView(View):
    @method_decorator(login_required)
    def get(self,request):
        logout(request)
        return redirect(reverse('dashboard_app_main:index'))
class DashboardData(View):
    def get(self,request):
        start_time=time.time()
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5609/sample"
        response = requests.get(url)
        xml_data = response.content

        
        response_time=(time.time() - start_time)*1000
        root = ET.fromstring(xml_data)
        AccumulatedTime.objects.all().delete()
        AxisFeedrate.objects.all().delete()
        Position.objects.all().delete()
        
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}DeviceStream"):
                device_name=c.attrib["name"]
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}ComponentStream"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AccumulatedTime"):
                        atime=AccumulatedTime()
                        atime.component=component
                        atime.component_id=component_id
                        atime.component_name=component_name
                        atime.component=child.attrib["name"]
                        atime.timestamp=child.attrib["timestamp"]
                        atime.name = child.attrib["name"]
                        atime.sequence = child.attrib["sequence"]
                        atime.subType = child.attrib["subType"]
                        atime.value = int(child.text)
                        atime.save()
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AxisFeedrate"):
                        ax=AxisFeedrate()
                        ax.component=component
                        ax.component_id=component_id
                        ax.component_name=component_name
                        ax.timestamp=child.attrib["timestamp"]
                        ax.name = child.attrib["name"]
                        ax.sequence = child.attrib["sequence"]
                        ax.value = float(child.text)
                        ax.save()
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}Position"):
                        pos=Position()
                        pos.component=component
                        pos.component_id=component_id
                        pos.component_name=component_name
                        pos.timestamp=child.attrib["timestamp"]
                        pos.name = child.attrib["name"]
                        pos.sequence = child.attrib["sequence"]
                        pos.subType = child.attrib["subType"]
                        pos.value = float(child.text)
                        pos.save()
        accumulated = json.dumps([
            {
                'timestamp': item.timestamp.isoformat(),
                'value': item.value,
                'component':item.component,
                'component_name':item.component_name,
                'component_id':item.component_id,
                'name':item.name,
                'sequence':item.sequence,
            }
            for item in AccumulatedTime.objects.all()
        ])

        axis = json.dumps([
            {
                'timestamp': item.timestamp.isoformat(),
                'value': item.value,
                'component':item.component,
                'component_name':item.component_name,
                'component_id':item.component_id,
                'name':item.name,
                'sequence':item.sequence
                
            }
            for item in AxisFeedrate.objects.all()
        ])

        position = json.dumps([
            {
                'timestamp': item.timestamp.isoformat(),
                'value': item.value,
                'component':item.component,
                'component_name':item.component_name,
                'component_id':item.component_id,
                'name':item.name,
                'sequence':item.sequence
            }
            for item in Position.objects.all()
        ])

        return render(request, 'dashboard_app_main/dashboardtest.html', context={'accumulated': accumulated, 'axis': axis, 'position': position,'response':response_time,'device':device_name})
class Dashboard(View):
    @method_decorator(login_required)
    def get(self,request):
        start_time = time.time()
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5609/sample"
        response = requests.get(url)
        xml_data = response.content

        response_time=(time.time() - start_time)*1000
        
        root = ET.fromstring(xml_data)
        AccumulatedTime.objects.all().delete()
        AxisFeedrate.objects.all().delete()
        Position.objects.all().delete()
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}ComponentStream"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AccumulatedTime"):
                        atime=AccumulatedTime()
                        atime.component=component
                        atime.component_id=component_id
                        atime.component_name=component_name
                        atime.component=child.attrib["name"]
                        atime.timestamp=child.attrib["timestamp"]
                        atime.name = child.attrib["name"]
                        atime.sequence = child.attrib["sequence"]
                        atime.subType = child.attrib["subType"]
                        atime.value = int(child.text)
                        atime.save()
        accumulated = json.dumps([
            {
                'timestamp': item.timestamp.isoformat(),
                'value': item.value
            }
            for item in AccumulatedTime.objects.all()
        ])


        
        return render(request, 'dashboard_app_main/dashboard.html', context={'accumulated': accumulated,'response':response_time})
        #return render (request, 'dashboard_app_main/dashboard.html', context={'accumulated':AccumulatedTime.objects.all(),'axis':AxisFeedrate.objects.all(),'position':Position.objects.all()})
        

class DashboardAxis(View):
    def get(self,request):
        start_time=time.time()
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5609/sample"
        response = requests.get(url)
        xml_data = response.content

        
        response_time=(time.time() - start_time)*1000
        root = ET.fromstring(xml_data)
        AccumulatedTime.objects.all().delete()
        AxisFeedrate.objects.all().delete()
        Position.objects.all().delete()
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}ComponentStream"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}AxisFeedrate"):
                        ax=AxisFeedrate()
                        ax.component=component
                        ax.component_id=component_id
                        ax.component_name=component_name
                        ax.timestamp=child.attrib["timestamp"]
                        ax.name = child.attrib["name"]
                        ax.sequence = child.attrib["sequence"]
                        ax.value = float(child.text)
                        ax.save()
        axis = json.dumps([
            {
                'timestamp': item.timestamp.isoformat(),
                'value': item.value,
                'component':item.component,
                'component_name':item.component_name,
                'component_id':item.component_id,
                'name':item.name,
                'sequence':item.sequence
                
            }
            for item in AxisFeedrate.objects.all()
        ])
        return render(request, 'dashboard_app_main/dashboardaxis.html', context={'axis': axis,'response':response_time})
    
class DashboardPosition(View):
    def get(self,request):
        start_time=time.time()
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5609/sample"
        response = requests.get(url)
        xml_data = response.content
        response_time=(time.time() - start_time)*1000
        
        
        root = ET.fromstring(xml_data)
        AccumulatedTime.objects.all().delete()
        AxisFeedrate.objects.all().delete()
        Position.objects.all().delete()
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}ComponentStream"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.3}Position"):
                        pos=Position()
                        pos.component=component
                        pos.component_id=component_id
                        pos.component_name=component_name
                        pos.timestamp=child.attrib["timestamp"]
                        pos.name = child.attrib["name"]
                        pos.sequence = child.attrib["sequence"]
                        pos.subType = child.attrib["subType"]
                        pos.value = float(child.text)
                        pos.save()
       
        position = json.dumps([
            {
                'component_name':item.component_name,
                'timestamp': item.timestamp.isoformat(),
                'value': item.value
            }
            for item in Position.objects.all()
        ])

        return render(request, 'dashboard_app_main/dashboardposition.html', context={'position': position,'response':response_time})

class DashboardTemperature(View):
    def get(self,request):
        start_time=time.time()
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5611/sample"
        response = requests.get(url)
        xml_data = response.content

        
        response_time=(time.time() - start_time)*1000
        root = ET.fromstring(xml_data)
        # AccumulatedTime.objects.all().delete()
        # AxisFeedrate.objects.all().delete()
        # Position.objects.all().delete()
        device_state="on"
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}DeviceStream"):
                device_name=c.attrib["name"]
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}ComponentStream" and c.attrib["component"]=="Device"):
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}EquipmentMode"):
                        device_state=str(child.text)
                        print(device_state)
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}ComponentStream" and c.attrib["component"]=="Rotary"):
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}Temperature"):
                        temp=Temperature()
                        temp.timestamp=child.attrib["timestamp"]
                        temp.sequence=child.attrib["sequence"]
                        #temp.dataItemId=child.attrib["dataItemId"]
                        temp.composition_id=child.attrib["compositionId"]
                        temp.value=float(child.text)
                        temp.save()
      

        temperature = json.dumps([
            {
                'timestamp': item.timestamp.isoformat(),
                'value': item.value,
                'composition_id':item.composition_id,
                #'dataItemId':item.dataItemId,
                'sequence':item.sequence,
            }
            for item in Temperature.objects.all()
        ])

        

        return render(request, 'dashboard_app_main/dashboardtemperature.html', context={'temperature': temperature,'response':response_time,'device_state':device_state,'device_name':device_name})
  
class DashboardAxis2(View):
    def get(self,request):
        start_time=time.time()
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5611/sample"
        response = requests.get(url)
        xml_data = response.content

        
        response_time=(time.time() - start_time)*1000
        root = ET.fromstring(xml_data)
        # AccumulatedTime.objects.all().delete()
        # AxisFeedrate.objects.all().delete()
        # Position.objects.all().delete()
        device_state="on"
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}DeviceStream"):
                device_name=c.attrib["name"]
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}ComponentStream" and c.attrib["component"]=="Device"):
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}EquipmentMode"):
                        device_state=str(child.text)
                        print(device_state)
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}ComponentStream" and c.attrib["component"]=="Linear"):

                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}AxisFeedrate"):
                        ax=AxisFeedrate2()
                        ax.component=component
                        ax.component_id=component_id
                        ax.component_name=component_name
                        ax.timestamp=child.attrib["timestamp"]
                        ax.dataItemId=child.attrib["dataItemId"]
                        ax.sequence = child.attrib["sequence"]
                        ax.value = float(child.text)
                        ax.save()    
      

        axis = json.dumps([
            {
                'timestamp': item.timestamp.isoformat(),
                'value': item.value,
                'component':item.component,
                'component_name':item.component_name,
                'component_id':item.component_id,
                'sequence':item.sequence,
            }
            for item in AxisFeedrate2.objects.all()
        ])

        

        return render(request, 'dashboard_app_main/dashboardaxis.html', context={'axis': axis,'response':response_time,'device_state':device_state,'device_name':device_name})
    
class DownloadCSV2(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        context_dict ={}
        url = "http://mtconnect.mazakcorp.com:5611/sample"
        response = requests.get(url)
        xml_data = response.content
        
        root = ET.fromstring(xml_data)
        for c in root.iter('*'):
            if (c.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}ComponentStream" and c.attrib["component"]=="Linear"):
                component_name=c.attrib["name"]
                component=c.attrib["component"]
                component_id=c.attrib["componentId"]
                for child in c.iter('*'): 
                    if(child.tag=="{urn:mtconnect.org:MTConnectStreams:1.4}AxisFeedrate"):
                        ax=AxisFeedrate2()
                        ax.component=component
                        ax.component_id=component_id
                        ax.component_name=component_name
                        ax.timestamp=child.attrib["timestamp"]
                        ax.sequence = child.attrib["sequence"]
                        ax.value = float(child.text)
                        ax.save()
        
        # Fetch data from the database
        data = AxisFeedrate2.objects.all()

        # Create a CSV writer
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Create a CSV writer
        writer = csv.writer(response)
        writer.writerow(['Component', 'Component Name', 'Component ID', 'Timestamp', 'Sequence', 'Value'])

        # Write data rows to the CSV
        for item in data:
            writer.writerow([
                item.component,
                item.component_name,
                item.component_id,
                item.timestamp,
                item.sequence,
                item.value,
            ])

        return response