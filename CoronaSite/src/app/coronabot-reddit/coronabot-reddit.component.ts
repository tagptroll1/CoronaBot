import { Component, OnInit } from '@angular/core';
import { CoronaRedditService } from './coronabot-reddit.service';

@Component({
  selector: 'coronabot-reddit',
  templateUrl: './coronabot-reddit.component.html',
  styleUrls: ['./coronabot-reddit.component.css']
})
export class CoronabotRedditComponent implements OnInit {
  posts: any[];

  constructor(private _service: CoronaRedditService ) { }

  ngOnInit(): void {
    this._service.getTop10().subscribe(posts => console.log(posts))
  }

}
