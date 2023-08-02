from textwrap import shorten
from django.shortcuts import render
from patient.models import Predictions
from .data_provider import *
# Create your views here.

def my_predictions(request):
    predictions = Predictions.objects.filter(user=request.user)
    return render(request,'patient/my_predictions.html',{'predictions':predictions})


def prediction_view(request,id):
    prediction = Predictions.objects.get(id=id)
    return render(request,'patient/prediction_view.html',{'prediction':prediction})

def predict(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        gender = int(request.POST['gender'])
        air_polution = int(request.POST['air_polution'])
        chronic_lung_disease = int(request.POST['chronic_lung_disease'])
        shortness_of_breath = int(request.POST['shortness_of_breath'])
        hoarseness = int(request.POST['hoarseness'])
        weight_loss = int(request.POST['weight_loss'])
        chest_pain = int(request.POST['chest_pain'])
        coughing_of_blood = int(request.POST['coughing_of_blood'])
        headache = int(request.POST['headache'])
        loss_of_memmory = int(request.POST['loss_of_memmory'])
        red_spot_in_skin = int(request.POST['red_spot_in_skin'])
        fever = int(request.POST['fever'])
        nose_bleeding = int(request.POST['nose_bleeding'])
        bleeding_easily = int(request.POST['bleeding_easily'])
        night_sweating = int(request.POST['night_sweating'])
        vomiting = int(request.POST['vomiting'])
        abdomen_discomfort = int(request.POST['abdomen_discomfort'])
        bleeding_stools = int(request.POST['stool_bleeding'])
        jaundice = int(request.POST['jaundice'])
        stomach_pain = int(request.POST['stomach_pain'])
        alcoholic = int(request.POST['alcoholic'])
        dust_alergy = int(request.POST['dust_alergy'])
        balanced_diet = int(request.POST['balanced_diet'])
        obesity = int(request.POST['obesity'])
        smoking = int(request.POST['smoking'])
        fatigue = int(request.POST['fatigue'])
        wheezing = int(request.POST['wheezing'])
        swallowing_difficulty = int(request.POST['Swallowing_difficulty'])
        clubbing_of_nails = int(request.POST['clubbing_of_nails'])
        frequent_cold = int(request.POST['frequent_cold'])
        dry_cough = int(request.POST['dry_cough'])
        is_cancer = True
        if chronic_lung_disease == 0 and shortness_of_breath == 0 and chest_pain == 0 and coughing_of_blood == 0 and loss_of_memmory == 0 and red_spot_in_skin == 0 and nose_bleeding == 0 and bleeding_easily == 0 and night_sweating == 0 and vomiting == 0 and bleeding_stools == 0 and jaundice == 0 and stomach_pain == 0 and alcoholic == 0 and obesity == 0 and smoking == 0 and fatigue == 0 and wheezing == 0 and swallowing_difficulty == 0 and clubbing_of_nails == 0:
            is_cancer = False
        
        features =[[ age,
        gender,
        air_polution,
        chronic_lung_disease,
        shortness_of_breath,
        hoarseness,
        weight_loss,
        chest_pain,
        coughing_of_blood,
        headache,
        loss_of_memmory,
        red_spot_in_skin,
        fever,
        nose_bleeding,
        bleeding_easily,
        night_sweating,
        vomiting,
        abdomen_discomfort,
        bleeding_stools,
        jaundice,
        stomach_pain,
        alcoholic,
        dust_alergy,
        balanced_diet,
        obesity,
        smoking,
        fatigue,
        wheezing,
        swallowing_difficulty,
        clubbing_of_nails,
        frequent_cold,
        dry_cough]]
        print(features)
        SVMClassifier,KNNClassifier,KMeansClassifier,DecisionTreeClassifier,RandomForestClassifier=GetAllClassifiers()
        predictions = {'SVMClassifier': str(SVMClassifier.predict(features)[0]),
            'KNearestNeighbours': str(KNNClassifier.predict(features)[0]),
             'KMeansClassifier': str(KMeansClassifier.predict(features)[0]),
             'DecisionTree': str(DecisionTreeClassifier.predict(features)[0]),
             'RandomForestClassifier': str(RandomForestClassifier.predict(features)[0]),
        }
            

        l=[predictions['SVMClassifier'],predictions['KNearestNeighbours'],predictions['KMeansClassifier'],predictions['DecisionTree'],predictions['RandomForestClassifier']]
        lc_count=l.count('1') #Lung Cancer
        bc_count=l.count('2') #Blood Cancer
        sc_count=l.count('3') #Stomach Cancer
        result=True


        if lc_count>sc_count and lc_count>bc_count:
            result=True
            pred_num=1
        elif sc_count>lc_count and sc_count>bc_count:
            result=True
            pred_num=3
        elif bc_count>lc_count and bc_count>sc_count:
            result=True
            pred_num=2
        elif sc_count == lc_count and bc_count < sc_count:
            result=True
            pred_num=4
        elif sc_count == bc_count and lc_count < sc_count:
            result=True
            pred_num=5
        elif bc_count == lc_count and sc_count < bc_count:
            result=True
            pred_num=6
        else:
            result=True
            pred_num=2
        if is_cancer:
            pnum = pred_num
        else:
            pnum = 0
        pred_data = Predictions()
        pred_data.user = request.user
        pred_data.age = age
        pred_data.gender = gender
        pred_data.air_polution = air_polution
        pred_data.alcohol = alcoholic
        pred_data.dust_alergy = dust_alergy
        pred_data.chronic_lung_disease = chronic_lung_disease
        pred_data.balanced_diet = balanced_diet
        pred_data.obesity = obesity
        pred_data.smoking = smoking
        pred_data.chest_pain = chest_pain
        pred_data.coughing_of_blood = coughing_of_blood
        pred_data.fatigue = fatigue
        pred_data.weight_loss = weight_loss
        pred_data.shortness_of_breath = shortness_of_breath
        pred_data.weezing = wheezing
        pred_data.swallowing_dificulty =swallowing_difficulty
        pred_data.clubbing_of_nails = clubbing_of_nails
        pred_data.frequent_cold = frequent_cold
        pred_data.dry_cough = dry_cough
        pred_data.num= pnum
        hoarseness = hoarseness
        headache = headache
        loss_of_memmory = loss_of_memmory
        red_spot_in_skin = red_spot_in_skin
        fever = fever
        nose_bleeding = nose_bleeding
        bleeding_easily = bleeding_easily
        night_sweating = night_sweating
        vomiting = vomiting
        abdomen_discomfort = abdomen_discomfort
        bleeding_stools = bleeding_stools
        jaundice = jaundice
        stomach_pain = stomach_pain
        pred_data.save()

        colors={}
        if pred_num==1:
            pd="Lung Cancer"
        elif pred_num==3:
            pd="Stomach Cancer"
        elif pred_num==2:
            pd="Blood Cancer"
        elif pred_num==4:
            pd="Stomach Cancer / Lung Cancer"
        elif pred_num==5:
            pd="Stomach Cancer / Blood Cancer"
        elif pred_num==6:
            pd="Lung Cancer / Blood Cancer"    
        else:
            pred_num=2
            pd="Blood Cancer"


        if predictions['SVMClassifier']=='1':
            predictions['SVMClassifier']="Lung Cancer"
        elif predictions['SVMClassifier']=='3':
            predictions['SVMClassifier']="Stomach Cancer"
        elif predictions['SVMClassifier']=='2':
            predictions['SVMClassifier']="Blood Cancer"
        elif pred_num==1:
            predictions['SVMClassifier']="Lung Cancer"
        elif pred_num==3:
            predictions['SVMClassifier']="Stomach Cancer"
        else:
            predictions['SVMClassifier']="Blood Cancer"

        if predictions['KNearestNeighbours']=='1':
            predictions['KNearestNeighbours']="Lung Cancer"
        elif predictions['KNearestNeighbours']=='3':
            predictions['KNearestNeighbours']="Stomach Cancer"
        elif predictions['KNearestNeighbours']=='2':
            predictions['KNearestNeighbours']="Blood Cancer"
        elif pred_num==1:
            predictions['KNearestNeighbours']="Lung Cancer"
        elif pred_num==3:
            predictions['KNearestNeighbours']="Stomach Cancer"
        else:
            predictions['KNearestNeighbours']="Blood Cancer"

        if predictions['KMeansClassifier']=='1':
            predictions['KMeansClassifier']="Lung Cancer"
        elif predictions['KMeansClassifier']=='3':
            predictions['KMeansClassifier']="Stomach Cancer"
        elif predictions['KMeansClassifier']=='2':
            predictions['KMeansClassifier']="Blood Cancer"
        elif pred_num==1:
            predictions['KMeansClassifier']="Lung Cancer"
        elif pred_num==3:
            predictions['KMeansClassifier']="Stomach Cancer"
        else:
            predictions['KMeansClassifier']="Blood Cancer"

        if predictions['DecisionTree']=='1':
            predictions['DecisionTree']="Lung Cancer"
        elif predictions['DecisionTree']=='3':
            predictions['DecisionTree']="Stomach Cancer"
        elif predictions['DecisionTree']=='2':
            predictions['DecisionTree']="Blood Cancer"
        elif pred_num==1:
            predictions['DecisionTree']="Lung Cancer"
        elif pred_num==3:
            predictions['DecisionTree']="Stomach Cancer"
        else:
            predictions['DecisionTree']="Blood Cancer"

        if predictions['RandomForestClassifier']=='1':
             predictions['RandomForestClassifier']="Lung Cancer"
        elif predictions['RandomForestClassifier']=='3':
            predictions['RandomForestClassifier']="Stomach Cancer"
        elif predictions['RandomForestClassifier']=='2':
            predictions['RandomForestClassifier']="Blood Cancer"
        elif pred_num==1:
            predictions['RandomForestClassifier']="Lung Cancer"
        elif pred_num==3:
            predictions['RandomForestClassifier']="Stomach Cancer"
        else:
            predictions['RandomForestClassifier']="Blood Cancer"
        
        
        if result:
            return render(request, 'patient/predictions.html',
                      {'pd':pd,'predictions':predictions,'result':result,'colors':colors,'is_cancer':is_cancer})
        else:        
            return render(request,'patient/predict.html')
    else:
        return render(request,'patient/predict.html')
