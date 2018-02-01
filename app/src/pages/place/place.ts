import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';

@Component({
  selector: 'page-place',
  templateUrl: 'place.html'
})
export class PlacePage {
  place;
  constructor(params: NavParams) {
    this.place = params.data.place;
  }

}

