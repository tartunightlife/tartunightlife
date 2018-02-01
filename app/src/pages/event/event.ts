import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';

@Component({
  selector: 'page-event',
  templateUrl: 'event.html'
})
export class EventPage {
  event;
  constructor(params: NavParams) {
    this.event = params.data.item;
  }

}

