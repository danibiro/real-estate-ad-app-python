from django.http import HttpResponse
from django.views import View
from bdim1996_x_python import db
from sqlalchemy.orm import Session
from ads.models import RealEstateAd
import logging
import json

class AdViewWithoutParam(View):
    log = logging.getLogger(__name__)

    def date_handler(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()

    def get(self, request):    
        self.log.debug('GET')
        with Session(db.engine) as session:
            session.expire_on_commit = False
            ads = session.query(RealEstateAd).all()
            json_data = json.dumps([ad.__dict__ for ad in ads], default = self.date_handler)
            json_data = json_data.replace('"_sa_instance_state": null, ', '')
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request):
        self.log.info('POST')
        data = json.loads(request.body)
        ad = RealEstateAd(
            title=data['title'],
            description=data['description'],
            address=data['address'],
            date_of_creation=data['date_of_creation'],
            negotiable=data['negotiable'],
            price=data['price'],
            area=data['area'],
            agent_id=data['agent_id']
        )
        with Session(db.engine) as session:
            session.expire_on_commit = False
            session.add(ad)
            session.commit()
        return HttpResponse('New ad added with ID = ' + str(ad.id), content_type='text/plain')
    

class AdViewWithParam(View):   
    def date_handler(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()

    def get(self, request, id):
        with Session(db.engine) as session:
            session.expire_on_commit = False
            ad = session.query(RealEstateAd).filter_by(id=id).first()
            if ad is None:
                return HttpResponse('Ad with ID = ' + str(id) + ' does not exist', content_type='text/plain')
            json_data = json.dumps(ad.__dict__, default = self.date_handler)
            json_data = json_data.replace('"_sa_instance_state": null, ', '')
        return HttpResponse(json_data, content_type='application/json')
    
    def put(self, request, id):
        data = json.loads(request.body)
        with Session(db.engine) as session:
            session.expire_on_commit = False
            ad = session.query(RealEstateAd).filter_by(id=id).first()
            if ad is None:
                return HttpResponse('Ad with ID = ' + str(id) + ' does not exist', content_type='text/plain')
            ad.title = data['title']
            ad.description = data['description']
            ad.address = data['address']
            ad.date_of_creation = data['date_of_creation']
            ad.negotiable = data['negotiable']
            ad.price = data['price']
            ad.area = data['area']
            ad.agent_id = data['agent_id']
            session.commit()
        return HttpResponse('Ad with ID = ' + str(id) + ' updated', content_type='text/plain')

    def delete(self, request, id):
        with Session(db.engine) as session:
            session.expire_on_commit = False
            ad = session.query(RealEstateAd).filter_by(id=id).first()
            if ad is None:
                return HttpResponse('Ad with ID = ' + str(id) + ' does not exist', content_type='text/plain')
            session.delete(ad)
            session.commit()
        return HttpResponse('Ad with ID = ' + str(id) + ' deleted', content_type='text/plain')