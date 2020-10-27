from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from fastai.basic_train import load_learner
from torch import argmax
import os

model = load_learner(os.path.dirname(os.path.abspath(__file__)),'models/KEEPModel.pkl')

#POST requests to /model/ are fed into the model and returns the reponse.
#
@require_POST
@csrf_exempt
def predict(request):
	if request.method == 'POST':
		pred = argmax(model.predict(request.POST.get('details'))[2])
		return JsonResponse(int(pred), safe=False)

	# if request.method == 'GET':
	# 	pred = argmax(model.predict('This is some random text to use as an example for prediction')[2])
	# 	return JsonResponse(int(pred), safe=False)
