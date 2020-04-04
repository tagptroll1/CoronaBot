import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CounterComponent } from './counter/counter.component';
import { HomepageComponent } from './homepage/homepage.component';
import { CoronabotCommandsComponent } from './coronabot-commands/coronabot-commands.component';
import { CoronabotFeaturesComponent } from './coronabot-features/coronabot-features.component';
import { CoronabotRedditComponent } from './coronabot-reddit/coronabot-reddit.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    CounterComponent,
    HomepageComponent,
    CoronabotCommandsComponent,
    CoronabotFeaturesComponent,
    CoronabotRedditComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
