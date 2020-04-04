import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';

@Injectable({providedIn: 'root'})
export class CoronaRedditService {
  private baseUrl = "https://www.reddit.com/r/coronavirus";
  private httpOptions = {
    mode: "cors",
    headers: new HttpHeaders({
      'User-Agent':  'angular httpclient (by u/peebls)',
    })
  };

  constructor(private httpClient: HttpClient) { }
  
  getTop10(): Observable<any[]> {
    return this.httpClient.get<any[]>(`${this.baseUrl}/top?count=10`, this.httpOptions)
  }
}