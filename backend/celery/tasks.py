import flask_excel
import time
from celery import shared_task
from backend.models import Blog
from backend.celery.mail_service import send_email


@shared_task(ignore_results = False)
def add(x,y):
    time.sleep()
    return x+y

@shared_task(bind=True,ignore_results = False)
def create_csv(self):
    resource = Blog.query.all()
    #for creating new filenames for blog
    task_id = self.request.id
    filename =f'blog_data_{task_id}.csv'
    column_names =[column.name for column in Blog.__table__.columns]
    csv_out= flask_excel.make_response_from_query_sets(resource,column_names=column_names,file_type='csv')
    
    with open(f'./backend/celery/user-downloads/{filename}','wb') as file:
        file.write(csv_out.data)
    return filename

@shared_task(ignore_result=True)
def email_reminder(to,subject,content):
    send_email(to,subject,content)