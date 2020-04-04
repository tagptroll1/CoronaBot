import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoronabotRedditComponent } from './coronabot-reddit.component';

describe('CoronabotRedditComponent', () => {
  let component: CoronabotRedditComponent;
  let fixture: ComponentFixture<CoronabotRedditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoronabotRedditComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoronabotRedditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
