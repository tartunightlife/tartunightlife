import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { PlacePage } from '../place/place';

@Component({
  selector: 'page-places',
  templateUrl: 'places.html'
})
export class PlacesPage {
  places = [];
  constructor(public navCtrl: NavController) {
    this.places = [
                   {id:1, name:'moku', address:'moku-address', url:'moku-url'},
                   {id:2, name:'Sooters', address:'Sooters-address', url:'Sooters-url'},
                   {id:3, name:'Illusion', address:'Illusion-address', url:'Illusion-url'}
                  ];
  }

  openPlacePage(place) {
    this.navCtrl.push(PlacePage, { place: place});
  }

}



