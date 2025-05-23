from celery import shared_task
import time
from backend.models import Blog
import flask_excel

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