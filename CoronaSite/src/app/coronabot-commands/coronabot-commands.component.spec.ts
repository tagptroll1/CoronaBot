import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoronabotCommandsComponent } from './coronabot-commands.component';

describe('CoronabotCommandsComponent', () => {
  let component: CoronabotCommandsComponent;
  let fixture: ComponentFixture<CoronabotCommandsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoronabotCommandsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoronabotCommandsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
