import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { EventPage } from '../event/event';

@Component({
  selector: 'page-place',
  templateUrl: 'place.html'
})
export class PlacePage {
  place;
  constructor(params: NavParams, public navCtrl: NavController) {
    this.place = params.data.place;
  }

  openEventPage(event) {
    this.navCtrl.push(EventPage, { event: event});
  }
}

