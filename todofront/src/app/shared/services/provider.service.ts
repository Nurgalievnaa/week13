import {Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {ITaskList, ITask} from '../models/TaskList';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]> {
    return this.get('http://localhost:8000/api/tasklists/', {});
  }

  getTaskListsTasks(id: number): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/tasklists/${id}/tasks/`, {});
  }

}