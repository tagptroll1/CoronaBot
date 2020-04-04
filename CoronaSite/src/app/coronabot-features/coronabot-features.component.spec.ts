import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoronabotFeaturesComponent } from './coronabot-features.component';

describe('CoronabotFeaturesComponent', () => {
  let component: CoronabotFeaturesComponent;
  let fixture: ComponentFixture<CoronabotFeaturesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoronabotFeaturesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoronabotFeaturesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
