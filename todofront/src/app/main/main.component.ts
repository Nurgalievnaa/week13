import {Component, OnDestroy, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITaskList, ITask} from '../shared/models/TaskList';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit, OnDestroy {

  public subTitle = '';
  public array2: any[] = [];

  public tasklists: ITaskList[] = [];
  public loading = false;

  public interval;
  public i = 0;

  public tasks: ITask[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {

    this.provider.getTaskLists().then(res => {
      this.tasklists = res;
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });

  }

  getTask(TaskList: ITask) {
    this.provider.getTaskListsTasks(TaskList.id).then(res => {
      this.tasks = res;
    });
  }

  ngOnDestroy() {
    clearInterval(this.interval);
  }

}