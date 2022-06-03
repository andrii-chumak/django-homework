from .models import CoxitWorker, Position


def workers_dict():
    coxit_workers = CoxitWorker.objects.all()
    
    json_dict = {}
    for num, worker in enumerate(coxit_workers):
        json_dict[num] = worker.json
        
    return json_dict


def position_workers_dict(position):
    position_id = Position.objects.filter(name=position).first()
    if position_id is None:
        return {}
    
    coxit_workers = CoxitWorker.objects.filter(workerposition__position=position_id)
    json_dict = {}
    for num, worker in enumerate(coxit_workers):
        json_dict[num] = worker.json
        
    return json_dict



def hire_worker(data):
    worker = CoxitWorker.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        birthday=data['birthday'],
        salary=500 * len(data['first_name']),
    )
    
    worker.save()
    return worker.json